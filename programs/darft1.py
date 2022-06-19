# make program that will select 1 day for each state and download sequences

from os import path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

drPath='C:/Users/abomb/Projects/covDatDownloader/chromedriver.exe'
gisaidUser='../gisaidLogin.txt'
gisaidPassword='../gisadPassword.txt'
gisaidPath='https://www.epicov.org/epi3/frontend#45e4b1'

# get name and password from a file
def getInfo(file):
    with open(file) as f:
        text = f.read()
    return text

# start driver
driver=webdriver.Chrome(drPath)
driver.get(gisaidPath)

# log in to the website
def logIn(login, password):
    driver.find_element_by_id('elogin').send_keys(login)
    driver.find_element_by_id('epassword').send_keys(password)
    driver.find_elements_by_class_name('form_button_submit')[0].click()
    time.sleep(5)
    print('Logged in')

# clear simple pop ups
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

# clear Gisaid promotion window
def clearWindow():
    try:
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        driver.find_element_by_xpath('//*[@id="ce_rd8pkw_rw"]/div/button').click()
        driver.switch_to.default_content()
    except:
        pass

# get to covid search option
def epiSearch():
    # Epicov
    try:
        driver.find_element_by_xpath('/html/body/form/div[5]/div/div[1]/div/div/div/div/div[2]/div/ul/li[3]/a')\
            .click()
    except:
        pass
    time.sleep(3)
    # Search
    try:
        driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[1]/div/div/div[3]')\
            .click() # clcik on the search option
    except:
        pass
    time.sleep(5)
    print('Went EpiSearch')

# Filter samples by name
def filterName(sampName):
    # virus name
    try:
        driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[1]/div/table/tbody/tr[2]/td[2]/div[3]/div/div[1]/input').\
            send_keys(sampName)
    except:
        pass
    time.sleep(10)
    print('Filtered by Name')

# filter b location
def filterLocation(location):
    try:
        driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[1]/div/table/tbody/tr[3]/td[2]/div/div/div/div[1]/input').\
            send_keys(location)
    except:
        pass
    time.sleep(10)

# filter by submuission date
def filterDate(day):
    # start date element
    try:
       startDay=driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[1]/div/table/tbody/tr[4]/td[2]/div[5]/div/div[1]/input')
       startDay.send_keys(day) 
    except:
        pass
    time.sleep(5)
    # end date
    try:
        endDay=driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[1]/div/table/tbody/tr[4]/td[2]/div[7]/div/div[1]/input')
        endDay.send_keys(day)
    except:
        pass
    time.sleep(5)

# clear dates input
def clearDate():
    # start date
    try:
       startDay=driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[1]/div/table/tbody/tr[4]/td[2]/div[5]/div/div[1]/input')
       startDay.clear()
    except:
        pass
    time.sleep(5)
    # end date
    try:
        endDay=driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[1]/div/table/tbody/tr[4]/td[2]/div[7]/div/div[1]/input')
        endDay.clear()
    except:
        pass
    time.sleep(5)

# Download 
def download():
    # select all the samples 
    try:
        driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/table/thead/tr/th[1]/div/span/input')\
            .click()
    except:
        pass
    time.sleep(8)
    try:
        # download button
        driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[2]/div[2]/div[3]/button[4]').click()
        time.sleep(5)
        # go to opened window
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        # select augur pipeline
        driver.find_element_by_xpath('/html/body/form/div[5]/div/div[1]/div/div/table[1]/tbody/tr/td[2]/div/div[1]/div[2]/div[2]/input').click()
        time.sleep(2)
        # click download
        driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div/div[2]/div/button').click()
        time.sleep(30)
        # go back to normal page
        driver.switch_to.default_content()
        time.sleep(2)
    except:
        pass
    time.sleep(15)
    try:
        # deselect all the samples
        driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/table/thead/tr/th[1]/div/span/input')\
            .click()
    except:
        pass
    time.sleep(10)

# find the number of samples selected for download
def samplesNum():
    sampNumb=''
    for elem in driver.find_elements_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/span/span'):
        sampNumb+=elem.text
    return(sampNumb)

# set variables
login=getInfo(gisaidUser)
password=getInfo(gisaidPassword)
sampName='hCoV-19/USA/GA-EHC'
location='North America / USA / Georgia'
# input the range of dates
date_rng = pd.date_range('2021-01-01','2021-01-03',freq='D')
dates=pd.Series(date_rng.format()).tolist()

# run functions
def runDays():
    logIn(login, password)
    epiSearch()
    filterName(sampName)
    filterLocation(location)
    for day in dates:
        filterDate(day)
        download()
        clearDate()

runDays()




