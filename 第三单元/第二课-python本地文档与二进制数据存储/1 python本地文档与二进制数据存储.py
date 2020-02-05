"""小块读取"""
import requests, uuid

def get_img(url):
    img = requests.get(url=url,stream=True)
    img_name = "{}.jpg".format(uuid.uuid4())
    with open(img_name,'wb') as f:
        chunks = img.iter_content(chunk_size=128)
        for chunk in chunks:
            f.write(chunk)

if __name__ == '__main__':
    url = "https://www.baidu.com"
    get_img(url)


"""Python操作文本"""
# r - 读取文件
# w - 创建文件（覆盖原文件）
# a - 追加文件（不存在会创建）
# b - 操作二进制流
# + - rw的集合
# with open('text.txt', 'r')as f:
#     # print(f.read())
#     content = f.readlines()
#     for c in content:
#         print(c.strip())

"""uuid"""
# import uuid
# print("uuid1:", uuid.uuid1())
# print("uuid4:", uuid.uuid4())
#
# from uuid import UUID
# print("uuid3:", uuid.uuid3(UUID(int=1),name="123"))
#


"""OS文件目录"""
# import os
#
# if not os.path.exists('test'):
#     os.mkdir('test')
#
# with open(os.getcwd() + '/test/' + 'txtl.txt','w') as f:
#     f.write("hello world")