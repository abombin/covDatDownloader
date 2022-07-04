from os import path
from turtle import down
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

time.sleep(5)
# log in to the website
def logIn(login, password):
    driver.find_element_by_id('elogin').send_keys(login)
    driver.find_element_by_id('epassword').send_keys(password)
    driver.find_elements_by_class_name('form_button_submit')[0].click()
    time.sleep(8)
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
    driver.find_element_by_xpath('/html/body/form/div[5]/div/div[1]/div/div/div/div/div[2]/div/ul/li[3]/a')\
        .click()
    time.sleep(6)
    # Search
    driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[1]/div/div/div[3]')\
        .click() # clcik on the search option
    time.sleep(5)
    print('Went EpiSearch')

# Filter samples by name
def filterName(sampName):
    time.sleep(2)
    # virus name
    driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[1]/div/table/tbody/tr[2]/td[2]/div[3]/div/div[1]/input').\
        send_keys(sampName)
    time.sleep(8)
    print('Filtered by Name')

# filter by location
def filterLocation(location):
    driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[1]/div/table/tbody/tr[3]/td[2]/div/div/div/div[1]/input').\
        send_keys(location)
    time.sleep(8)

# filter by submuission date
def filterDate(day):
    time.sleep(2)
    # start date element
    startDay=driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[1]/div/table/tbody/tr[4]/td[2]/div[5]/div/div[1]/input')
    startDay.send_keys(day)
    time.sleep(8)
    # end date
    endDay=driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[1]/div/table/tbody/tr[4]/td[2]/div[7]/div/div[1]/input')
    endDay.send_keys(day)
    time.sleep(8)

# clear dates input
def clearDate():
    # start date
    startDay=driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[1]/div/table/tbody/tr[4]/td[2]/div[5]/div/div[1]/input')
    startDay.clear()
    time.sleep(5)
    # end date
    endDay=driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[1]/div/table/tbody/tr[4]/td[2]/div[7]/div/div[1]/input')
    endDay.clear()
    time.sleep(5)

# select all samples and click download
def selectSamples():
    time.sleep(3)
    # select all the samples 
    elements=driver.find_elements_by_class_name('yui-dt-checkbox')
    time.sleep(2)
    for i in elements:
        i.click()
    time.sleep(8)
    # download button
    driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[2]/div[2]/div[3]/button[4]').click()
    time.sleep(8)

# Downlaod
def download():
    time.sleep(2)
    # go to window
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    time.sleep(4)
    # select augur pipeline
    driver.find_element_by_xpath('/html/body/form/div[5]/div/div[1]/div/div/table[1]/tbody/tr/td[2]/div/div[1]/div[2]/div[2]/input').click()
    time.sleep(8)
    # click download
    driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div/div[2]/div/button').click()
    time.sleep(18)

# deselcet samples
def deselectSamples():
    time.sleep(2)
    # go back to normal page
    driver.switch_to.default_content()
    time.sleep(5)
    # select all the samples 
    driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/table/thead/tr/th[1]/div/span/input')\
        .click()
    time.sleep(8)
    # deselect all the samples
    driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/table/thead/tr/th[1]/div/span/input')\
        .click()
    time.sleep(8)

# jump to next page currently is not used:
def nextPage():
    driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/a[1]')\
        .click()
# got to next page
def selectPage(page):
    time.sleep(2)
    findPage=driver.find_element_by_xpath("//a[@title='Page %s']" % page)
    findPage.click()
    time.sleep(5)
    clearPopUp()
    time.sleep(2)
    #driver.switch_to.default_content()

# find the number of samples selected for download
def samplesNum():
    sampNumb=''
    for elem in driver.find_elements_by_xpath('/html/body/form/div[5]/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/span/span'):
        sampNumb+=elem.text
    return(sampNumb)

# remove string elements
def getSampNumb(sampNumb):
    part1=sampNumb.replace('Total: ', '')
    part2=part1.replace(' viruses', '')
    part3=part2.replace(',', '')
    return(part3)

# count number of pages to switch for 1 day
def getPagesNumber(intSamples):
    samples=intSamples
    pages=samples/50
    if pages.is_integer()==True:
        pagesNumb=pages+1
    else:
        pagesNumb=pages+2
    return int(pagesNumb)

def finalCall(day, page):
    time.sleep(5)
    selectSamples()
    # download
    tryDownload(day, page)
    # deselect samples
    tryDeselectSamples(day, page)

## set variables
login=getInfo(gisaidUser)
password=getInfo(gisaidPassword)
sampName='hCoV-19/USA/GA-EHC'
location='North America / USA / Georgia'

## Try wrapper functions
def trySelectSamples(day, page):
    try:
        selectSamples()
    except:
        time.sleep(5)
        try:
            selectSamples()
        except Exception as e:
            print(e) 
            with open("errorLog.txt", "a") as text_file:
                text_file.write("%s samples selection failed on page %s" % (day, page) + "\n")

def tryDownload(day, page):
    try:
        download()
    except:
        time.sleep(5)
        try:
            download()
        except Exception as e:
            print(e)
            with open("errorLog.txt", "a") as text_file:
                text_file.write('%s download failed on page %s' % (day, page) + '\n')
        else:
            # write downloaded date into log
            with open("completedLog.txt", "a") as text_file:
                text_file.write("%s Completed page %s" % (day, page) + "\n")
    else:
        # write downloaded date into log
        with open("completedLog.txt", "a") as text_file:
            text_file.write("%s Completed page %s" % (day, page) + "\n")

def tryDeselectSamples(day, page):
    try:
        deselectSamples()
    except:
        time.sleep(5)
        try:
            deselectSamples()
        except Exception as e:
            print(e)
            with open("errorLog.txt", "a") as text_file:
                text_file.write('%s samples deselection failed on page %s' % (day, page) + '\n')

## loop the functions
def runDays(firstDay, lastDay):
    date_rng = pd.date_range(firstDay, lastDay,freq='D')
    dates=pd.Series(date_rng.format()).tolist()
    logIn(login, password)
    epiSearch()
    # itterate through dates
    for day in dates:
        filterDate(day)
        sampNumb=samplesNum()
        intSamples=int(getSampNumb(sampNumb))
        if intSamples>0:
            pagesNumb= getPagesNumber(intSamples)
            for page in range(2,pagesNumb):
                # select samples
                time.sleep(5)
                selectSamples()
                # download
                tryDownload(day, page)
                # deselect samples
                tryDeselectSamples(day, page)
                # go to next page
                selectPage(page)
        else:
            print('No samples to download')
            with open("noSamplesLog.txt", "a") as text_file:
                text_file.write("%s No_samples" % day + "\n")
        # clear dates
        page=(pagesNumb-1)
        finalCall(day, page)
        clearDate()
    print('Program stopped')

# run the program
if __name__ == '__main__':
    runDays(firstDay='2020-03-24', lastDay='2020-03-24')