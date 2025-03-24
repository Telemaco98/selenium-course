from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

url = "https://curso-python-selenium.netlify.app/aula_09_a.html"

browser = Firefox()
browser.get(url)
browser.implicitly_wait(30)

button = browser.find_element(By.CSS_SELECTOR, 'button')

button.click()

success = browser.find_element(By.ID, 'finished')
assert success.text == "Carregamento concluído"