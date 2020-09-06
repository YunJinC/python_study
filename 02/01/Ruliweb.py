import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from package.MyLibrary import MyLibrary
import pandas as pd
import requests

class Ruliweb:
    
    def __init__(self):
        self.libs = MyLibrary()

    def login(self):
        url = 'https://user.ruliweb.com/member/login_proc'
        acct = pd.read_csv('D:\\03.Code\\06.python_study\\python_study\\02\\01\\account.scrt')
        data = {'user_id' : acct['ID'], 'user_pw' : acct['PW']}
        res = self.libs.sess.post(url, data=data)
        print('로그인 성공') if res.ok else print('로그인 실패')
    
    def setBaseUrl(self, url):
        self.base_url = url
    

if __name__ == "__main__":
    R = Ruliweb()
    R.login()



