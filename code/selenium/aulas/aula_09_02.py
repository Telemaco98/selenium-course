"""
Precisamos: 
	1. Carregar a página
	2. Esperar o botão
	3. Clicar no botão

"""

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def esperar_botao(webdriver):
	elements = webdriver.find_elements(By.CSS_SELECTOR, 'button')
	print('tentando achar o botão')
	return bool(elements)

def esperar_sucesso(webdriver):
	elements = webdriver.find_elements(By.CSS_SELECTOR, '#finished')
	print('esperando conclusão')
	return bool(elements)

url = "https://curso-python-selenium.netlify.app/aula_09_a.html"

browser = Firefox()
wdw = WebDriverWait(browser, 10)
browser.get(url)

wdw.until(esperar_botao, "Não consegui acha o botão :/")

button = browser.find_element(By.CSS_SELECTOR, 'button')
button.click()

wdw.until(esperar_sucesso, "A mensagem de sucesso não apareceu")
sucesso = browser.find_element(By.ID, 'finished')

assert sucesso.text == 'Carregamento concluído'