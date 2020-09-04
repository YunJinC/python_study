import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from package.CrawlingPackage import CrawlingPackage
import pandas as pd
import requests

class Ruliweb:
    
    def __init__(self):
        self.libs = CrawlingPackage()
        self.sess = requests.Session()

    def login(self):
        url = 'https://user.ruliweb.com/member/login_proc'
        acct = pd.read_csv('account.scrt')
        data = {'user_id' : acct['ID'], 'user_pw' : acct['PW']}
        self.sess.post(url, data=data)
    
    def setBaseUrl(self, url):
        self.base_url = url
    

if __name__ == "__main__":
    R = Ruliweb()
    R.login()



