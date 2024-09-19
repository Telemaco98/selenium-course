from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

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

def find_by_href(browser, link):
    """Encontrar o elemento "a" com o link "link"

    Argumentos:
        - browser = Instancia do browser [firefox, chrome ...]
        - link = link que será procurado em todas as tags "a"
    """
    elements = browser.find_elements(By.TAG_NAME, "a")
    for e in elements:
        if link in e.get_attribute("href"):
            return e



browser = Firefox()
url = "https://curso-python-selenium.netlify.app/aula_04_a.html"
browser.get(url)

browser.implicitly_wait(1)

element_ddg = find_by_text(browser, "a", "DuckDuckGo")

element_ddg = find_by_href(browser, "ddg")
