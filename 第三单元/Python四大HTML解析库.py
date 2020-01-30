"""解析百度为例（练习）"""
from lxml import etree
import requests
headers ={
    "Cookie": "BAIDUID=FB486F8AEE5483C06DA00B5641B7B885:FG=1; BIDUPSID=FB486F8AEE5483C06DA00B5641B7B885; PSTM=1563553227; BDUSS=2NTOHVPLTE2MDg4eUtESG1yd0l6NTIwNVltbEQtRVp2LWpvUzloZXo4WjNORzFkSVFBQUFBJCQAAAAAAAAAAAEAAABSyO2eAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHenRV13p0VdN; BD_UPN=12314753; MCITY=-180%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; yjs_js_security_passport=51e61761dd99b16057174b08ec9b033626616c8e_1580292326_js; H_PS_PSSID=1455_21088_26350; delPer=0; BD_CK_SAM=1; PSINO=7; COOKIE_SESSION=1095_1_8_6_4_6_0_0_8_4_0_3_6556_0_0_0_1580292087_1580116322_1580295961%7C9%235266_4_1580116289%7C3; H_PS_645EC=dccff69AnajB1GcTKZyBHiCrVLvFNJNxOgwrVM4Ixcpm8cIk2RCTEdiVBBg"
    ,"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}
def get_content(html):
    soup = etree.HTML(html.text)
    titles = soup.xpath('//div[@id="content_left"]/div[contains(@class,"result")]')
    for t in titles:
        title = t.xpath('h3/a/text()')
        url = t.xpath('h3/a/@href')
        # print("".join(title))
        # print(url[0])

if __name__ == '__main__':
    html = requests.get("http://www.baidu.com/s?wd=python", headers=headers)
    get_content(html)

"""获取所有的标题"""
# html = requests.get("https://www.baidu.com/s?wd=python")
# html = etree.HTML(html.text)
# res = html.xpath('//div[@id="content_left"] / div[contains(@class,"result")] ')
# print(res)


"""xpath语法练习"""
# from lxml import etree
# import requests
#
# html = requests.get("https://www.runoob.com/python3/python3-tutorial.html")
# soup = etree.HTML(html.text)
# titles = soup.xpath('//div[@class="design"]/a/text()')
# for title in titles:
#     print(title.strip())

"""正则表达式练习"""
# import re
# text = '<a href="http://www.baidu.com">'\
#     'href="www.news163.com">'\
#     'Python表达式</a>'

"""re.sub(pattern,replace,text,flag) -----NLP常用"""

"""re.compile(pattern[.flags])
#match,search,findall(少),finditer(多),group,groups"""
# res = re.compile('href="(.*?)"', re.I | re.S)
# for r in res.finditer(text):
#     print(r.groups())
# # print(res.findall(text))

"""re.match(pattern, string,flag)"""

# res = re.match('<a href=".*?"', text, re.I)
# print(res)

"""必备字符串操作：str.split"""
# urls = ['a','b','c']
# print(' '.join(urls))
#
"""必备字符串操作：str.split"""
# url = 'http://www.baidu.com/python'
# url.split()
#
#
"""必备字符串操作：str.translate"""
# inp = "aeiou"  #inp 一一对应 oup
# outp = "12345"
# trantab = str.maketrans(inp,outp)
#
# text = "this is a string example .... wowp!"
# print(text.translate(trantab))

"""必备字符串操作：str.replace(a,b)"""
# url = 'http://www.baidu.com'
# url = url.replace('baidu','python')
# print(url)


# import requests
# html = requests.get('http://www.baidu.com')
# html.encoding = 'utf8'
# print(html.text)

# text = "文本"
# html = text.encode('utf8')
# print(html)
# html = html.decode('utf8')
# print(html)
