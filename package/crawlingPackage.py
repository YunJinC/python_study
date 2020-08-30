import requests
import pandas as pd
from bs4 import BeautifulSoup

class crawlingPackage():
    
    def url2Html(self, url):
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        return soup

if __name__ == "__main__":
    crawler = crawlingPackage()