import selenium
import time
import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # Added import
from myDB import myDB
def web_Scrapping():
    targetWeb ='https://www.unibet.com/betting/sports/filter/football/turkey/super_lig/all/matches'
    #'https://www.unibet.com/betting/sports/filter/football/usa/mls/all/matches'
    # The profile where I enabled the VPN previously using the GUI.
    opera_profile = '/home/dan/.config/opera' 
    options = webdriver.ChromeOptions()
    options.add_argument('user-data-dir=' + opera_profile)
    options.add_experimental_option('w3c', True)
    driver = webdriver.Opera(options=options , executable_path=r'C:\Users\kerem\anaconda3\Scripts\operadriver.exe')
    driver.get(targetWeb)
    #Initialize your storage
    teams = []
    x12 = [] #3-way;
    wait = WebDriverWait(driver, 120)
    wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "div")))
    try:
        # Wait up to 10 seconds before throwing a TimeoutException unless it finds the element to return within 10 seconds
        WebDriverWait(driver, 120).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"div.f9aec._0c119.bd9c6")))
    except TimeoutException:
        print('Timed out waiting for page to load')
        driver.quit()
    # Verileri depolamak için boş listeler oluştur
    team = []
    odds = []
    # İlgili elementleri bul
    elements = driver.find_elements(By.CSS_SELECTOR,"div.f9aec._0c119.bd9c6")
    # Her bir element için takım adını ve oranı al
    for element in elements:
        team_elements = element.find_elements(By.CSS_SELECTOR,"div.c539a")
        odds_elements = element.find_elements(By.CSS_SELECTOR,"span._8e013")
        # Takım adlarını listeye ekle
        for team_element in team_elements:
            team.append(team_element.text)
        # Oranları listeye ekle
        for odds_element in odds_elements:
            odds.append(odds_element.text)
    # WebDriver'ı kapatma
    for i in range(0, len(odds), 3):
        obje = odds[i:i+3]  # Her üç elemanı bir obje olarak al
        x12.append(obje)
    teams = []
    for i in range(0, len(team), 2):
        if i + 1 < len(team):
            element = team[i] + "-" + team[i + 1]  # Araya "-" ekleyerek yeni elemanı oluştur
            teams.append(element)
    dict_gambling = {'Teams': teams, '1x2': x12}
    df_gambling = pd.DataFrame.from_dict(dict_gambling)
    myDB.update_to_mongo('BahisSiteleriCur3', 'unibet', df_gambling)
    driver.quit()
web_Scrapping()
