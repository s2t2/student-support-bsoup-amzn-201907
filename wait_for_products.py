# adapted from:
#   + https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/packages/beautifulsoup.md
#   + https://github.com/s2t2/student-support-apt-scraper-py/blob/master/browsing5.py
#   + https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/packages/selenium.md
#   + https://github.com/s2t2/student-support-bsoup-mlb-201906
# code by @s2t2

from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
