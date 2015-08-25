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
url=file_url.readline()
i=0
while url:
    url=url.strip('\n')
    html=requests.get(url, headers=headers)
    html.encoding='utf-8'
    #print(html.encoding)
    dst='D:/webSpider/'+str(i)+'.html'
    f=open(dst,'w',encoding='utf-8')
    f.write(html.text)
    f.close()

    #data mining
    names=re.findall('<h1>(.*?)</h1>',html.text,re.S)
    for eachName in names:
        print(eachName)
    description=re.findall('<meta name="description" content="(.*?)>',html.text,re.S)
    print(description[0])
    resume=re.findall('<div class="para">(.*?)</div>',html.text,re.S)
    for eachResume in resume:
        print(eachResume.strip('<(.*?)>'))


    print('URL:'+url)
    url=file_url.readline()
    i=i+1
file_url.close()
#print(html.text)
#chinese=re.findall('color: #039;">(.*?)</a>',html.text,re.S)
#for each1 in chinese:
   # print(each1)



