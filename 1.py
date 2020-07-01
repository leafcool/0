#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1.py
# @Time      :2020/6/29 10:58
# @Author    :leafcool

import matplotlib.pyplot as plt
import  numpy as np
plt.rcParams['font.sans-serif']=['SimHei']

# x_data=['2011','2012','2013','2014','2015','2016','2017']
# y_data=[2800,5541,154,52121,54542,2288,84122]
# plt.plot(x_data,y_data)
# plt.show()

# ''' 等高线图'''
# delta=0.025
# x=np.arange(-3.0,3.0,delta)
# y=np.arange(-2.0,2.0,delta)
# X,Y=np.meshgrid(x,y)
# Z1=np.exp(-X**2-Y**2)
# Z2=np.exp(-(X-1)**2-(Y-1)**2)
# z=(Z1-Z2)*2
# plt.contourf(x,y,z,16,delta=0.75,cmap='rainbow')
# C=plt.contour(x,y,z,16,colors='black',linewidth=0.5)
# plt.clabel(C,inline=True,fontsize=10)
# plt.xticks(())
# plt.yticks(())
# plt.title("等高线")
# plt.xlabel("维度")
# plt.ylabel("经度")
# plt.show()


'''3D图'''
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure(figsize=(12,8))
ax=Axes3D(fig)

delta=0.125
x=np.arange(-3.0,-3.0,delta)
y=np.arange(-2.0,2.0,delta)
X, Y=np.meshgrid(x,y)
Z1=np.exp(-X**2-Y**2)
Z2=np.exp(-(X-1)**2-(Y-1)**2)
Z=X**2+Y**3+X**2+X*Y
ax.plot_surface(X,Y,Z,
    rstride=1,
    cstride=1,
    cmap=plt.get_cmap('rainbow'))
ax.set_zlim(-2,2)
plt.title("3D图")
plt.show()
# plt.savefig('fig.png',bbox_inches='tight')

