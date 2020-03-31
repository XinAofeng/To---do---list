import requests,json,os
#定义一个获取数据的函数，参数为url
def getData(url):
    #模拟请求头
    headers={"user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/63.0.3239.132 Safari/537.36"}
    #使用requests库的get方法，获得消息对象r
    r = requests.get(url,headers=headers)
    try:
        #设置消息对象的编码方式为原网页的显式编码
        r.encoding= r.apparent_encoding
        #提取消息对象中的text文本内容，就是想要的数据
        result=r.text
    except:
        print("error")
    return result
def data():
    url = 'https://gwpre.sina.cn/interface/fymap2020_data.json?_=1584150310964'  #定位到的URL
    data= getData(url)          #获得数据，不过是字符串形式的。
    data_dict=json.loads(data)  #将字符串转换为字典对象
    d = data_dict['data']   #打印键为data的内容
    history_data = d['historylist']
    today = history_data[0]
    yesterday = history_data[1]
    incress = int(today['cn_conNum']) - int(yesterday['cn_conNum'])
    #print(history_data)
    #print("截至%s累计确诊%s" % (today['date'] , today['cn_conNum']))
    return today['date'] , today['cn_conNum'] , incress