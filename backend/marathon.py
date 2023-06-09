import selenium
import time
import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException  # Added import

def web_Scrapping():
    targetWeb ='https://www.marathonbet.com/tr/betting/Football/Turkey/Super+Lig+-+46180'
    #'https://www.marathonbet.com/tr/betting/Football/USA/MLS+-+138152'
    # The profile where I enabled the VPN previously using the GUI.
    opera_profile = '/home/dan/.config/opera' 
    options = webdriver.ChromeOptions()
    options.add_argument('user-data-dir=' + opera_profile)
    options.add_experimental_option('w3c', True)
    driver = webdriver.Opera(options=options , executable_path=r'C:\Users\kerem\anaconda3\Scripts\operadriver.exe')
    driver.get(targetWeb)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "div")))
    try:
        # Wait up to 10 seconds before throwing a TimeoutException unless it finds the element to return within 10 seconds
        WebDriverWait(driver, 120).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.selection-link.active-selection")))
        WebDriverWait(driver, 120).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span[data-member-link='true']")))
    except TimeoutException:
        print('Timed out waiting for page to load')
        driver.quit()
    teams = []
    x12 = [] #3-way;
    # 1x2 array için:
    prices = driver.find_elements(By.CSS_SELECTOR, "span.selection-link.active-selection")
    prices_array = [price.text for price in prices]

    # teams array için:
    teams = driver.find_elements(By.CSS_SELECTOR, "span[data-member-link='true']")
    teams_array = [team.text for team in teams]
    for i in range(0, len(prices_array), 3):
        obje = prices_array[i:i+3]  # Her üç elemanı bir obje olarak al
        x12.append(obje)
    teams = []
    for i in range(0, len(teams_array), 2):
        if i + 1 < len(teams_array):
            element = teams_array[i] + "-" + teams_array[i + 1]  # Araya "-" ekleyerek yeni elemanı oluştur
            teams.append(element)
    dict_gambling = {'Teams': teams, '1x2': x12}
    df_gambling = pd.DataFrame.from_dict(dict_gambling)
    df_gambling.to_json(r'marathon.json')
    driver.quit()  # tarayıcıyı kapat

web_Scrapping()