import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from package.CrawlingPackage import CrawlingPackage

class NaverImg:
    
    def __init__(self):
        self.base_url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
        self.libs = CrawlingPackage()
    
    def setKeyword(self, keyword):
        self.keyword = keyword
    
    def setImgUrlList(self):
        if self.keyword == '':
            print('키워드를 입력해 주세요')
        else:
            soup = self.libs.url2Html(self.base_url + self.keyword)
            self.imgUrlList = [img.attrs['data-source'] for img in soup.select('.photowall img')]
    
    def saveImgs(self):
        for i in range(len(self.imgUrlList)):
            self.libs.saveImg(self.imgUrlList[i], './'+self.keyword, self.keyword+'_'+str(i)+'.jpg')


if __name__ == "__main__":
    N = NaverImg()
    N.setKeyword('파이썬')
    N.setImgUrlList()
    N.saveImgs()



