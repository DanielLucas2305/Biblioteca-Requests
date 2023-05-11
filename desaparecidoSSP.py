import requests as rq
from bs4 import BeautifulSoup as bs
from lxml import html
import pandas as pd

all = []

response = rq.get("http://200.144.31.45/desaparecidos/default.aspx?filtro=homem")
content = response.content#o ponto content serve para ler o html do site acima
fonte = html.fromstring(response.content)

site = bs(content, 'html.parser')#o ponto parse converte em html
#print(site.prettify()) #o ponto prettify serve para estruturar o código igual ao html real do site
ver = site.findAll('i')#attrs serve para procurar um atributo no html
#print(ver)



for t in range(238, 248):
    nomes = fonte.xpath(f'//*[@id="ctl{t}_lblNome"]/text()')
    
    orig = fonte.xpath(f'//*[@id="ctl{t}_lblCidNasc"]/text()')
    
    nasc = fonte.xpath(f'//*[@id="ctl{t}_lblDtNasc"]/text()')
    print(nomes, orig, nasc)
    all.append([nomes[0], orig[0], nasc[0]])

desaps = pd.DataFrame(all, columns=['NOMES', 'ORIGEM', 'NASCIMENTO'])
#print(desaps)
desaps.to_excel('Desaps.xlsx')