"""
    Seguir as cordenadas que página diz
    https://curso-python-selenium.netlify.app/exercicio_06.html
"""

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
import time

url = "https://curso-python-selenium.netlify.app/exercicio_06.html"

browser = Firefox()
browser.implicitly_wait(1)
browser.get(url)

def find_n_times_to_fill(browser):
    """ Get the number to fill the forms

    Parameters:
    browser (WebDriver): The browser webdriver

    Returns:
    Int: The number of time to fll the forms
    """
    p1 = browser.find_element(By.CSS_SELECTOR, 'header > p:first-child').text

    for char in p1.split():
        if char.isdigit():
            return int(char)

def find_instruction(browser):
    """ Get form class name to be fill by Instruction

    Parameters:
    browser (WebDriver): The browser webdriver

    Returns:
    String: Form class name to be fill
    """
    form_to_fill = browser.find_element(By.CSS_SELECTOR, 'header > p:nth-of-type(2) > span').text
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


n = find_n_times_to_fill(browser)

for x in range(-1, n):
    time.sleep(2)

    instruction = find_instruction(browser)
    fill_form(browser, instruction)

browser.quit()
