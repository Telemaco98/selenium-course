"""
    Crie um programa com selenium que
        - jogue o jogo
        - Quando você ganhar o script deve parar de ser executado
    https://curso-python-selenium.netlify.app/exercicio_02.html
"""

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

url = "https://curso-python-selenium.netlify.app/exercicio_02.html"
browser = Firefox()

browser.get(url)
browser.implicitly_wait(1)

ps = browser.find_elements(By.TAG_NAME, "p")
stop_value = ps[1].text
print(f"É pra parar no valor: {stop_value}")

last_value = ""
play = browser.find_element(By.ID, "ancora")

while "Você ganhou:" not in last_value:
    play.click()
    ps = browser.find_elements(By.TAG_NAME, "p")
    last_value = ps[-1].text

    print(f"Ultimo resultado: {last_value}")
    pass

browser.quit()
