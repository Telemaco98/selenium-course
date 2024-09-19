from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By


url = "https://curso-python-selenium.netlify.app/aula_05_c.html"
browser = Firefox()
browser.get(url)

def fill_melhor_filme (filme, email, telef):
    """ Preemche com formulario do melhor filme """
    browser.find_element(By.NAME, "filme").send_keys(filme)
    browser.find_element(By.NAME, "email").send_keys(email)
    browser.find_element(By.NAME, "telefone").send_keys(telef)
    browser.find_element(By.NAME, "enviar").click()

fill_melhor_filme("gravidade", "shi@du.edu", "(081)312345678")


browser.quit()
