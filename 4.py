#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :4.py
# @Time      :2020/7/14 15:35
# @Author    :leafcool

# records = [
#     ('foo', 1, 2),
#     ('bar', 'hello'),
#     ('foo', 3, 4),
# ]
#
# def do_foo(x, y):
#     print('foo', x, y)
#
# def do_bar(s):
#     print('bar', s)
#
# for tag, *args in records:
#     if tag == 'foo':
#         do_foo(*args)
#     elif tag == 'bar':
#         do_bar(*args)
#

# 迭代
# items=[1,1,5,45,5,6,86,6,5]
# head,*tail=items
#
# def sum(items):
#     head,*tail=items
#     return head+sum(tail) if tail else head
#
# print(sum(items))

# import heapq
# nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# print(heapq.nlargest(3,nums))
# print(heapq.nsmallest(3,nums))
#
# portfolio = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
# expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
# print(cheap)
# print(expensive)

# rows = [
#     {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
#     {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
#     {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
#     {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
# ]
#
# from operator import itemgetter
# rows_by_fname = sorted(rows, key=itemgetter('fname'))
# rows_by_uid = sorted(rows, key=itemgetter('uid'))
# print(rows_by_fname)
# print(rows_by_uid)

# a = slice(5, 50, 2)
# print(a)

# words = [
#     'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
#     'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
#     'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
#     'my', 'eyes', "you're", 'under'
# ]
# from  collections import Counter
# word_counts=Counter(words)
# top_three=word_counts.most_common(3)
# print(top_three)

#listary app

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from operator import itemgetter
from itertools import groupby

# Sort by the desired field first
rows.sort(key=itemgetter('date'))
# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)

from collections import  defaultdict#多值词典
rows_by_data=defaultdict(list)
for row in rows:
    rows_by_data[row['date']].append(row)

for r in rows_by_data['07/01/2012']:
    print(r)

mylist=[1,4,-5,10,-7,2,3,-1]
print([n for n in mylist if n>0])
print([n for n in mylist if n<0])
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
import math
print([math.sqrt(n) for n in mylist if n > 0])
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p16_filter_sequence_elements.html
#https://github.com/EbookFoundation/free-programming-books/blob/master/free-programming-books-zh.md#ide
# http://lucida.me/blog/developer-reading-list/#python_essential_reference

