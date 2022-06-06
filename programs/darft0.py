from os import path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

drPath='C:/Users/abomb/Projects/covDatDownloader/chromedriver.exe'

driver=webdriver.Chrome(drPath)

driver.get('https://www.epicov.org/epi3/frontend#45e4b1')

print(driver.title)

