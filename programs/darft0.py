from nturl2path import url2pathname
from os import path
from pydoc import pathdirs
from tabnanny import check
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
    #try:
        #driver.find_elements_by_class_name('sys-form-button')[0].click()
    #except:
        #pass
    #try:
        #driver.find_elements_by_class_name('sys-form-button')[1].click()
    #except:
        #pass
    #try:
        #driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div[2]/div/div/div/button').click()
    #except:
        #pass

def clearWindow():
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    driver.find_element_by_xpath('//*[@id="ce_rd8pkw_rw"]/div/button').click()
    driver.switch_to.default_content()

clearWindow()

time.sleep(5)

# continue to the search page

driver.find_element_by_xpath('//*[@id="c_rd8pkw_1c5-c_rd8pkw_1c5"]/div/div[3]')\
    .click() # clcik on the search option

time.sleep(5)

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

#filterNme()

#time.sleep(8)

def checkBox():
    try:
        elements=driver.find_elements_by_class_name('yui-dt-checkbox')
        for i in elements:
            i.click()
    except:
        pass

checkBox()

time.sleep(5)

def download():
    driver.find_element_by_xpath('//*[@id="c_rd8pkw_1cj_btns"]/div[3]/button[4]').click()
    time.sleep(5)
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    driver.find_element_by_xpath('//*[@id="ce_rd8pkw_13p_2"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="ce_rd8pkw_13v"]/div/button').click()
    time.sleep(30)
    driver.switch_to.default_content()

#download()


#driver.find_element_by_xpath('//*[@id="yui-pg0-0-next-link70"]').click()

driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/a[1]').click()

clearPopUp()

time.sleep(5)

def checkAndJump():
    try:
        elements=driver.find_elements_by_class_name('yui-dt-checkbox')
        for i in elements:
            i.click()
    except:
        pass
    time.sleep(10)
    try:
        driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/a[1]').click()
    except:
        pass
    clearPopUp()


def switchPage(i): # does not work as intended, checkAndJump() works
    for _ in range(i):
        checkAndJump()

checkAndJump()