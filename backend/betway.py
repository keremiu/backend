import selenium
import time
import pandas as pd
from selenium import webdriver
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # Added import
from myDB import myDB
def web_Scrapping():
    targetWeb ='https://betway.com/en/sports/grp/soccer/turkey/super-lig'
    #'https://betway.com/en/sports/grp/soccer/usa/mls'
    opera_profile = '/home/dan/.config/opera' 
    options = webdriver.ChromeOptions()
    options.add_argument('user-data-dir=' + opera_profile)
    options.add_experimental_option('w3c', True)
    driver = webdriver.Opera(options=options , executable_path=r'C:\Users\kerem\anaconda3\Scripts\operadriver.exe')
    driver.get(targetWeb)
    teams = []
    x12 = [] #3-way;
    wait = WebDriverWait(driver, 120)
    wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "div")))
    try:
        # Wait up to 10 seconds before throwing a TimeoutException unless it finds the element to return within 10 seconds
        WebDriverWait(driver, 120).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.oneLineEventItem div.odds')))
    except TimeoutException:
        print('Timed out waiting for page to load')
        driver.quit()
    odds_elements = driver.find_elements(By.CSS_SELECTOR,'div.oneLineEventItem div.odds')
    odds_values = [element.text for element in odds_elements]
    team_elements = driver.find_elements(By.CSS_SELECTOR,'span.teamNameFirstPart.teamNameHomeTextFirstPart, span.teamNameFirstPart.teamNameAwayTextFirstPart')
    team = []

    for element in team_elements:
        team.append(element.text)
    for i in range(0, len(odds_values), 3):
        obje = odds_values[i:i+3]  # Her üç elemanı bir obje olarak al
        x12.append(obje)
    teams = []
    for i in range(0, len(team), 2):
        if i + 1 < len(team):
            element = team[i] + "-" + team[i + 1]  # Araya "-" ekleyerek yeni elemanı oluştur
            teams.append(element)
    dict_gambling = {'Teams': teams, '1x2': x12}
    df_gambling = pd.DataFrame.from_dict(dict_gambling)
    myDB.update_to_mongo('BahisSiteleriCur3', 'betway', df_gambling)
    driver.quit()
    
web_Scrapping()