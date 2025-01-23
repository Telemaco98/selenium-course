from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

browser = Firefox()
url = "https://curso-python-selenium.netlify.app/keyboard"
browser.get(url)

html = browser.find_element(By.TAG_NAME, 'html')

html.send_keys('selenium')
