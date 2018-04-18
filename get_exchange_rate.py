import requests as req
import pandas as pd
from time import sleep

payload = {'download':'','hdn_gostartdate':'2017/09/1','hdn_goenddate':'2017/11/30','syear':'2017','smonth':'09','sday':'1','eyear':'2017','emonth':'11','eday':'30','datestart':'2017/09/1','dateend':'2017/11/30'}

err_count = 0
while err_count <3:
    try:
        html = req.post('http://www.taifex.com.tw/chinese/3/3_5.asp', data=payload)
        break
    except:
        sleep(5)
        err_count += 1
        continue
if err_count == 3:
    print('連線失敗')

#注意網頁編碼
html.encoding = 'utf-8'
df = pd.read_html(html.text)
df = df[2] #這裡的數字必須從0開始試，直到選取所需資料為止
df.columns = df.iloc[0] #指定第一列為欄位名稱
df = df.drop(0).reset_index(drop=True) #刪除第一列
df.sort_index(ascending=False).head() #以index排序(由新到舊)


df.to_csv('./exchange_rate.csv', sep=',',  index=False)
