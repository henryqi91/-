"""uuid"""
import uuid
print("uuid1:", uuid.uuid1())
print("uuid4:", uuid.uuid4())

from uuid import UUID
print("uuid3:", uuid.uuid3(UUID(int=1),name="123"))



"""OS文件目录"""
# import os
#
# if not os.path.exists('test'):
#     os.mkdir('test')
#
# with open(os.getcwd() + '/test/' + 'txtl.txt','w') as f:
#     f.write("hello world")