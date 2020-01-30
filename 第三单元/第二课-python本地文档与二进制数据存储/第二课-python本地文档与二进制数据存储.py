"""Python操作文本"""
# r - 读取文件
# w - 创建文件（覆盖原文件）
# a - 追加文件（不存在会创建）
# b - 操作二进制流
# + - rw的集合
with open('text.txt', 'r')as f:
    print(f.read())

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