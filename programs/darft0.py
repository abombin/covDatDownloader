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
    try:
        driver.find_elements_by_class_name('sys-form-button')[0].click()
    except:
        pass
    try:
        driver.find_elements_by_class_name('sys-form-button')[1].click()
    except:
        pass
    try:
        driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div[2]/div/div/div/button').click()
    except:
        pass

# need to try to switch to window

#clearPopUp()     

#time.sleep(10)

# continue to the search page

driver.find_element_by_xpath('//*[@id="c_rd8pkw_1c5-c_rd8pkw_1c5"]/div/div[3]')\
    .click() # clcik on the search option

time.sleep(10)

def sortSubmuit():
	print("Sorting by submission date...")
	submission_date = driver.find_element_by_xpath("//a[@class='yui-dt-sortable'][text()='Submission Date']")
	submission_date.click()
	time.sleep(10)
	submission_date = driver.find_element_by_xpath("//a[@class='yui-dt-sortable'][text()='Submission Date']")
	submission_date.click()

def filterNme():
    try:
        driver.find_element_by_id('ce_rd8pkw_s2_entry').send_keys('hCoV-19/USA/GA-EHC')
    except:
        pass


#sortSubmuit()

filterNme()

time.sleep(8)

def checkBox():
    try:
        driver.find_elements_by_class_name('yui-dt-checkbox')[2].click()
    except:
        pass

checkBox()