from nturl2path import url2pathname
from os import path
from pydoc import pathdirs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import Chrome, ChromeOptions

drPath='C:/Users/abomb/Projects/covDatDownloader/chromedriver.exe'
gisaidUser='../gisaidLogin.txt'
gisaidPassword='../gisadPassword.txt'
gisaidPath='https://www.epicov.org/epi3/frontend#45e4b1'

def getUser(user):
    with open(user) as f:
        text = f.read()
    return text

def getPassword(password):
    with open(password) as f:
        text=f.read()
    return(text)

driver=webdriver.Chrome(drPath)
page=driver.get(gisaidPath)



