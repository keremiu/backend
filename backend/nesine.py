import selenium
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.common.exceptions import TimeoutException  # Added import
from myDB import myDB
def web_Scrapping():
    targetWeb =r"https://www.nesine.com/iddaa?et=1&lc=584&le=1&ocg=MS-2%2C5&gt=Pop%C3%BCler"
    #r'https://www.nesine.com/iddaa?et=1&lc=15&le=1&ocg=MS-2%2C5&gt=Pop%C3%BCler'
    driver= webdriver.Chrome(executable_path=r"C:\\Users\\kerem\\anaconda3\\Scripts\\chromedriver")
    driver.get(targetWeb)
    '''wait = WebDriverWait(driver, 60)
    wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "div")))
    try:
        WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.ID, "c-p-bn")))
    except TimeoutException:
        print('Timed out waiting for page to load')
        driver.quit()
    cookie_accept_button = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "c-p-bn"))
    )
    cookie_accept_button.click() '''
    #Initialize your storage
    teams = []
    odd_3_list = [] #3-way;
    try:
        WebDriverWait(driver, 120).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"div[class='odd-col event-list pre-event']")))
    except TimeoutException:
        print('Timed out waiting for page to load')
        driver.quit()

    event_divs = driver.find_elements(By.CSS_SELECTOR,"div[class='odd-col event-list pre-event']")

    # "name" sınıfına sahip öğelerin metinlerini teams listesine aktar
    for event_div in event_divs:
        name_div = event_div.find_element(By.CSS_SELECTOR,"div.name")
        teams.append(name_div.text)
    event_rows = driver.find_elements(By.CSS_SELECTOR,"dd.col-03.event-row")
    # Her bir <dd class="col-03 event-row"> öğesi için odd değerlerini alın ve listeye ekleyin
    for event_row in event_rows:
        odd_elements = event_row.find_elements(By.CSS_SELECTOR,"a.odd")
        odd_values = [odd.text if odd.text else None for odd in odd_elements]
        odd_3_list.append(odd_values)
    odd_3_list = odd_3_list[::2]
    dict_gambling = {'Teams': teams, '1x2': odd_3_list}
    #Presenting data in dataframe
    df_gambling = pd.DataFrame.from_dict(dict_gambling)
    myDB.update_to_mongo('BahisSiteleriCur3', 'nesine', df_gambling)
    driver.quit()

web_Scrapping()
