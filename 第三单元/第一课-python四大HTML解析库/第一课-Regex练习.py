# 练习1：熟悉正则表达式
# 用正则表达式爬取百度搜索的所有链接和标题
import requests
import re

headers ={
    "Cookie": "BAIDUID=FB486F8AEE5483C06DA00B5641B7B885:FG=1; BIDUPSID=FB486F8AEE5483C06DA00B5641B7B885; PSTM=1563553227; BDUSS=2NTOHVPLTE2MDg4eUtESG1yd0l6NTIwNVltbEQtRVp2LWpvUzloZXo4WjNORzFkSVFBQUFBJCQAAAAAAAAAAAEAAABSyO2eAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHenRV13p0VdN; BD_UPN=12314753; MCITY=-180%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; yjs_js_security_passport=51e61761dd99b16057174b08ec9b033626616c8e_1580292326_js; H_PS_PSSID=1455_21088_26350; delPer=0; BD_CK_SAM=1; PSINO=7; COOKIE_SESSION=1095_1_8_6_4_6_0_0_8_4_0_3_6556_0_0_0_1580292087_1580116322_1580295961%7C9%235266_4_1580116289%7C3; H_PS_645EC=dccff69AnajB1GcTKZyBHiCrVLvFNJNxOgwrVM4Ixcpm8cIk2RCTEdiVBBg"
    ,"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}

def get_content(url):
    html = requests.get(url, headers=headers).text
    titles = re.compile(html,)
    print(html)


if __name__ == '__main__':
    url = "https://www.baidu.com/s?wd=python"
    get_content(url=url)
    pass


#练习2：正则表达式匹配邮箱(面试题）


"""习题自己练习"""
# 判断字符串是否全部是小写
import re

