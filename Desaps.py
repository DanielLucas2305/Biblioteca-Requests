import requests as rq
from bs4 import BeautifulSoup as bs

response = rq.get("http://200.144.31.45/desaparecidos/default.aspx?filtro=homem")
content = response.content#o ponto content serve para ler o html do site acima

site = bs(content, 'html.parser')#o ponto parse converte em html
#print(site.prettify()) #o ponto prettify serve para estruturar o código igual ao html real do site
ver = site.findAll('i')#attrs serve para procurar um tributo no html
#print(ver)

for v in ver:
    nome = v.find("span")
    print(nome)
    

#print(type(ver))