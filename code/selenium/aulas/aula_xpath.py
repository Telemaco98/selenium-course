from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
import time

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
_2nd_li = browser.find_element(By.XPATH, "//ol[1]/li[2]")
print('\n\n'+_2nd_li.text)

browser.quit()
