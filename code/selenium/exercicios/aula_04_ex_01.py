"""
    Crie um programa com selenium que
        - ache o unicornio
    https://curso-python-selenium.netlify.app/exercicio_03.html
"""

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
from selenium.common.exceptions import NoSuchElementException

url = "https://curso-python-selenium.netlify.app/exercicio_03.html"
browser = Firefox()
browser.get(url)
browser.implicitly_wait(1)

"""
    Parte 1 - clicar em comentar
"""
main = browser.find_element(By.TAG_NAME, "main")
a = main.find_element(By.TAG_NAME, "a")
a. click()

"""
    Parte 2 - entender o comando do jogo: se é pra responder "certo" ou "contrário"
"""

def answer_click(browser, web_elem, answer_should_be):
    _as = web_elem.find_elements(By.TAG_NAME, "a")
    path = urlparse(browser.current_url).path

    for a in _as:
        if a.get_attribute("attr") == answer_should_be:
            return a
        elif a.get_attribute("attr") == "" and a.text == path[1:]:
            return a

ganhou = False

while not ganhou:
    main = browser.find_element(By.TAG_NAME, "main")

    try:
        command = main.find_element(By.TAG_NAME, "p")

        if "certo" in command.text:
            answer_click(browser, main, "certo").click()
        elif "contrário" in command.text:
            answer_click(browser, main, "errado").click()
        elif "refresh" in command.text:
            browser.refresh()
    except NoSuchElementException as e:
        print("the end")
        ganhou = True
