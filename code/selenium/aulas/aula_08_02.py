from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import keyboard
import time

url = "https://curso-python-selenium.netlify.app/aula_08_a.html"
input_text = 'Selenium'


browser = Firefox()
browser.implicitly_wait(2)
browser.get(url)

# hi-level
texto = browser.find_element(By.NAME, 'texto')
# texto.send_keys(input_text) # The browser don't identify the Ctrl of S

# low-level
ac = ActionChains(browser)
ac.move_to_element(texto)
ac.click()
ac.key_down(Keys.SHIFT)
ac.key_down(input_text[0])
ac.key_up(input_text[0])
ac.key_up(Keys.SHIFT)
ac.perform()


keyboard.press_and_release('caps lock')
keyboard.send('alow')

time.sleep(2)

ac = ActionChains(browser)
ac.move_to_element(texto)
ac.click()
for i in input_text[1:]:
    ac.key_down(i)
    ac.key_up(i)

ac.perform()
