from bs4 import BeautifulSoup
import requests
import os

url = 'http://zhongxinzhiyuan.cn/yiqing_real_time_map.html'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
url_get = requests.get(url,headers = header)
'''url_decode = url_get.content.decode("gb2312","ignore").encode("utf-8","ignore") #gb2312为网页编码
url_soup = BeautifulSoup(url_decode,'html.parser')
all_a = url_soup.find('div',id="zuixin").find_all('a',attrs={"class":"title"}) #此处attrs={"class":"title"}必须为大括号
for a in all_a:
    title = a.get_text().replace('/','') #取得<a>标签中的text
    href = a.get('href') #取得<a>标签中的href
    img_url = url + href[1:-4] + '(1).htm' #补全herf
    if os.path.isdir(os.path.join("D:\zhuoku",title)): #如果存在文件夹
        print('exist ' + title)
        pass #跳过
    else: #否则
        os.makedirs(os.path.join("D:\zhuoku",title)) #创建文件夹
        print('makedir ' + title)
    os.chdir("D:\zhuoku\\"+title) #切换到此文件夹
    img_url_get = requests.get(img_url,headers = header)
    img_url_soup = BeautifulSoup(img_url_get.text,'html.parser')
    max_img_page = img_url_soup.find('div',id="yema").find_all('a')[-1].get_text() #[-1]表示find_all('a')中的最后一个
    for page in range(1, int(max_img_page)+1):
        jpg_href = url + href[1:-4] + '(' + str(page) + ').htm' + '#turn' #jpg网址
        jpg_href_get = requests.get(jpg_href,headers = header)
        jpg_soup = BeautifulSoup(jpg_href_get.text,'html.parser')
        jpg_url = jpg_soup.find('div',id="bizhiimg").find('img')['src'] #jpg网址中的图片文件地址
        name = jpg_url[-9:] #截取图片文件地址的倒数第9位至末尾为图片的名字
        if os.path.isfile(name): #如果存在名为name的文件
            print(name + ' exist skip')
            pass #下面全跳过
        else: #否则
            jpg_header = {
                    'Referer':jpg_href,
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'
                    }
            jpg = requests.get(jpg_url,headers = jpg_header) #jpg文件地址解析
            f = open(name, 'ab')
            f.write(jpg.content)
            print(name + ' saved')
            f.close()
print('congratulations! all finished!')'''