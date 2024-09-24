from flask import Flask, jsonify
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.rpa_utilities.web_scrapping import WebScrapping



app = Flask(__name__)
URL = 'https://www.gsuplementos.com.br/'
# ELEMENTS = ['//*[@id="buscaCabecalho"]/form/input']
@app.route('/getHtml')
def get_html():
   web_scrapping = WebScrapping('chrome')
   result = web_scrapping.execute(URL)
   result_json = jsonify(result)
   return result_json

if __name__=="__main__":
   app.run(debug=False)