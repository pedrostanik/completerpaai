from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class WebScrapping():
    def __init__(self, navigator):
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
        

    def execute(self, url, elements):
        self.driver.get(url)
        for element in elements:
            time.sleep(3)
            field = self.wait.until(EC.visibility_of_element_located((By.XPATH, element)))
            field.click()