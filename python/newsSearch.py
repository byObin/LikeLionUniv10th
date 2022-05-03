
from bs4 import BeautifulSoup
import openpyxl
import requests
import pandas as pd
import numpy as np
from pandas import DataFrame
from openpyxl import workbook


keyword=input("검색할 키워드를 입력해주세요. : ")
pagenum=int(input("크롤링할 페이지를 입력해주세요. : "))
pagenum=(pagenum-1)*10+1
url = f"https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query={keyword}&start={pagenum}"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.select('a.news_tit')

index_list=[]
title_list=[]
x=1

for i in titles:
    title = i.get_text()
    index_list.append(x)
    title_list.append(title)
    x=x+1

data={'번호':index_list,'제목' : title_list}
df=pd.DataFrame(data,columns=['번호','제목'])
df.to_excel(excel_writer='article.xlsx', index=True)

print(df)

