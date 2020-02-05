"""
Assignment: 爬取腾讯新闻 title,url,text 分别存入：txt,csv文件
"""
import requests, json, bs4
from lxml import etree
import os
import pandas as pd

df = pd.DataFrame(columns=["title", "author", "url", "detail"])

headers = {
    "cookie": "RK=+foUjOoJx3; ptcz=4bcd907572d28e51333756494b70eb998488835a332158ea4c3993cb91e9d835; pvid=9751350034; tvfe_boss_uuid=8e24955117e8fbf5; pgv_pvid=635939967; pgv_pvi=3498835968; pac_uid=0_5d800beacc1f8; eas_sid=b1R5i7y7d5i467J489o0Z8F3M3; pgv_info=ssid=s3397335584; ts_last=news.qq.com/; ts_uid=4065882363; ad_play_index=18"
    , "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    , "referer": "https://news.qq.com/"
}

session = requests.session()
html0 = session.get(url="https://news.qq.com/ext2020/apub/json/prevent.new.json", headers=headers)
content = json.loads(html0.text)
counter = 0
for c in content:
    # print(c["title"].strip(), c["id"].strip())
    curr_title = c["title"].strip()
    curr_url = "https://new.qq.com/rain/a/{}.html".format(c["id"])
    html = session.get(url=curr_url)
    if html.status_code == 200:
        # soup = etree.HTML(html.text)
        # intro = soup.xpath(" /html/body/div[3]/div[1]/h1")
        soup = bs4.BeautifulSoup(html.text, "lxml")
        infos = soup.select("div.content-article p.one-p")
        # print(infos)
        try:
            intro = soup.select_one("div.introduction").getText()
        except:
            continue
        curr_data = ""
        curr_author = infos[0].text
        for info in infos[1:]:
            curr_data += info.text

        #储存到csv文件
        # curr_row = {"title":curr_title, "author":curr_author, "url":curr_url, "detail":curr_data}
        curr_row = pd.DataFrame([[curr_title, curr_author, curr_url, curr_data]], columns=["title", "author", "url", "detail"])
        # print(curr_row)
        df = df.append(curr_row, ignore_index=True)
        counter += 1
        print("progress: ",counter,"/",len(content))
        # print(df,'\n')
df.to_csv("result.csv")


