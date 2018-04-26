# -*- encoding: utf8-*-
import pandas as pd
import requests

url = 'http://mops.twse.com.tw/mops/web/ajax_t78sb04'

payload = {

    'encodeURIComponent':'1',
    'TYPEK':'all',
    'step':'1',
    'run':'Y',
    'firstin':'true',
    'FUNTYPE':'02',
    'year':'107',
    'season':'01',
    'fund_no':'0'

}
res = requests.post(url, data=payload)
res.encoding ='utf-8'
pd_tables = pd.read_html(res.text)
df = pd.DataFrame(pd_tables[1])


df.iloc[0,0] = df.iloc[0,1]
df.iloc[0,1] = df.iloc[0,2]
df.iloc[0,2] = df.iloc[0,3]
df.iloc[0,3] = df.iloc[0,4]

df.iloc[1,0] = df.iloc[1,1]
df.iloc[1,1] = df.iloc[1,2]
df.iloc[1,2] = df.iloc[1,3]
df.iloc[1,3] = df.iloc[1,4]
df = df.drop(4, axis=1)
#pd_tables.iloc[0,0] = pd_tables.iloc[0,1]
#pd_tables[1].to_csv('component.csv', header=None, index=False)
#print(pd_tables[1])
df.to_csv('component.csv', header=None, index=False)
#print(df.to_csv('component.csv', header=None, index=False))
