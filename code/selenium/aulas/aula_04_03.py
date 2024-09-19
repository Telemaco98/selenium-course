"""
    Aula sobre histórico de navegação
"""

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

def find_by_text(browser, tag, text):
    """Encontrar o elemento com o texto 'text'

    Argumentos:
        - browser = Instancia do browser [firefox, chrome ...]
        - texto = conteúdo que deve estar na tag
        - tag = nome da tag onde o texto será procurado
    """
    tag_list = browser.find_elements(By.TAG_NAME, tag) #lista
    for t in tag_list:
        if t.text == text:
            return t

url = "https://curso-python-selenium.netlify.app/aula_04_b.html"
browser = Firefox()
browser.implicitly_wait(1)
browser.get(url)


box_name = ['um', "dois", "tres", "quatro"]

for texto in box_name:
    find_by_text(browser, "div", texto).click()

for texto in box_name:
    sleep(1)
    browser.back()

for texto in box_name:
    sleep(1)
    browser.forward()
