import requests
import pandas as pd
import os
from bs4 import BeautifulSoup

class CrawlingPackage():
    
    def url2Html(self, url):
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        return soup

    def makeDir(self, path):
        try:
            if not(os.path.isdir(path)):
                os.makedirs(os.path.join(path))
        except OSError as e:
            print("Failed to create directory!!!!!")
            raise


    def saveImg(self, url, path, fileName):
        self.makeDir(path)
        res = requests.get(url)
        f = open(path+"/"+fileName, "wb")
        f.write(res.content)
        f.close()


if __name__ == "__main__":
    crawler = CrawlingPackage()