# make program that will select 1 day for each state and download sequences

from os import path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

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

driver=webdriver.Chrome(drPath)
driver.get(gisaidPath)

driver.find_element_by_id('elogin').send_keys(login)
driver.find_element_by_id('epassword').send_keys(password)

driver.find_elements_by_class_name('form_button_submit')[0].click()

time.sleep(10) # sleep to deal with pop up manually

def clearPopUp():
    try:
        alert=driver.switch_to.alert()
        alert.acept()
    except:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="ce_rd8pkw_rw"]/div/button').click()
    except:
        pass

def clearWindow():
    try:
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        driver.find_element_by_xpath('//*[@id="ce_rd8pkw_rw"]/div/button').click()
        driver.switch_to.default_content()
    except:
        pass

clearWindow()

time.sleep(3)

driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[1]/div/div/div[3]')\
    .click() # clcik on the search option

time.sleep(5)


def filterNme():
    try:
        driver.find_element_by_id('ce_rdf3cu_rv_entry').send_keys('hCoV-19/USA/GA-EHC')
    except:
        pass

filterNme()

time.sleep(15)

driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/table/thead/tr/th[1]/div/span/input').click()
