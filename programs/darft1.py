from os import path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

drPath='C:/Users/abomb/Projects/covDatDownloader/chromedriver.exe'
gisaidUser='../gisaidLogin.txt'
gisaidPassword='../gisadPassword.txt'
gisaidPath='https://www.epicov.org/epi3/frontend#45e4b1'
driver=webdriver.Chrome(drPath)
driver.get(gisaidPath)