__author__ = 'liulei'
# coding urf-8
# a web spider for data mining
import requests
import re
import sys

#reload(sys)
#sys.setdefaultencoding("gb18030")
type=sys.getfilesystemencoding()
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'}
#html=requests.get('http://wenku.baidu.com/new?fr=home')
file_url=open('D:/webSpider/url.txt')
url=file_url.read()
file_url.close()
html=requests.get(url, headers=headers)
html.encoding='utf-8'
print(html.encoding)

f=open('D:/webSpider/test.html','w',encoding='utf-8')
f.write(html.text)
f.close()
#print(html.text)
chinese=re.findall('color: #039;">(.*?)</a>',html.text,re.S)
for each1 in chinese:
    print(each1)



