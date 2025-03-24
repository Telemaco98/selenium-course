"""
Precisamos: 
	1. Carregar a página
	2. Esperar o botão
	3. Clicar no botão

"""
from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def esperar_elemento(elemento, webdriver):
	print(f'tentando achar o "{elemento}"')
	if webdriver.find_elements(By.CSS_SELECTOR, elemento):
		return True
	return False


esperar_botao = partial(esperar_elemento, 'button')
esperar_sucesso = partial(esperar_elemento, '#finished')

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