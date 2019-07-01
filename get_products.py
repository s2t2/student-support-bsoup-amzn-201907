# adapted from: https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/packages/beautifulsoup.md
# code by @s2t2

import requests
from bs4 import BeautifulSoup

request_url = "______________"
print("GETTING PAGE CONTENTS FROM:", request_url)

response = requests.get(request_url)
print(type(response))
print(response.status_code)
print(type(response.text))

soup = BeautifulSoup(response.text, features="html.parser") # add features param to avoid warning message
print(type(soup))

breakpoint()

#my_table = soup.find("table", id="_________")
