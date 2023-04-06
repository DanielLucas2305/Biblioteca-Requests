import requests as rq
from bs4 import BeautifulSoup as bs
import pandas as pd

lista_noticias = []


response = rq.get("https://g1.globo.com/")
content = response.content#o ponto content serve para ler o html do site acima

site = bs(content, 'html.parser')#o ponto parse converte em html
#print(site.prettify()) #o ponto prettify serve para estruturar o código igual ao html real do site
noticias = site.findAll('div', attrs={'class' : 'feed-post-body'})#attrs serve para procurar um atributo no html

for noticia in noticias:
    #titulo
    titulo = noticia.find('a', attrs={'class' : 'feed-post-link'})
    print(titulo.text)
    print(titulo['href'])#href é para pegar o link da notícia
    #subtitulo
    sub = noticia.find('div', attrs={'class' : 'feed-post-body-resumo'})
    if (sub):
        print(sub.text)
        lista_noticias.append([titulo.text, sub.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text, '', titulo['href']])

    #print(noticias)
    
    print("------------------*********************-------------")

print(lista_noticias)  

news = pd.DataFrame(lista_noticias, columns=["TITULO", "SUBTITULO", "LINK"])
news.to_excel("Tabela de noticias.xlsx", index =False)#Index igual a false não escreve o index na tabela

print(news)
#print(type(site))
#print(response.content)
#print(type(response))