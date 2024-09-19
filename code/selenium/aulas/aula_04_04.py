"""
    Aula sobre location
"""
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from urllib.parse import urlparse



url = "https://curso-python-selenium.netlify.app/aula_04_a.html"
browser = Firefox()
browser.implicitly_wait(1)
browser.get(url)

url_parseada = urlparse(browser.current_url)
