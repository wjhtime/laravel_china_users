import requests
from lxml import etree
import common
from requests.adapters import HTTPAdapter
import time
# import logging
# logging.basicConfig(level=logging.DEBUG)


s = requests.session()
s.mount('http://', HTTPAdapter(max_retries=5))
url = "https://laravel-china.org/users/%d"
uid = 0
while True:
    uid+=1
    response = s.get(url % uid)
    if response.status_code != 200:
        common.sleep(uid)
        continue

    e = etree.HTML(response.content)
    name = e.xpath("//h3[@class='media-heading']/text()")[0].strip()
    label = e.xpath("//a[@class='label label-success role']/text()")
    if label:
        label = label[0]
    else:
        label = ""
    followers = e.xpath("//div[@class='follow-info row']/div[1]/a/text()")[0]
    discuss = e.xpath("//div[@class='follow-info row']/div[2]/a/text()")[0]
    article = e.xpath("//div[@class='follow-info row']/div[3]/a/text()")[0]
    row = {'uid': uid, 'name': name, 'label': label, 'followers': followers, 'discuss': discuss, 'article': article}
    common.save_mysql(row)

    common.sleep(uid)


