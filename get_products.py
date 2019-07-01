# adapted from: https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/packages/beautifulsoup.md
# code by @s2t2

import requests
from bs4 import BeautifulSoup

request_url = "https://www.amazon.com/s?k=gooseneck+kettle"
print("GETTING PAGE CONTENTS FROM:", request_url)

response = requests.get(request_url)
print(type(response))
print(response.status_code)
print(type(response.text))

soup = BeautifulSoup(response.text, features="html.parser") # add features param to avoid warning message
print(type(soup))

breakpoint()

results_list = soup.find("div", "s-search-results") # this works


# running into "Robot Check"
#>
#> Robot Check\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
#> Enter the characters you see below\n
#> Sorry, we just need to make sure you\'re not a robot.
#> For best results, please make sure your browser is accepting cookies.\n\n\n\n\n\n\n\n\n\n\n
#> Type the characters you see in this image:\n\n\n\n\n\n\n\n\n
#> Try different image\n\n\n\n\n\n\n\n\n\n\n\n
#> Continue shopping\n\n\n\n\n\n\n\n\n\n\n\n
