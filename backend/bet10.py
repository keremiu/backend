import selenium
import time
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # Added import
from myDB import myDB
def web_Scrapping():
    targetWeb = 'https://www.10bet.com/sports/football/turkey-super-ligi/'
    #'https://www.10bet.com/sports/football/usa-mls/'#amerika
    #'https://www.10bet.com/sports/football/turkey-super-ligi/'
    opera_profile = '/home/dan/.config/opera' 
    options = webdriver.ChromeOptions()
    options.add_argument('user-data-dir=' + opera_profile)
    options.add_experimental_option('w3c', True)
    driver = webdriver.Opera(options=options , executable_path=r'C:\Users\kerem\anaconda3\Scripts\operadriver.exe')
    driver.get(targetWeb)

    wait = WebDriverWait(driver, 120)
    wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "div")))
    #Initialize your storage
    teams = []
    x12 = [] #3-way;
    try:
        # Wait up to 10 seconds before throwing a TimeoutException unless it finds the element to return within 10 seconds
        WebDriverWait(driver, 120).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.rj-ev-list__ev-card--upcoming')))
    except TimeoutException:
        print('Timed out waiting for page to load')
    elements = driver.find_elements(By.CSS_SELECTOR,'div.rj-ev-list__ev-card--upcoming')
    # Her element için gerekli veriyi al
    values = [element.text for element in elements]
    for item in values:
        odds = []
        lines = item.split('\n')
        team = lines[0] + '-'+ lines[1]
        odds.append(lines[5])
        odds.append(lines[7])
        odds.append(lines[9])
        x12.append(odds)
        teams.append(team)
    #Storing lists within dictionary
    dict_gambling = {'Teams': teams, '1x2': x12}
    #Presenting data in dataframe
    df_gambling = pd.DataFrame.from_dict(dict_gambling)
    myDB.update_to_mongo('BahisSiteleriCur3', 'bet10', df_gambling)
    driver.quit()
    
web_Scrapping()
