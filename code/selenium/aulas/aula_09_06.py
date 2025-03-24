from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class EsperarElementoAtivo:
	def __init__(self, locator):
		self.locator = locator

	def __call__(self, web_driver):
		elementos = web_driver.find_elements(*self.locator)
		if elementos:
			return not('unclick' in elementos[0].get_attribute('class'))
		return False

def esperar_elemento(locator, webdriver):
	if webdriver.find_elements(*locator):
		return True
	return False

url = "https://curso-python-selenium.netlify.app/aula_09.html"

browser = Firefox()
wdw = WebDriverWait(browser, 10)
browser.get(url)

botao_locator = (By.CSS_SELECTOR , 'button')
sucesso_locator = (By.ID, 'finished')

wdw.until( 
	EsperarElementoAtivo(botao_locator),	
	"Não consegui acha o botão :/"
)

button = browser.find_element(*botao_locator)
button.click()

wdw.until(
	partial(esperar_elemento, sucesso_locator),
	"A mensagem de sucesso não apareceu"
)

sucesso = browser.find_element(*sucesso_locator)
assert sucesso.text == 'Carregamento concluído'