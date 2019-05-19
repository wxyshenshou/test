# coding=utf-8
'''
request接口尝试
'''
import requests
import json
import pprint


class Bilibili():
    def __init__(self):
        self.url = 'https://api.bilibili.com/x/reply?jsonp=jsonp&pn=1&type=1&oid=52664208&sort=0&_=1558272125800'
        self.header = {'Referer': 'https://www.bilibili.com/video/av52664208/?spm_id_from=333.334.b_63686965665f7265636f6d6d656e64.20',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}
        #print (self.url)

    def bilib(self, data):
        # get请求用requests.get
        # self.html = requests.request(
        #     'POST', self.url, data=data, headers=self.header)

        self.html = requests.get(self.url, headers=self.header)
        print(self.html.status_code)
        # print(self.html.text)
        # 如果可以转为json格式则
        respons = json.loads(self.html.text)
        pprint.pprint(respons['data']['page']['count']//20+1)
        total_pages = respons['data']['page']['count']//20+1
        user_map = {}
        for page in range(total_pages, total_pages+1):
            r = requests.get(
                f'https://api.bilibili.com/x/reply?jsonp=jsonp&pn={page}&type=1&oid=52664208&sort=0&_=1558272125800')
            respons = json.loads(r.text)
            for i in respons['data']['replies']:
                # pprint.pprint(i['replies'])
                user_map[i['member']['mid']] = i['member']['uname']
                if i['replies'] != None:
                    for j in i['replies']:
                        # pprint.pprint(j['member']['mid'])
                        user_map[j['member']['mid']] = j['member']['uname']
        pprint.pprint(user_map)
        with open ('biliuser.txt','a',encoding='utf-8') as f:
            dd = str(user_map)
            f.write(dd)


biliurl = Bilibili()
data = {'callback': 'jQuery1720251185818952826_1558272119565',
        'jsonp': 'jsonp',
        'pn': '1',
        'type': '1',
        'oid': '52664208',
        'sort': '0',
        '_': '1558272125800'}

biliurl.bilib(data)
