#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author leafcool
#
# from pathlib import *
# p=Path('.')
# for x in p.iterdir():
#     print(x)
#
# print('-----------------------------------------')
#
# p=Path('../')
# for x in p.glob('**/*.py'):
#     print(x)
#
# print('-----------------------------------------')
# p=Path('C:\Python27')
# for x in p.glob('**/*.txt'):
#     print(x)

# import  time
# for i in range(10):
#     print("当前时间：%s"%time.ctime())
#     time.sleep(1.5)

from urllib.parse import *
result=urlparse('https://mp.weixin.qq.com/s/S_7N8ZOLUZ_Zo9R9BKaLnw')
print(result)
print('scheme :', result.scheme, result[0])
print ( '主机和端口：',result.netloc,result[1])
print ('主机：', result.hostname)
print ( '端口：',result.port)
print('资源路径：',result.path,result[2])
print('参数：',result.params,result[3] )
print('查询字符串:',result.query , result[4])
print('fragment :',result.fragment, result[5])
print(result.geturl())

