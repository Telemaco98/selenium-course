from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By


url = "https://curso-python-selenium.netlify.app/aula_05_b.html"
browser = Firefox()
browser.get(url)

topico = browser.find_element(By.CLASS_NAME, "topico")
print(topico.text)

linguagens = browser.find_elements(By.CLASS_NAME, "linguagens")

for l in linguagens:
    h2 = l.find_element(By.TAG_NAME, "h2").text
    p = l.find_element(By.TAG_NAME, "p").text
    print(h2, p)

browser.quit()
