"""
	Encontrar o momento exato em que a classe 'selenium' apareça no botão

	Tasks:
		1. Esperar o carregamento do botão
		2. Esperar até que a classe 'selenium' apareça no botão
		3. Tentar clicar e ver o que acontece
"""

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

class ElementWaiter:
	def __init__(self, locator):
		self.locator = locator

	def __call__(self, webdriver):
		elements = webdriver.find_elements(*self.locator)
		if elements:
			return True
		return False

class SeleniumWaiter:
	def __init__(self, locator):
		self.locator = locator

	def __call__(self, webdriver):
		elements = webdriver.find_elements(*self.locator)
		if 'selenium' in elements[0].get_attribute('class'):
			print('Time to click')
			return True
		return False


url = "https://curso-python-selenium.netlify.app/exercicio_09"

browser = Firefox()
browser.get(url)

waiter = WebDriverWait(browser, 20) 	# Receive the webdriver and the timetout 

btn_locator = (By.ID, 'request')

waiter.until(
	ElementWaiter(btn_locator),
	'Something wrong, unable to load the button'
)

waiter.until(
	SeleniumWaiter(btn_locator),
	'The class `selenium` could not be found'
)

try:
	browser.find_element(*btn_locator).click()
	print("\n\t!!! Clicked !!!")
except StaleElementReferenceException:
	print('The button is not able to click anymore')
except TimeoutException as e:
	print(str(e))
