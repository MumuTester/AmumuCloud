#!/usr/bin/python
# -*- coding: utf-8 -*-

#@Project Name：AmumuCloud
#@File    Name：class_demos.py
#@User    Name: amumu
#@Editor  Time: 2020-03-18

import os
import sys
import time
from tkinter import *
from appium import webdriver


class demos(object):
    def __init__(self,username,password):
        self.username = username
        self.password = password

    #普通方法可以直接调用类中的其他变量
    def order_def(self):
        self.oder_username = self.username
        self.oder_password = self.password
        return self.oder_username,self.oder_password

    #静态方法内部无法直接调用类中的其他变量
    @staticmethod
    def staticmethods(*args):
        statics = "staticmethods"
        methods = 888888
        return args,statics,methods

    #类的装饰方法无法直接调用其他的变量
    @classmethod
    def classmethods(cls,password,func):
        cls.funcs = func(password)
        cls.classmethod_username = cls.funcs
        return cls.funcs

#用于传递高阶函数给demos类中的classmethod
def super_def(password):
    username = "super_mumu"
    password = password
    return username,password

#实例化demos类，new一个实例化对象
get_demos = demos("sadmummy",123456)

if __name__ == '__main__':
    print("调用demos类中inint的变量：%s,%d" %(get_demos.username,get_demos.password))
    print("调用demos类中order_def函数：",get_demos.order_def())
    print("调用demos类中staticmethods函数：",get_demos.staticmethods("ammu",654321))
    print("调用demos类中classmethods函数：",get_demos.classmethods(333333,super_def))



