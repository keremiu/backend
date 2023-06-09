import selenium
import time
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from myDB import myDB
def web_Scrapping():
    targetWeb ='https://www.misli.com/iddaa/futbol'
    driver= webdriver.Chrome(executable_path=r"C:\\Users\\kerem\\anaconda3\\Scripts\\chromedriver")
    driver.get(targetWeb)

    wait = WebDriverWait(driver, 120)
    wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "div")))
    cookie_accept_button = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
    )
    cookie_accept_button.click()
    close_button = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='btn btn-orange tutorialClose']"))
    )
    close_button.click()
    first_button = WebDriverWait(driver, 120).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='filter-select filter-league']//button[@class='filter-select-btn']"))
    )
    first_button.click()
    # belirli bir metne sahip öğeyi bekleyin
    element = WebDriverWait(driver, 120).until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Türkiye - Türkiye Süper Lig')]"))
    ) 
    parent = element.find_element(By.XPATH,'./..') 
    checkbox = parent.find_element(By.XPATH,'.//input') 
    checkbox.click()
    '''element = WebDriverWait(driver, 120).until( #amerika 
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'ABD - ABD Major Lig')]"))
    )
    parent = element.find_element(By.XPATH,'./..') 
    checkbox = parent.find_element(By.XPATH,'.//input') 
    checkbox.click()'''
    apply_button = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='apply-filter selected']"))
    )
    apply_button.click()
    #Initialize your storage
    teams = []
    super_odds = []
    rows = driver.find_elements(By.CSS_SELECTOR,".bulletinRowInner")
    teams = []
    super_odds = []
    # Her bir row için işlem yap
    for row in rows:
        # Home ve Away takımlarını bul ve listeye ekle
        home_team = row.find_element(By.CSS_SELECTOR,".bulletinHomeTeam").text
        away_team = row.find_element(By.CSS_SELECTOR,".bulletinAwayTeam").text
        teams.append(home_team)
        teams.append(away_team)

        # superOdd veya lastOdd elementlerini bul ve listeye ekle
        divs = row.find_elements(By.CSS_SELECTOR,"div")
        for div in divs:
            try:
                span = div.find_element(By.CSS_SELECTOR, 'span.superOdd')
            except NoSuchElementException:
                try:
                    span = div.find_element(By.CSS_SELECTOR, 'span.lastOdd')
                except NoSuchElementException:
                    continue  # if neither 'superOdd' nor 'lastOdd' are present, skip this div
            super_odds.append(span.text)
    from collections import OrderedDict
    new_super_odds = []
    seen = set()
    for value in super_odds:
        stripped_value = value.strip()
        if stripped_value == "":
            continue
        if stripped_value not in seen or new_super_odds[-1] != stripped_value:
            new_super_odds.append(stripped_value)
        seen.add(stripped_value)
    super_odds = new_super_odds
    teams_updated = []
    for i in range(0, len(teams), 2):
        if i + 1 < len(teams):
            element = teams[i] + "-" + teams[i + 1]  # Araya "-" ekleyerek yeni elemanı oluştur
            teams_updated.append(element)
    x12 = []
    for i in range(0, len(super_odds), 3):
        obje = super_odds[i:i+3]  # Her üç elemanı bir obje olarak al
        x12.append(obje)
    dict_gambling = {'Teams': teams_updated, '1x2': x12}
    print(dict_gambling)
    df_gambling = pd.DataFrame.from_dict(dict_gambling)
    myDB.update_to_mongo('BahisSiteleriCur3', 'misli', df_gambling)
    driver.quit()
web_Scrapping()