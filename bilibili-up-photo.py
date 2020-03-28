import requests
import json
import uuid
import time
headers = {
'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36 Edg/80.0.361.57'
           }
def photo(url):
    html = requests.get(url, headers)  # get函数获取图片链接地址，requests发送访问请求
    content = requests.get(url).content
    name = 'photo'
    namespace = uuid.uuid1()
    text=uuid.uuid5(namespace, name)
    title = 'E:\\photoes\\' + str(text)
    img_name = title + '.png'
    with open(img_name, 'wb') as file:  # 以byte形式将图片数据写入
        file.write(html.content)
        file.flush()
        file.close()  # 关闭文件
    time.sleep(2)

def make_url(url_strat):
    res = requests.get(url_strat, headers=headers)
    pic_json=json.loads(res.text)
    url_list=[]
    for i in range(0,30):
        for z in range(0,11):
            try:
                url = (pic_json['data']['items'][i]['pictures'][z]['img_src'])
                url_list.append(url)
            except:
                break
    return url_list

if __name__ == '__main__':
    url_strat_lists=[
        'https://api.vc.bilibili.com/link_draw/v1/doc/doc_list?uid=168687092&page_num=1&page_size=30&biz=all'
        'https://api.vc.bilibili.com/link_draw/v1/doc/doc_list?uid=168687092&page_num=2&page_size=30&biz=all'
        'https://api.vc.bilibili.com/link_draw/v1/doc/doc_list?uid=168687092&page_num=3&page_size=30&biz=all'
        'https://api.vc.bilibili.com/link_draw/v1/doc/doc_list?uid=168687092&page_num=4&page_size=30&biz=all'
    ]
    for url_start_list in url_strat_lists:
        url_list = make_url(url_strat=url_start_list)
        for url in url_list:
            photo(url)