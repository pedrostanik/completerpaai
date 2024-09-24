from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://www.gsuplementos.com.br/"
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)
driver.get(url)

search = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="buscaCabecalho"]/form/input')))
time.sleep(5)
search.send_keys('whey')
botao = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="buscaCabecalho"]/form/div[1]/button')))
botao.click()
time.sleep(6)

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