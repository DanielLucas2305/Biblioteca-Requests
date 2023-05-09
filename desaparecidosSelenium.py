from selenium import webdriver
from time import sleep
navegador = webdriver.Chrome()

all = [] #lista vazia

navegador.get("http://200.144.31.45/desaparecidos/default.aspx?filtro=homem")


def searchs():
    q = navegador.maximize_window
    for t in range(238, 248):
        sleep(1.5)
        nomes = navegador.find_element('xpath', f'//*[@id="ctl{t}_lblNome"]').text
        
        orig = navegador.find_element('xpath', f'//*[@id="ctl{t}_lblCidNasc"]').text
        
        nasc = navegador.find_element('xpath', f'//*[@id="ctl{t}_lblDtNasc"]').text
        print(nomes, orig, nasc)
        all.append([nomes, orig, nasc][0])

# searchs()

# print(all)

pags = navegador.find_element('xpath', '//*[@id="lkBtnIdades"]').click()
sleep(2)
segpag = navegador.find_element('xpath', '//*[@id="link2"]').click()
sleep(5)
for a in range(1, 139):
    segpag = navegador.find_element('xpath', f'//*[@id="link{a}"]').click()
    searchs()
    print(all)
    print("-#-"*7,"Próxima Página",'-*-'*7)


'''
//*[@id="link1"]
//*[@id="link2"]
//*[@id="link5"]
//*[@id="link131"]
//*[@id="link129"]

#full XPath

/html/body/form/div[3]/div[2]/div[3]/div[3]/div/div/div/a[3]
/html/body/form/div[3]/div[2]/div[3]/div[3]/div/div/div/a[4]
/html/body/form/div[3]/div[2]/div[3]/div[3]/div/div/div/a[5]
/html/body/form/div[3]/div[2]/div[3]/div[3]/div/div/div/a[6]


'''

# for a in range(1, 139):
#     elem = str(f'//*[@id="link{a}"]"]')
#     pag = navegador.find_element('xpath', elem).click()