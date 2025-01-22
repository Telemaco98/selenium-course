"""
    Refazer exercicio_03 usando o EventListenner para printar o after da
    navegação e de clicks. Ou seja, me diga aonde você está clicando e quando
    você vai para proxima aba eu quero saber em qual aba você está.
    https://curso-python-selenium.netlify.app/exercicio_03.html
"""

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.events import (
    AbstractEventListener,
    EventFiringWebDriver
)
from urllib.parse import urlparse
import time

class Listener(AbstractEventListener):
    def after_navigate_to(self, url, webdriver):
        print(f'the url had changed: {url}')

    def before_click(self, element, webdriver):
        print(f'cliquei no "{element.text}"')

def answer_click(browser, answer_should_be):
    _as = browser_wrapper.find_elements(By.CSS_SELECTOR, 'main a')
    path = urlparse(browser.current_url).path

    for a in _as:
        if a.get_attribute("attr") == answer_should_be:
            return a
        elif a.get_attribute("attr") == "" and a.text == path[1:]:
            return a

url = "https://curso-python-selenium.netlify.app/exercicio_03.html"

browser = Firefox()
browser_wrapper = EventFiringWebDriver(browser, Listener())
browser_wrapper.implicitly_wait(2)
browser_wrapper.get(url)

start = browser_wrapper.find_element(By.CSS_SELECTOR, 'main a')
start.click()

win = False

while not win:
    try:
        command = browser_wrapper.find_element(By.CSS_SELECTOR, 'main > p')
        if "certo" in command.text:
            answer_click(browser_wrapper, "certo").click()
        elif "contrário" in command.text:
            answer_click(browser_wrapper, "errado").click()
        elif "refresh" in command.text:
            browser_wrapper.refresh()
    except NoSuchElementException as e:
        print("the end")
        win = True
    except StaleElementReferenceException as e:
        print("Catched StaleElementReferenceException")


browser.quit()
