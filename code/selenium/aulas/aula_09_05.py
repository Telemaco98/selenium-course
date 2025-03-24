"""
Utilizando OO e Locators
"""
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class EsperarElemento:
	def __init__(self, locator):
		self.locator = locator

	def __call__(self, web_driver):
		if web_driver.find_elements(*self.locator):
			return True
		return False


url = "https://curso-python-selenium.netlify.app/aula_09_a.html"

browser = Firefox()
wdw = WebDriverWait(browser, 10)
browser.get(url)

botao_locator = (By.CSS_SELECTOR , 'button')
sucesso_locator = (By.ID, 'finished')

wdw.until( 
	EsperarElemento(botao_locator),	
	"Não consegui acha o botão :/"
)

button = browser.find_element(*botao_locator)
button.click()

wdw.until(
	EsperarElemento(sucesso_locator),
	"A mensagem de sucesso não apareceu"
)

sucesso = browser.find_element(*sucesso_locator)
assert sucesso.text == 'Carregamento concluído'