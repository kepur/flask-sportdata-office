"""
create by khan.hozin 2020/7/1
"""
__author__ = 'hozin'

import json
import requests
# http://api.avatardata.cn/Soccer/LiveGame?key=f46385384b4140208ae5a87df865932a

AppKey="f46385384b4140208ae5a87df865932a"
uri=" http://api.avatardata.cn/Soccer/AhoddsList?key={}&pid=3".format(AppKey)
headers = {'Content-Type': 'application/json'}
response = requests.get(url=uri, headers=headers)
result=json.loads(response.text)
print(result)


