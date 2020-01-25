from urllib import parse
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool  #多进程
import time # 效果对比

"""
说明：
- 加快下载速度：使用session
- 多进程：每个页面一个进程
- 未优化【多线程】的爬取结果编号部分。

***时间对比（100个结果）： 
    - requests —— 7.5
    - session —— 6.6
    - multiprocessing + requests —— 2.3
    - multiprocessing + session —— 2.3
结论：
    - session比request要快
    - multiprocessing的情况下，request vs. session时间差不多————分析是因为每页爬取的数量较少（8个），没有显著区别。
    
"""

headers = {
    "Cookie": "BAIDUID=FB486F8AEE5483C06DA00B5641B7B885:FG=1; BIDUPSID=FB486F8AEE5483C06DA00B5641B7B885; PSTM=1563553227; BDUSS=2NTOHVPLTE2MDg4eUtESG1yd0l6NTIwNVltbEQtRVp2LWpvUzloZXo4WjNORzFkSVFBQUFBJCQAAAAAAAAAAAEAAABSyO2eAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHenRV13p0VdN; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; BD_CK_SAM=1; BD_HOME=1; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; MCITY=-180%3A; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=1455_21088_26350; ZD_ENTRY=baidu; PSINO=1; COOKIE_SESSION=42_1_6_7_2_6_0_0_5_4_0_0_490195_0_0_0_1578037686_1579971641_1579971644%7C9%234254627_19_1579971602%7C9; H_PS_645EC=3a82Nf2yRuh%2FlZLdmZxyDczcO5x1OIagcqtMwAQET7zNaYjRXNqYkyoyoF8"
    ,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}

def get_data(url, num_of_results):
    # start_time = time.time() #下载时间测试戳
    num = 1
    # 时间对比（40个结果）： requests——3.12秒左右；session——2.88秒左右；session+multiprocessing——
    session = requests.session()
    while num <= num_of_results:
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
                print("--",desc)
                # print("img link:",img_link)
                if num > num_of_results:
                    break
                num += 1
            if num > num_of_results:
                break
        else:
            print("ERROR")
    print("FINISHED!")
    # 以下为下载时间测试
    # end_time = time.time()
    # time_elapsed = end_time - start_time
    # print(time_elapsed)
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
    # start_time = time.time() #时间对比测试

    keyword = 'python'
    num_of_results = 100
    # url = 'https://www.baidu.com/s?wd={}'.format(parse.quote(keyword))
    # get_data(url=url, num_of_results=num_of_results)  #普通版本

    #多进程版本，每一页一个进程
    page_num = num_of_results // 8 + 1
    p = Pool(6) #我的电脑是6核的
    for i in range(page_num):
        start_num = 8*i
        url = 'http://image.baidu.com/search/index?tn=baiduimage&word={}&pn={}'.format(parse.quote(keyword), 10*i)
        p.apply_async(get_data2, args=(url, start_num,))
    p.close()
    p.join()

    # 以下为下载时间测试
    # end_time = time.time()
    # time_elapsed = end_time - start_time
    # print(time_elapsed)
