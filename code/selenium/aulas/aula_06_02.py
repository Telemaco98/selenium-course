"""
 Aula 06_a
    Vimos operadores para valores de atributo
        =   Deve ser exatamente igual
        *=  Deve ocorrer em
        |=  Deve ser exatamente ou iniciar
        ^=  Iniciado em
        $=  Terminado em
        ~=  Um deve ser exatamente igual
"""


from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

url = "https://curso-python-selenium.netlify.app/aula_06_a.html"
browser = Firefox()
browser.implicitly_wait(2)
browser.get(url)

# usando o attributo type [attr="valor"]
# nome = browser.find_element(By.CSS_SELECTOR, '[type="text"]')
# password = browser.find_element(By.CSS_SELECTOR, '[type="password"]')
# btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')

# usando o atributo name [attr="valor"]
# nome = browser.find_element(By.CSS_SELECTOR, '[name="nome"]')
# password = browser.find_element(By.CSS_SELECTOR, '[name="senha"]')
# btn = browser.find_element(By.CSS_SELECTOR, '[name="l0c0"]')

# elemento que o [att] contenha "value" [att*="value"]
# *= deve ocorrer em
# nome = browser.find_element(By.CSS_SELECTOR, '[name*="ome"]')
# password = browser.find_element(By.CSS_SELECTOR, '[name*="nha"]')
# btn = browser.find_element(By.CSS_SELECTOR, '[name*="l0"]')

# elemento que o [att] que comece com "value" (ou é exatamente) [att|="value"]
# |= deve ser exatamente ou iniciar
# nome = browser.find_element(By.CSS_SELECTOR, '[name|="nome"]')
# password = browser.find_element(By.CSS_SELECTOR, '[name|="senha"]')
# btn = browser.find_element(By.CSS_SELECTOR, '[name|="l0c0"]')

# elemento que o [att] que comece com "value" [att^="value"]
# ^= incia com
nome = browser.find_element(By.CSS_SELECTOR, '[name^="n"]')
password = browser.find_element(By.CSS_SELECTOR, '[name^="s"]')
btn = browser.find_element(By.CSS_SELECTOR, '[name^="l0"]')

nome.send_keys('Oharinha')
password.send_keys('Batatinha123')
# btn.click()
