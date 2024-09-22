"""
    Seguir as cordenadas que página diz
    https://curso-python-selenium.netlify.app/exercicio_05.html
"""

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
import time

url = "https://curso-python-selenium.netlify.app/exercicio_05.html"

browser = Firefox()
browser.get(url)

def find_instruction(browser):
    """ Get form class name to be fill by Instruction

    Parameters:
    browser (WebDriver): The browser webdriver

    Returns:
    String: Form class name to be fill
    """
    form_to_fill = browser.find_element(By.CSS_SELECTOR, 'header span').text
    return '.form-' + form_to_fill

def fill_form(browser, form_class_name):
    """Fill selected form

    Parameters:
    browser (WebDriver): The browser webdriver
    form_class_name (String): The form class name to be filled
    """
    form = browser.find_element(By.CSS_SELECTOR, form_class_name)
    form.find_element(By.NAME, 'nome').send_keys('name')
    form.find_element(By.NAME, 'senha').send_keys('senha')
    form.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

while True:
    time.sleep(2)
    instruction = find_instruction(browser)

    if  'conseguiu' in instruction:
        break
    fill_form(browser, instruction)
