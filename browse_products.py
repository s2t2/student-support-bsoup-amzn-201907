# adapted from:
#   + https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/packages/beautifulsoup.md
#   + https://github.com/s2t2/student-support-apt-scraper-py/blob/master/browsing5.py
#   + https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/packages/selenium.md
#   + https://github.com/s2t2/student-support-bsoup-mlb-201906
# code by @s2t2

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

driver = webdriver.Chrome("/usr/local/bin/chromedriver") # location where chromedriver is installed
print(type(driver))

request_url = "https://www.amazon.com/s?k=gooseneck+kettle"
print("VISITING:", request_url)

driver.get(request_url)
print(driver.title)

try:

    print("PARSING CONTENTS...")
    soup = BeautifulSoup(driver.page_source, "html.parser") # add features param to avoid warning message
    print(type(soup))

    results_list = soup.find("div", "s-search-results") # this works

    items = results_list.findAll("div", "s-result-item") #> <class 'bs4.element.ResultSet'>

    print(f"FOUND {len(items)} ITEMS...") #> 48, confirms visual scan of the page

    for item in items:
        print(type(item))
        #print(item.text) #>"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nSponsored\n\n\n\n\nThese are ads for products you'll find on Amazon.com. Clicking an ad will take you to the product's page.\n\nLearn more about Sponsored Products.\n\n\n\n\n\n\n\n\n\n\n\n\nHamilton Beach Electric Kettle, Tea and Hot Water Heater, Variable Temperature, Cordless Serving, Keep Warm, Soft Blue LED (41020), 1.7 Liter, Stainless Steel\n\n\n\n\n\n\n\n4.1 out of 5 stars\n\n\n\n\n241\n\n\n\n\n\n\n\n\n\n\nLimited time deal\n\n\n\n\n$42.49$42.49\n$49.99$49.99\n\n\n\n\n\n\n\n\n\n\n\n\n\nGet it as soon as Wed, Jul 3\n\n\n\nFREE Shipping by Amazon\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
        #print(item.text.strip()) #>
        #print("-------------")

except TimeoutException:
    print("TIME OUT!")
finally:
    driver.quit() # always close the web browser to prevent memory issues
