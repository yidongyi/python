#-*-coding:utf8-*-

import requests
from lxml import etree

cook = {"Cookie": "SINAGLOBAL=3040909481746.1655.1496844570518; UM_distinctid=15cb98144ec69d-0ee54009e21ab7-474f0820-1fa400-15cb98144ed77b; _s_tentry=zsw.gdxa.cn; UOR=www.pcpop.com,widget.weibo.com,zsw.gdxa.cn; login_sid_t=a6f5b3462e559b97fc4c243fc32e6881; Apache=8026906060280.308.1502871244065; ULV=1502871244072:3:1:1:8026906060280.308.1502871244065:1497760875945"}
url = 'http://weibo.com/' #此处请修改为微博网址
# html = requests.get(url).content
# print html
html = requests.get(url, cookies = cook).content
# html = requests.get(url, cookies = cook).text

# html = bytes(bytearray(html, encoding='utf-8'))
selector = etree.HTML(html)
content = selector.xpath('//span[@class="ctt"]')
for each in content:
    text = each.xpath('string(.)')
    b = 1
    print text
