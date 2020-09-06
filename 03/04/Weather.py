import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from package.MyLibrary import MyLibrary
import pandas as pd

class Weather:

    def __init__(self):
        self.libs = MyLibrary()
    
    def getMySite(self):
        url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1135057000'
        soup = self.libs.url2Html(url)
        columns = ['hour', 'day', 'temp', 'tmx', 'tmn', 'sky', 'pty', 'wfkor', 'wfen', 'pop'
                 , 'r12', 's12', 'ws', 'wd', 'wdkor', 'wden', 'reh', 'r06', 's06']
        datas = []
        for data in soup.select('data'):
            datas.append([data.select(columns[i])[0].text for i in range(len(columns))])
            
        return pd.DataFrame(datas, columns=columns)

if __name__ == "__main__":
    W = Weather()
    print(W.getMySite())
    