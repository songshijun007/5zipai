import urllib.request
import re
import os


mianurl = 'http://www.6zipai.com/'
targetPath = 'D:/spider/51zipai/picture1/'
def getdata(url):
    headers = {
                   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/60.0.3112.113 Safari/537.36'
                   }
    request = urllib.request.Request(url = url,headers=headers)
    response = urllib.request.urlopen(request)
    data = response.read()
    return data
#print(data)

#爬取首页帖子网址
data = getdata(mianurl).decode('utf-8')
reg = re.compile('<li class="i_list list_n2"> <a href="(.*?)" title="(.*?)"> <img')
data = re.findall(reg,data)
#爬取每篇帖子的图片
for i in range(0,len(data)):
    url = data[i][0]
    title = data[i][1]
    print(url,title)
    print('http://www.6zipai.com' + url)
    data1 = getdata('http://www.6zipai.com/' + url).decode('utf-8')
    #print(data1)
    reg = re.compile('<img src=\'(.*?)\'>')
    pictureurl = re.findall(reg,data1)
    #保存图片
        #创建路径，以标题创建文件夹
    Path = targetPath + title
    if not os.path.isdir(Path):
        os.mkdir(Path)
    endPath = Path + '/'
    for j in pictureurl:
        link = 'http://www.6zipai.com/' + j
        print(link)
        pos = link.rindex('/')
        t = os.path.join(endPath, link[pos + 1:])
        print(t)
        pic = getdata(link)
        with open(t,'wb') as f:
           f.write(pic)
        #with open(path,'w',encoding = 'utf-8') as f:f.write(data)

