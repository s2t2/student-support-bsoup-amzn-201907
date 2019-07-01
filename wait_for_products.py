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
#from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

request_url = "__________"
print(f"GETTING PAGE CONTENTS FROM {request_url}")

driver = webdriver.Chrome("/usr/local/bin/chromedriver") # location where chromedriver is installed
print(type(driver))

driver.get(request_url)
print(driver.title)

try:

    print("PARSING HTML TABLE...")
    soup = BeautifulSoup(driver.page_source, "html.parser") # add features param to avoid warning message
    print(type(soup))

    #breakpoint()

    print("2019 STATS:")

    #my_table = soup.find("table", id="______")


except TimeoutException:
    print("TIME OUT!")
finally:
    driver.quit() # always close the web browser to prevent memory issues
