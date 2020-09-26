import requests
import pandas as pd
import os
from bs4 import BeautifulSoup
from sqlalchemy import create_engine

class MyLibrary():

    def __init__(self):
        self.sess = requests.Session()
    
    def url2Html(self, url):
        res = self.sess.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        return soup

    def makeDir(self, path):
        try:
            if not(os.path.isdir(path)):
                os.makedirs(os.path.join(path))
        except:
            print("Failed to create directory!!!!!")
            raise

    def saveImg(self, url, path, fileName):
        self.makeDir(path)
        res = requests.get(url)
        f = open(path+"/"+fileName, "wb")
        f.write(res.content)
        f.close()

    def setEngine(self, tool, user=None, passwd=None, host=None, port=None, schema=None):
        
        if tool == 'sqlite':  
            self.engine = create_engine('sqlite:///sqlite.db', echo=False)
        else :
            toolParam = {
                'mysql' : 'mysql+mysqldb',            
            }

            params = pd.read_json('package//dbConfig.scrt', typ='series')

            if user != None : params['user'] = user
            if passwd != None : params['pass'] = passwd
            if host != None : params['host'] = host
            if port != None : params['port'] = port
            if schema != None : params['schema'] = schema

            self.engine = create_engine(toolParam[tool] + '://{user}:{pass}@{host}:{port}/{schema}?charset=utf8mb4'.format(**params), echo=False)
    

if __name__ == "__main__":
    crawler = MyLibrary()