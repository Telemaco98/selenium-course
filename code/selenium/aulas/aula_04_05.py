"""
    Aula sobre location

    Objetivos:
    1. Pegar todos os links de aulas
        {'nome da aula': 'link da aula'}
    2. Navegar até o exercicio 3
        achar a url do exercicio 3 e ir até lá
"""
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from pprint import pprint # preatty print

url = "https://curso-python-selenium.netlify.app/aula_04.html"
browser = Firefox()
browser.implicitly_wait(1)
browser.get(url)


def get_links(browser, element):
    """
        pega todos os links dentro de um elemento

        - browser = a instancia do navegador
        - element = webelement [aside, main, body, ul, ol]
    """

    el = browser.find_element(By.TAG_NAME, element)
    el_anchors = el.find_elements(By.TAG_NAME, "a")

    result = {}

    for anchor in el_anchors:
        result[anchor.text] = anchor.get_attribute("href")

    return result


"""
    PARTE 1
"""

aulas = get_links(browser, "aside")
pprint(aulas)

"""
    PARTE 2
"""

exercicios = get_links(browser, "main")
pprint(exercicios)
browser.get(exercicios['Exercício 3'])
