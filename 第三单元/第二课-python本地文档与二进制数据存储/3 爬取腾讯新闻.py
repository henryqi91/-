import requests,json

headers = {
    "cookie": "RK=+foUjOoJx3; ptcz=4bcd907572d28e51333756494b70eb998488835a332158ea4c3993cb91e9d835; pvid=9751350034; tvfe_boss_uuid=8e24955117e8fbf5; pgv_pvid=635939967; pgv_pvi=3498835968; pac_uid=0_5d800beacc1f8; eas_sid=b1R5i7y7d5i467J489o0Z8F3M3; pgv_info=ssid=s3397335584; ts_last=news.qq.com/; ts_uid=4065882363; ad_play_index=18"
    ,"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    ,"referer": "https://news.qq.com/"
}

html = requests.get(url="https://news.qq.com/ext2020/apub/json/prevent.new.json", headers=headers)
# print(html.text)
content = json.loads(html.text)
# print(content)
for c in content:
    print(c["title"].strip(),c["id"].strip())