
import requests
import pandas as pd
import json
import numpy as np

url = 'http://www.twse.com.tw/exchangeReport/FMTQIK?response=json&date=&_=1524707641392'
#url = 'http://www.twse.com.tw/indicesReport/MI_5MINS_HIST?response=json&date=&_=1524023635326'
response = requests.get(url)
json_form = json.loads(response.text)
df  = pd.DataFrame(json_form['data'])
df.to_csv('./market_info.csv', index=None, header=None)


