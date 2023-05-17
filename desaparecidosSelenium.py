from selenium import webdriver
from time import sleep
import csv
navegador = webdriver.Chrome()

all = [] #lista vazia

#Funções para a busca de homens e mulheres

def searchs():
    for t in range(238, 248):
        sleep(1)
        nomes = navegador.find_element('xpath', f'//*[@id="ctl{t}_lblNome"]').text
        
        orig = navegador.find_element('xpath', f'//*[@id="ctl{t}_lblCidNasc"]').text
        
        nasc = navegador.find_element('xpath', f'//*[@id="ctl{t}_lblDtNasc"]').text
        print(nomes, orig, nasc)
        all.append([nomes, orig, nasc])
        sleep(1.3)


#Inicio da busca no site
navegador.get("http://200.144.31.45/desaparecidos/default.aspx?")
sleep(4)
pags = navegador.find_element('xpath', '//*[@id="LkBtnLimpar"]').click()
sleep(2)
segpag = navegador.find_element('xpath', '//*[@id="link2"]').click()
sleep(3)

#Loop para busca em todas as páginas
for a in range(1, 3):
    segpag = navegador.find_element('xpath', f'//*[@id="link{a}"]').click()
    searchs()
    print("-#-"*7,f"Página([{a}]) Abaixo",'-*-'*7)
    print(all)
    print("-#-"*7,f"Página([{a}]) Acima",'-*-'*7)

sleep(3)

for a in range(3, 139):
    segpag = navegador.find_element('xpath', f'//*[@id="link{a}"]').click()
    searchs()
    print("-#-"*7,f"Página([{a}]) Abaixo",'-*-'*7)
    print(all)
    print("-#-"*7,f"Página([{a}]) Acima",'-*-'*7)


#criação do arquivo csv
with open('DB.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(all)

csvfile.close()


'''
# outras anotações
#homens

//*[@id="link1"]
//*[@id="link2"]
//*[@id="link5"]
//*[@id="link131"]
//*[@id="link129"]

#mulheres

//*[@id="link21"]


#full XPath
'''