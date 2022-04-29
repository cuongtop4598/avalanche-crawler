from audioop import add
from curses import meta
from lib2to3.pgen2.token import OP
from typing_extensions import assert_type
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import json

chrome_options = Options()
#chrome_options.add_argument('--headless')
driver = webdriver.Chrome('/home/cuongtop/Desktop/Avalanche-crawler/chromedriver', options=chrome_options)
driver.get("https://avascan.info/blockchain/c/tokens")

tokens = []
for i in range(1,50):
    print(i)
    name  = driver.find_element_by_xpath(f'/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[{i}]/td[5]/div[1]').text
    address = driver.find_element_by_xpath(f"/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[{i}]/td[6]/a[1]/span[1]").text
    try:
        img_icon = driver.find_element_by_xpath(f"/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[{i}]/td[3]/img[1]")
    except:
        continue
    # with open(f'./assets/images/{address}.png','wb') as file:
    #     file.write(img_icon.screenshot_as_png)
    metadata  = {
        'id': i,
        'name': name,
        'icon_url': img_icon.get_attribute('src'),
        'address': address
    }
    tokens.append(metadata)
with open('tokens-list.json','w') as tokens_file:
    tokens_file.write(json.dumps(tokens))  
