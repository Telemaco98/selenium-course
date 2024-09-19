"""
    Fazer o match do resutlado com a query
    https://curso-python-selenium.netlify.app/exercicio_04.html
"""
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
from json import loads

url = "https://curso-python-selenium.netlify.app/exercicio_04.html"
browser = Firefox()
browser.implicitly_wait(2)
browser.get(url)

# nome, email, senha, telefone, btn

def fill_form(browser, nome, email, senha, telefone):
    browser.find_element(By.NAME, 'nome').send_keys(nome)
    browser.find_element(By.NAME, 'email').send_keys(email)
    browser.find_element(By.NAME, 'senha').send_keys(senha)
    browser.find_element(By.NAME, 'telefone').send_keys(telefone)
    browser.find_element(By.NAME, 'btn').click()


dados = {
    "nome": "Shirley",
    "email": "shirloca@gmail.com",
    "senha": "12345678",
    "telefone": "(21)9825874114"
}

fill_form(browser, **dados)

url = urlparse(browser.current_url)
query = url.query


text_result = browser.find_element(By.ID, "result").text
text_result = text_result.replace('\'', '\"')
dict_result = loads(text_result)

assert dict_result == dados

# TODO: Fazer o match do resutlado com a query
