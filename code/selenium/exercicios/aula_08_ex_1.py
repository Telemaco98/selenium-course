"""
    Dizer todas as cores possíveis da caixinha
    https://curso-python-selenium.netlify.app/caixinha
    # Spoiler: são 17 cores

    Ações: click, double click, context menu, mouseenter, mouseleave
    Modificadores: Crtl, Shift, Ctrl + Shift


    My notes:
        FIXME         execute all possible actions, including modfiers - Tip: make a method
          MISSING COLORS - there is some bug here, because double click is not identified.
          It can be not a selenium fault, but a script issue
              {evento:"dblclick", cor:"lightsalmon", shift:False, ctrl:True}
              {evento:"dblclick", cor:"olivedrab", shift:True, ctrl:True}
        
        DONE          show the results of colors set
"""

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlparse
import sys

def perform_actions():
    ac.double_click()
    ac.click()

def caixinha_colors(*keys):
    for key in keys:
        ac.key_down(key)

    ac.move_to_element(caixinha)
    perform_actions()
    ac.move_to_element(span)

    ac.pause(2)
    for key in keys:
        ac.key_up(key)

def result_colors(textarea_str):
    textarea_str = textarea_str.replace('evento', '"evento"').replace('cor', '"cor"').replace('shift', '"shift"').replace('ctrl', '"ctrl"')
    textarea_json = '[' + textarea_str.replace('\n', ',') + ']'

    result = eval(textarea_json)
    colors_set = set()

    for row in result:
        colors_set.add(row['cor'])

    print(f'We find out {len(colors_set)} colors. They are:')
    i = 1
    for color in colors_set:
        print(f'{i}. {color}')
        i += 1

url = "https://curso-python-selenium.netlify.app/caixinha"
browser = Firefox()
browser.get(url)

ac = ActionChains(browser)

caixinha = browser.find_element(By.ID, 'caixa')
span = browser.find_element(By.TAG_NAME, 'span')

caixinha_colors(Keys.CONTROL)
caixinha_colors(Keys.CONTROL, Keys.SHIFT)
caixinha_colors(Keys.SHIFT)
caixinha_colors()

ac.move_to_element(caixinha)
ac.context_click()
ac.move_to_element(span)

ac.perform()

textarea = browser.find_element(By.ID, 'area')
result_colors(textarea.text)