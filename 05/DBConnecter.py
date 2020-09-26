import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from package.MyLibrary import MyLibrary
import pandas as pd

class DBConnecter:
    
    def __init__(self):
        self.lib = MyLibrary()
    
    def getQuery(self, query):
        return pd.read_sql(query, con=self.lib.engine)
    
    def putDataFrame(self, df, table):
        df.to_sql(table, if_exists='append', index=False, con=self.lib.engine)
    
if __name__ == "__main__":
    D = DBConnecter()
    df = pd.read_excel('05/data/test.xlsx')

    D.lib.setEngine('sqlite')
    print(D.getQuery('SELECT * FROM sqlite_master WHERE type="table";'))
    D.putDataFrame(df, 'customer')
    print(D.getQuery('SELECT * FROM customer;'))

    D.lib.setEngine('mysql')
    print(D.getQuery('show databases'))
    D.putDataFrame(df, 'customer')
    print(D.getQuery('SELECT * FROM customer;'))


    


