"""
    Brincar com os eventos enquanto preenche o formulário
    https://curso-python-selenium.netlify.app/exercicio_07.html
"""

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import (
    AbstractEventListener,
    EventFiringWebDriver
)
import time

class Listener(AbstractEventListener):
    def before_click(self, element, webdriver):
        if element.get_attribute('id') == "nome":
            lnome = webdriver.find_element(By.ID, "lnome")
            print(f'Antes de clicar no input de `nome`, a sua label é: "{lnome.text}"')
        if element.get_attribute('id') == "email":
            lemail = webdriver.find_element(By.ID, "lemail")
            print(f'Antes de clicar no input de `email`, a sua label é: "{lemail.text}"')
        if element.get_attribute('id') == "senha":
            lsenha = webdriver.find_element(By.ID, "lsenha")
            print(f'Antes de clicar no input de `senha`, a sua label é: "{lsenha.text}"')

    def after_click(self, element, webdriver):
        if element.get_attribute('id') == "nome":
            lnome = webdriver.find_element(By.ID, "lnome")
            print(f'Depois de clicar no input de `nome`, a sua label é: "{lnome.text}"')
        if element.get_attribute('id') == "email":
            lemail = webdriver.find_element(By.ID, "lemail")
            print(f'Depois de clicar no input de `email`, a sua label é: "{lemail.text}"')
        if element.get_attribute('id') == "senha":
            lsenha = webdriver.find_element(By.ID, "lsenha")
            print(f'Depois de clicar no input de `senha`, a sua label é: "{lsenha.text}"')

    def after_change_value_of(self, element, driver):
        print(f'O input {element.get_attribute("id")} mudou para: "{element.get_attribute('value')}" \n')


url = "https://curso-python-selenium.netlify.app/exercicio_07.html"

browser = Firefox()
browser_wrapper = EventFiringWebDriver(browser, Listener())
browser_wrapper.implicitly_wait(2)
browser_wrapper.get(url)

name_input = browser_wrapper.find_element(By.ID, "nome")
email_input = browser_wrapper.find_element(By.ID, "email")
senha_input = browser_wrapper.find_element(By.ID, "senha")

enviar_btn = browser_wrapper.find_element(By.ID, "btn")

name_input.click()
name_input.send_keys("Epaminondas Telemaco")

email_input.click()
email_input.send_keys("epaminondas@gmail.com")

senha_input.click()
senha_input.send_keys("S3nh4!")

enviar_btn.submit()

time.sleep(2)

result = browser_wrapper.find_element(By.ID, 'result')
print(result.text)


browser.quit()
