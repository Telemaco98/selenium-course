from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By


url = "https://curso-python-selenium.netlify.app/aula_06_a.html"
browser = Firefox()
browser.implicitly_wait(2)
browser.get(url)

browser.find_element(By.CSS_SELECTOR, 'input').send_keys('Ohara')
