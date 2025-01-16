"""
    Refazer exercicio_03 usando o EventListenner para printar o after da
    navegação e de clicks. Ou seja, me diga aonde você está clicando e quando
    você vai para proxima aba eu quero saber em qual aba você está.
    https://curso-python-selenium.netlify.app/exercicio_03.html
"""

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
import time

url = "https://curso-python-selenium.netlify.app/exercicio_03.html"

browser = Firefox()
browser.implicitly_wait(1)
browser.get(url)

# TODO

browser.quit()
