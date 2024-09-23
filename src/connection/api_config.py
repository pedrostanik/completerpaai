import Flask
from src.rpa_utilities.web_scrapping import WebScrapping

app = Flask(__name__)
URL = 'www.gsuplementos.com.br'
ELEMENTS = ['//*[@id="buscaCabecalho"]/form/input']
@app.route('/getHtml')
def get_html():
   web_scrapping = WebScrapping('chrome')
   web_scrapping.execute(URL, ELEMENTS)