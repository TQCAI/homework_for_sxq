#!/usr/bin/python3
# -*- coding: utf-8 -*-
from collections import Counter

'''
如何提交作业：
Step1：修改本文件文件名为学号_homework1, 例如：1901210100_homework1.py
Step2：在本文件内按要求完成本文件要求实现的函数，勿重命名函数名和参数名
Step3: 发送邮件到python_19@163.com，邮件标题同附件名，以截止时间2019/10/10 23:59:59 前的第一次提交为准
'''

'''
作业题
1.输入一个字符串，例如"  he threw three free throws "
1）（例题不计分）求出字符串长度（对于例句，输出为29), 请在def getStringLength()中实现；
2）计算句子中各单词（按空格分隔）出现的频数(通过字典存储)，请在def wordCount()中实现;
3）把字符串转换成全大写,并去除句首和句末的空格，请在def myFormatting()中实现

2.判断学生成绩是否达标。要求：输入一些学生的多门科目的成绩，
如果总成绩小于 100，记作未通过，否则通过，返回通过率，精确到小数点后两位，如0.90
'''

'''
Tips：
1. 注意输入输出要求的数据类型
2. 如何测试自己的代码是否正确？在其他.py中自定义数据并本地测试单个函数，注意去除self（如果对类和面向对象有了解的话有更好的办法），
对python环境安装和编辑器使用还有疑问？参考课件书本，或访问
https://code.visualstudio.com/
https://code.visualstudio.com/docs/python/python-tutorial
3. 需要更多的练习？请访问https://leetcode.com/problems
'''


class Solution:
    def getStringLength(self, myString):
        """
        :type myString: string
        :rtype: int
        """

        return len(myString)

    def wordCount(self, myString):
        """
        :type myString: string
        :rtype: {key:string, value:int}，字典
        """
        counter = Counter(myString.split(' '))
        if '' in counter: counter.pop('')
        return dict(counter)

    def myFormatting(self, myString):
        """
        :type myString: string
        :rtype: string        
        """

        return myString.strip().upper()

    def getPassingRate(self, rateList):
        """
        :type rateList: list[list[int]], 二维列表 
        :rtype:  float       
        """
        return round(sum([1 if sum(subList) >= 100 else 0 for subList in rateList]) / len(rateList), 2)
