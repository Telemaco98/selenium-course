from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By


browser = Firefox()
url = "https://curso-python-selenium.netlify.app/aula_04_a.html"
browser.get(url)

browser.implicitly_wait(1)

unorder_list = browser.find_element(By.TAG_NAME, "ul")
lis = unorder_list.find_elements(By.TAG_NAME, "li")
a = lis[0].find_element(By.TAG_NAME, "a").text

print(a)

browser.quit()
