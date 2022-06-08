from nturl2path import url2pathname
from os import path
from pydoc import pathdirs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

drPath='C:/Users/abomb/Projects/covDatDownloader/chromedriver.exe'
gisaidUser='../gisaidLogin.txt'
gisaidPassword='../gisadPassword.txt'
gisaidPath='https://www.epicov.org/epi3/frontend#45e4b1'

def getInfo(file):
    with open(file) as f:
        text = f.read()
    return text

login=getInfo(gisaidUser)
password=getInfo(gisaidPassword)


options = Options()
options.add_argument("--disable-notifications")



driver=webdriver.Chrome(drPath)
driver.get(gisaidPath)

driver.find_element_by_id('elogin').send_keys(login)
driver.find_element_by_id('epassword').send_keys(password)

driver.find_elements_by_class_name('form_button_submit')[0].click()

time.sleep(20) # sleep to deal with pop up manually

driver.find_element_by_xpath('//*[@id="c_rd439f_1az-c_rd439f_1az"]/div/div[3]')\
    .click() # clcik on the search option