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
    targetWeb = 'https://www.888sport.com/football/turkey/turkey-super-lig-t-320219/'
    #'https://www.888sport.com/football/united-states-of-america/us-major-league-soccer/'# amerika
    #'https://www.888sport.com/football/turkey/turkey-super-lig-t-320219/' türk
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
        WebDriverWait(driver, 120).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.bet-card')))
    except TimeoutException:
        print('Timed out waiting for page to load')
        driver.quit()
    team = []
    odds_values = []
    bet_cards = driver.find_elements(By.CSS_SELECTOR,'div.bet-card')
    for bet_card in bet_cards:
        team_elements = bet_card.find_elements(By.CSS_SELECTOR,'span.event-description__competitor-text')
        odd_elements = bet_card.find_elements(By.CSS_SELECTOR,'span.bb-sport-event__selection')
        
        for team_element in team_elements:
            team.append(team_element.text)
        
        for odd_element in odd_elements:
            odds_values.append(odd_element.text)
    odds_float = []
    for odd in odds_values:
        numerator, denominator = odd.split('/')
        numerator = float(numerator)
        denominator = float(denominator)
        
        # İşlem sonucunda sıfıra bölme hatasını önlemek için kontrol yapılır
        if denominator != 0:
            odd_float = numerator / denominator
        else:
            odd_float = 0.0
        
        odd_float = round(odd_float, 3)  # Virgülden sonra en fazla 3 basamak
        
        odds_float.append(odd_float)
    for i in range(0, len(odds_float), 3):
        obje = odds_float[i:i+3]  # Her üç elemanı bir obje olarak al
        x12.append(obje)
    teams = []
    for i in range(0, len(team), 2):
        if i + 1 < len(team):
            element = team[i] + "-" + team[i + 1]  # Araya "-" ekleyerek yeni elemanı oluştur
            teams.append(element)
    dict_gambling = {'Teams': teams, '1x2': x12}
    df_gambling = pd.DataFrame.from_dict(dict_gambling)
    myDB.update_to_mongo('BahisSiteleriCur3', '888sport', df_gambling)
    driver.quit()
    

web_Scrapping()