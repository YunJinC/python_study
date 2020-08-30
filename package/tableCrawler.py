import requests
import pandas as pd
from bs4 import BeautifulSoup

class tableCrawler():
    
    def url2Html(self, url):
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        return soup

    def tableCrawling(self, url, where='table'):
        soup = self.url2Html(url)
        df = []
        for table in soup.select(where):
            header = []
            for th in table.select('th'):
                header = [td.text.strip() for td in th.select('td')]
            data = []
            for tr in table.select('tr'):
                data.append([td.text.strip() for td in th.select('td')])
            df.append(pd.Dataframe(data, columns=header))
        return df

if __name__ == "__main__":
    print('start')
    crawler = tableCrawler()
    print(crawler.tableCrawling('http://www.ppomppu.co.kr/zboard/zboard.php?id=money'))