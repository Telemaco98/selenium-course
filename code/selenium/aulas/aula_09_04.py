"""
Utilizando parse com By
"""
from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def esperar_elemento(by, elemento, webdriver):
	print(f'tentando achar o "{elemento}"')
	if webdriver.find_elements(by, elemento):
		return True
	return False

url = "https://curso-python-selenium.netlify.app/aula_09_a.html"

browser = Firefox()
wdw = WebDriverWait(browser, 10)
browser.get(url)

wdw.until(
	partial(esperar_elemento, By.CSS_SELECTOR , 'button'),
	"Não consegui acha o botão :/"
)

button = browser.find_element(By.CSS_SELECTOR, 'button')
button.click()

wdw.until(
	partial(esperar_elemento, By.ID, 'finished'), 
	"A mensagem de sucesso não apareceu"
)

sucesso = browser.find_element(By.ID, 'finished')
assert sucesso.text == 'Carregamento concluído'