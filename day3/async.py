# -*- coding = utf-8 -*-
# @Time : 2020/5/11 13:20
# @Author : AX
# @File : async.py
# @Software: PyCharm

import requests
headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/75.0"
}

try:
    rs=requests.get("https://api.apiopen.top/getJoke?page=1&count=2&type=video ")
    rs= rs.json()
    print(rs['result'])

except requests.exceptions as e:
    print(e['code'])
