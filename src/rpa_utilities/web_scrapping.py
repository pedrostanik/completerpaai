from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import pandas as pd
import os

class WebScrapping():
    def __init__(self, navigator):
        self.path_data = r'C:\Users\pedro\OneDrive\Documentos\projetos\projeto_rpa_ia\src\data\dados.csv'
        self.driver = None       
        if navigator == 'chrome':
           self.driver = webdriver.Chrome()
        elif navigator == 'edge':
            self.driver = webdriver.Edge()
        elif navigator == 'firefox':
            self.executedriver = webdriver.Firefox()
        else:
            raise Exception('Navegador inválido!')
        self.wait = WebDriverWait(self.driver, 20)
        if os.path.getsize(self.path_data) > 0:
            self.dados = pd.read_csv(self.path_data)
        

    def execute(self, url):
        self.driver.get(url)
        time.sleep(2)
        # for element in elements:
        #     time.sleep(3)
        #     field = self.wait.until(EC.visibility_of_element_located((By.XPATH, element)))
        #     field.click()

        search = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="buscaCabecalho"]/form/input')))
        time.sleep(5)
        search.send_keys('whey')
        botao = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="buscaCabecalho"]/form/div[1]/button')))
        botao.click()
        time.sleep(6)

        html_content = self.driver.page_source

        soup = BeautifulSoup(html_content, 'html.parser')

        # # section = soup.find_all(id="listagemMainContainer")
        produtos = soup.find_all('a', class_="cardprod text-decoration-none")
        produtos_dict = {}
        produtos_list = []
        for produto in produtos:
            # print(f"produto: {produto}")
            # Exemplo de como acessar o conteúdo ou atributos de cada produto
            nome_produto = produto.get_text(strip=True)
            link_produto = produto['href']
            
            print(f"Nome do produto: {nome_produto}, Link: {link_produto}")
            produtos_list.append(nome_produto)
        
        produtos_dict["produtos"] = produtos_list
        df = pd.DataFrame(produtos_dict)
        df.to_csv(r'C:\Users\pedro\OneDrive\Documentos\projetos\projeto_rpa_ia\src\data\dados.csv', sep=';', index=False, encoding='utf-8')

        return produtos_dict