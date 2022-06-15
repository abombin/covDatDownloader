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

def logIn(login, password):
    driver.find_element_by_id('elogin').send_keys(login)
    driver.find_element_by_id('epassword').send_keys(password)
    driver.find_elements_by_class_name('form_button_submit')[0].click()
    time.sleep(5)
    print('Logged in')


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

def epiSearch():
    try:
        driver.find_element_by_xpath('/html/body/form/div[5]/div/div[1]/div/div/div/div/div[2]/div/ul/li[3]/a')\
            .click()
    except:
        pass
    time.sleep(3)
    try:
        driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[1]/div/div/div[3]')\
            .click() # clcik on the search option
    except:
        pass
    time.sleep(5)
    print('Went EpiSearch')



sampName='hCoV-19/USA/GA-EHC'

def filterName(sampName):
    try:
        driver.find_element_by_id('ce_rdf3cu_rv_entry').send_keys(sampName)
    except:
        pass
    time.sleep(10)
    print('Filtered by Name')

location='North America / USA / Georgia'

def filterLocation(location):
    try:
        driver.find_element_by_id('ce_rdf3cu_rx_entry').send_keys(location)
    except:
        pass
    time.sleep(10)

#day= '2022-06-14'
def filterDate(day):
    try:
       driver.find_element_by_id('ce_rdf3cu_s1_input').send_keys(day) 
    except:
        pass
    time.sleep(5)
    try:
        driver.find_element_by_id('ce_rdf3cu_s2_input').send_keys(day)
    except:
        pass
    time.sleep(5)


def download():
    try:
        driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/table/thead/tr/th[1]/div/span/input')\
            .click()
    except:
        pass
    time.sleep(15)
    driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/table/thead/tr/th[1]/div/span/input')\
        .click()
    time.sleep(10)

# run functions
#logIn(login, password)
#epiSearch()
#filterName(sampName)
#filterLocation(location)
#filterDate(day)
#download()
days= ['2022-06-14', '2022-06-15']

def runDays():
    logIn(login, password)
    epiSearch()
    filterName(sampName)
    for i in days:
        day=i
        filterDate(day)
        download()


