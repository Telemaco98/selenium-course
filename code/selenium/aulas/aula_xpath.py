from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
import time
import requests
from parsel import Selector

url = "https://rennerocha.github.io/xpath/"
browser = Firefox()
browser.get(url)
time.sleep(2)

# Gets the recipe title
title = browser.find_element(By.XPATH, "//h1")
print(title.text+"\n\n")

# Gets all 'li' inside all 'ol's
all_lis = browser.find_elements(By.XPATH, "//ol/li")
for li in all_lis:
    print(li.text)

# Gets the second 'li' inside the first 'ol'
_2nd_li = browser.find_element(By.XPATH, "//ol[1]/li[2]") # outra maneira de escrever esse path seria "(//ol/li)[2]"
print('\n\n'+_2nd_li.text)

browser.quit()


# Using selector to extract elements xpath
html = requests.get(url).text
selector = Selector(html)

# Todos os H1's
print(selector.xpath('//h1').getall())
print("\n")

# Todos os títulos de H1's
print(selector.xpath('//h1/text()').getall())
print("\n")

# Todos os valores dos elementos H1 que contenham o atributo "data-section"
print(selector.xpath('//h1/@data-section').getall())
print("\n")

# Todos os elementos H1 que contenham o atributo "data-section"
print(selector.xpath('//h1[@data-section]').getall())
