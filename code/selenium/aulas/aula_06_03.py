"""
 Aula 06_a
    Seletores com Combinadores:
        Irmão adjacentes    (A + B)
        Geral de irmãos     (A ~ B)         A ~ B selects all B that follow a A
        Filhos              (A > B)
        Descendentes        (A   B)
    Nessa URL vimos vários outros Combinadores: https://flukeout.github.io
        A                   A
        #id                 Elemento com o id
        #id A               Descendentes do #id
        .classname          Elemento com a class = classname
        A.classname         A da classname
        A, B                A and B
        *                   Todos
        A *                 Todos descendentes de A
        A + B               Todos os irmãos B que são adjacentes ao A
        A ~ B               Todos os irmãos B que sucedem o A
        A > B               Todos os B filhos de A
        A:first-child       Todos os A que são first-child
        *:only-child        Todos que são filhos únicos (only-child)
        B:last-child        Todos os B que são o último filho (last-child)
        A:nth-child(n)      O n-ésimo dos A elementos
        A:nth-lastchild(n)  O n-ésimo ultimo dos A elementos
        A:first-of-type     O primeiro do tipo A
        A:nth-of-type(n)    O n-ésimo do tipo A
        A:nth-of-type(xn+y) O n-ésimo do tipo A, começando em y pulando de x em x
        B > A:only-of-type  O único do tipo A que seja filho de B
        A:last-of-type      O último do tipo A
        A:empty             Todos os A que não tenham elementos dentro dele
        :not(X)             Todos os não X-elementos
        [att]               Todos que tenham o atributte
        A[attribute]        Todos do tipo A que tenham o atributo `att`
        [att="value"]       Todos que tenham o atributo att="value"
        [att^="value"]      Todos que tenham o atributo att começando com "value"
        [att$="value"]      Todos que tenham o atributo att terminando com "value"
        [att*="value"]      Todos que tenham o atributo att que o valor contenha "value"
"""


from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

url = "https://curso-python-selenium.netlify.app/aula_06_a.html"
browser = Firefox()
browser.implicitly_wait(2)
browser.get(url)

fg = browser.find_element(By.CSS_SELECTOR, 'div.form-group')
