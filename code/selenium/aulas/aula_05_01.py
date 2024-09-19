from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By


url = "https://curso-python-selenium.netlify.app/aula_05_a.html"
browser = Firefox()
browser.get(url)

haskell = browser.find_element(By.ID, "haskell")
print(haskell.text)

browser.quit()
