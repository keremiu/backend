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
    targetWeb ='https://www.tuttur.com/bulten/futbol#2=parameter-leagueId-584|3=sort-leaguePriority-1'
    #'https://www.tuttur.com/bulten/futbol#2=parameter-leagueId-15|3=sort-date-1' US
    driver= webdriver.Chrome(executable_path=r"C:\\Users\\kerem\\anaconda3\\Scripts\\chromedriver")
    driver.get(targetWeb)
    #Initialize your storage
    teams = []
    x12 = [] #3-way;
    wait = WebDriverWait(driver, 120)
    wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "div")))
    try:
        # Wait up to 10 seconds before throwing a TimeoutException unless it finds the element to return within 10 seconds
        WebDriverWait(driver, 120).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="ReactVirtualized__Grid__innerScrollContainer"]')))
    except TimeoutException:
        print('Timed out waiting for page to load')
        driver.quit()
    # find the container element
    container = driver.find_element(By.XPATH, '//div[@class="ReactVirtualized__Grid__innerScrollContainer"]')
    # find all odds elements within the container
    odds_elements = container.find_elements(By.XPATH, './/div[@class="sportsbookEventOdds"]')
    # find all team elements within the container
    teams_elements = container.find_elements(By.XPATH, './/div[@class="sportsbookEventRow-header-team"]')
    # prepare the arrays
    odds_array = []  # preparing an array to store odds arrays
    teams_array = []
    # populate odds_array
    for odds_element in odds_elements:
        # preparing an array for the current 'sportsbookEventOdds' div
        current_odds = [None, None, None]

        for tag, index in [('1', 0), ('X', 1), ('2', 2)]:
            try:
                outcome_element = odds_element.find_element(By.XPATH, f'.//div[@class="eventOdd-name"][text()="{tag}"]/following-sibling::div')
                current_odds[index] = outcome_element.text
            except:
                pass  # if an element is not found, just pass

        x12.append(current_odds)
    # populate teams_array
    for element in teams_elements:
        teams_array.append(element.text)
    teams_updated = []
    for i in range(0, len(teams_array), 2):
        if i + 1 < len(teams_array):
            element = teams_array[i] + "-" + teams_array[i + 1]  # Araya "-" ekleyerek yeni elemanı oluştur
            teams_updated.append(element)
    # WebDriver'ı kapatma
    dict_gambling = {'Teams': teams_updated, '1x2': x12}
    df_gambling = pd.DataFrame.from_dict(dict_gambling)
    myDB.update_to_mongo('BahisSiteleriCur3', 'tuttur', df_gambling)
    driver.quit()
web_Scrapping()
