"""
Objetivos:

1. Checar se a mudança ocorre no span (focus, blur)
2. Checar se a mudança ocorre no p (change)
"""
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

browser = Firefox()
url = "https://curso-python-selenium.netlify.app/aula_07_d.html"

browser.implicitly_wait(2)
browser.get(url)

input_text = browser.find_element(By.TAG_NAME, 'input')
span = browser.find_element(By.TAG_NAME, 'span')
p_counter = browser.find_element(By.TAG_NAME, 'p')

"""
    Cenário 1. Checar se a mudança ocorre no span (focus, blur)

 Quando clicar no elemento `input`
 Então o texto `está com foco` deve ser o content de `span`

 Quando clicar no elemento `span`
 Então o texto `está sem foco` deve ser o content de `span`
"""
input_text.click()
assert 'está com foco' == span.text

span.click()
assert 'está sem foco' == span.text

"""
    Cenário 2. Checar se a mudança ocorre no p (change)

Como acionar o change? Quando eu clico no input insiro algum texto e então
eu clico em outro elemento (tiro ele de foco)

Quando escrever o texto `test text` no input
E então clicar no elemento, ex.: `span`
Então o texto `1` deve ser o content de `p`
"""
input_text.send_keys('test text')
span.click()

assert '1' == p_counter.text

browser.quit()
