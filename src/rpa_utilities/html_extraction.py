from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

url = "https://www.gsuplementos.com.br/"
driver = webdriver.Chrome()
driver.get(url)

time.sleep(30)

html_content = driver.page_source

soup = BeautifulSoup(html_content, 'html.parser')



# # section = soup.find_all(id="listagemMainContainer")
produtos = soup.find_all('a', class_="cardprod text-decoration-none")


for produto in produtos:
    # print(f"produto: {produto}")
    # Exemplo de como acessar o conteúdo ou atributos de cada produto
    nome_produto = produto.get_text(strip=True)
    link_produto = produto['href']
    
    print(f"Nome do produto: {nome_produto}, Link: {link_produto}")

##########################################################################

# Encontra todos os itens da lista de sabores
# sabores = soup.find_all('li', class_='filtros__container-lista-item')

# # Itera sobre os itens da lista e extrai os dados
# for sabor in sabores:
#     # Extrai o link
#     link = sabor.find('a', class_='filtros__container-lista-item-link')['href']
    
#     # Extrai o nome do sabor
#     nome_sabor = sabor.find('span').text
    
#     # Exibe o nome do sabor e o link
#     print(f"Sabor: {nome_sabor}, Link: {link}")