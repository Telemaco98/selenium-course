"""
Objetivos:

"""
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import (
    AbstractEventListener,
    EventFiringWebDriver
)

class MyListener(AbstractEventListener):
    def after_navigate_to(self, url, webdriver):
        print(f'Estou na URL: {url}')

    def after_navigate_back(self, webdriver):
        print('voltando para página anterior')

    def before_click(self, element, webdriver):
        if element.tag_name == 'input':
            print(webdriver.find_element(By.TAG_NAME, 'span').text)
        print(f'antes do click no {element.tag_name}')

    def after_click(self, element, webdriver):
        if element.tag_name == 'input':
            print(webdriver.find_element(By.TAG_NAME, 'span').text)
        print(f'depois do click no {element.tag_name}')

browser = Firefox()

rapi_browser = EventFiringWebDriver(browser, MyListener())

url = "https://curso-python-selenium.netlify.app/aula_07_d.html"

rapi_browser.implicitly_wait(2)
rapi_browser.get(url)

input_text = rapi_browser.find_element(By.TAG_NAME, 'input')
span = rapi_browser.find_element(By.TAG_NAME, 'span')
p_counter = rapi_browser.find_element(By.TAG_NAME, 'p')

input_text.click()
span.click()

aula_c = "https://curso-python-selenium.netlify.app/aula_07_c.html"
rapi_browser.get(aula_c)

rapi_browser.back()

browser.quit()
