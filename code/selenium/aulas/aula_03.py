from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

url = "https://curso-python-selenium.netlify.app/aula_03.html"
browser = Firefox ()

browser.get(url)

browser.implicitly_wait(2)

a = browser.find_element(By.TAG_NAME, 'a')
p = browser.find_element(By.TAG_NAME, 'p')

for click in range(10):
    ps = browser.find_elements(By.TAG_NAME, 'p')
    a.click()
    print(f"Valor do ultimo p: {ps[-1].text} valor do click: {click}")
    print(f"Os valores são iguais? {ps[-1].text == str(click)} \n")

browser.quit()
