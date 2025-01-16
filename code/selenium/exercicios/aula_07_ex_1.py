"""
    Brincar com os eventos enquanto preenche o formulário
    https://curso-python-selenium.netlify.app/exercicio_07.html
"""

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
import time

url = "https://curso-python-selenium.netlify.app/exercicio_07.html"

browser = Firefox()
browser.get(url)

# TODO

browser.quit()
