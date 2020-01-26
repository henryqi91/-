from urllib import parse
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool  #多进程
import time # 效果对比
from uuid import uuid4
import os

"""
说明：
- 加快下载速度：使用session
- 多进程：每个json一个进程(辨识：不同pn)
- **增加用户需要的搜索结果的数量
- 未优化【多线程】的爬取结果编号部分。

"""

headers = {
    "Cookie": "BAIDUID=FB486F8AEE5483C06DA00B5641B7B885:FG=1; BIDUPSID=FB486F8AEE5483C06DA00B5641B7B885; PSTM=1563553227; BDUSS=2NTOHVPLTE2MDg4eUtESG1yd0l6NTIwNVltbEQtRVp2LWpvUzloZXo4WjNORzFkSVFBQUFBJCQAAAAAAAAAAAEAAABSyO2eAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHenRV13p0VdN; indexPageSugList=%5B%22%E5%8D%87%E5%9B%BD%E6%97%97%20%E5%B0%8F%E5%AD%A6%20%E5%8D%A1%E9%80%9A%22%2C%22%E5%8D%87%E5%9B%BD%E6%97%97%20%E5%B0%8F%E5%AD%A6%22%2C%22%E5%8D%87%E5%9B%BD%E6%97%97%22%2C%22%E9%9D%A2%E5%90%91%22%5D; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; MCITY=-180%3A; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=1; H_PS_PSSID=1455_21088_26350; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=www.baidu.com; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm"
    ,"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    ,"Referer": "http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=python"
    ,"Connection": "keep-alive"
}

num = 0 #图片计数器

def get_data(url,session):
    global num
    html = session.get(url, headers=headers)
    if html.status_code == 200:
        try:
            content = html.json()['data']
            for c in content[:-1]:
                if num >= num_of_results:
                    break
                #下载图片
                img = session.get(c['middleURL'], headers=headers)
                with open("imgs/{}.jpg".format(uuid4()), 'wb') as f:
                    f.write(img.content)
                    num += 1
                    print(num)
        except:
            pass
    else:
        print("ERROR fetching HTML, pls check ur internet connection or contact your ISP")
    pass

def get_data2(url,start_num):
    num = start_num
    session = requests.session()
    # html = requests.get(url,headers=headers)
    html = session.get(url, headers=headers)
    if html.status_code == 200:
        print("成功获取网页，解析中....")
        soup = BeautifulSoup(html.text, 'lxml')
        results = soup.select('div.result.c-container')
        for result in results:
            title = result.select_one('h3 a').text
            href = result.select_one('h3 a')['href']
            desc = result.select_one('div.c-abstract').text
            # img_link = result.select('div.general_image_pic.c-span6 a img')['src']
            print("【{}】".format(num), title, href)
            print(title, href)
            print("--", desc)
            # print("img link:",img_link)
            num += 1
    else:
        print("ERROR")

    print("FINISHED!",start_num // 8)
    pass

def download_img(url):
    pass

if __name__ == '__main__':
    if not os.path.exists("imgs"):
        os.makedirs("imgs")
    # start_time = time.time() # 时间对比测试
    keyword = 'python'
    num_of_results = 50
    # keyword = parse.quote(input("请输入你的关键字>>>> "))
    # num_of_results = int(input("请输入结果数量>>> "))
    session = requests.session()

    # #### 单进程
    # for i in range(1,num_of_results//30+2):
    #     url = "http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={}" \
    #           "&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word={}" \
    #           "&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&force=&pn={}" \
    #           "&rn=30&gsm=&1580012267072=".format(keyword,keyword,30*i)
    #     get_data(url=url,session=session)

    #### 多进程版本，每个json一个进程
    p = Pool(6) #cpu core = 6
    for i in range(1, num_of_results//30+2):
        url = "http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={}" \
              "&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word={}" \
              "&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&force=&pn={}" \
              "&rn=30&gsm=&1580012267072=".format(keyword, keyword, 30*i)
        p.apply_async(get_data, args=(url,session,))
    p.close()
    p.join()

    # 时间对比测试
    # end_time = time.time()
    # time_elapsed = end_time - start_time
    # print(time_elapsed)
