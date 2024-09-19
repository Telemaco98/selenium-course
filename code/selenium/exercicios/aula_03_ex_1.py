"""
    Crie um programa com selenium que gere um dicionario onde a chave é a tag h1
     - O valor deve ser um novo dicionario
     - cada chave do valor deverá ser o valor de 'atributo'
     - cada valor deve ser o texto contido no elemento
    https://curso-python-selenium.netlify.app/exercicio_01.html
"""

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

url = "https://curso-python-selenium.netlify.app/exercicio_01.html"

browser = Firefox()
browser.get(url)

browser.implicitly_wait(1)

h1 = browser.find_element(By.TAG_NAME, "h1")

print(h1.text)

ps = browser.find_elements(By.TAG_NAME, "p")

dict_result = {}
dict_result["h1"] = {}

for p in ps:
    value = p.get_attribute("atributo")
    dict_result["h1"][value] = p.text

print(dict_result)

browser.quit()
