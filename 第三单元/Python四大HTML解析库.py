#解析百度为例（练习）
from lxml import etree
import requests

headers ={

}
def get_content(html):
    soup = etree.HTML(html.text)
    titles = soup.xpath('//div[@id="content_left"]/div[contains(@class,"result")]')
    for t in titles:
        title = t.xpath('h3/a/text()')
        print(title)

if __name__ == '__main__':
    html = requests.get("http://www.baidu.com/s?wd=python")
    # print(html.text)
    get_content(html)

# #获取所有的标题
# html = requests.get("https://www.baidu.com/s?wd=python")
# html = etree.HTML(html.text)
# res = html.xpath('//div[@id="content_left"] / div[contains(@class,"result")] ')
# print(res)


#xpath语法练习
# from lxml import etree
# import requests
#
# html = requests.get("https://www.runoob.com/python3/python3-tutorial.html")
# soup = etree.HTML(html.text)
# titles = soup.xpath('//div[@class="design"]/a/text()')
# for title in titles:
#     print(title.strip())

#正则表达式练习
# import re
# text = '<a href="http://www.baidu.com">'\
#     'href="www.news163.com">'\
#     'Python表达式</a>'

#re.sub(pattern,replace,text,flag) -----NLP常用

#re.compile(pattern[.flags])
#match,search,findall(少),finditer(多),group,groups
# res = re.compile('href="(.*?)"', re.I | re.S)
# for r in res.finditer(text):
#     print(r.groups())
# # print(res.findall(text))

#re.match(pattern, string,flag)

# res = re.match('<a href=".*?"', text, re.I)
# print(res)

# #必备字符串操作：str.split
# urls = ['a','b','c']
# print(' '.join(urls))
#
# #必备字符串操作：str.split
# url = 'http://www.baidu.com/python'
# url.split()
#
#
# #必备字符串操作：str.translate
# inp = "aeiou"  #inp 一一对应 oup
# outp = "12345"
# trantab = str.maketrans(inp,outp)
#
# text = "this is a string example .... wowp!"
# print(text.translate(trantab))

#必备字符串操作：str.replace(a,b)
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
