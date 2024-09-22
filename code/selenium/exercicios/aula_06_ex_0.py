"""
    Brincar com essa página
    https://curso-python-selenium.netlify.app/aula_06.html
"""

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

browser = Firefox()

url = 'https://curso-python-selenium.netlify.app/aula_06.html'

browser.implicitly_wait(2)
browser.get(url)

# Fills nome 3rd form
third_form = browser.find_element(By.CSS_SELECTOR, 'form:nth-of-type(3)')
third_form.find_element(By.CSS_SELECTOR, 'input[name]').send_keys("teste1")
third_form.find_element(By.CSS_SELECTOR, 'form:nth-of-type(3) input[name="senha"]').send_keys("teste1")

# Clicar em todos o forms que contenham 'l1'
l1_forms = browser.find_elements(By.CSS_SELECTOR, '[class*="l1"]')
for l1 in l1_forms:
    assert "l1" in l1.get_attribute('class')

# Pegar todos os form irmãos adjacentes do 'l0c1'
#   RE: l1c0 & l1c1
l0c1_irmaos_adj = browser.find_elements(By.CSS_SELECTOR, '.form-l0c1 ~ form')
test3_set = {'form-l1c0', 'form-l1c1'}
for ele in l0c1_irmaos_adj:
    assert ele.get_attribute('class') in test3_set
