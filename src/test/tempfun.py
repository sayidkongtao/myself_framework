#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2016��10��30��

@author: kttao
'''
from lxml import etree
import os

PATH = lambda p:os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),p)
        )

filepath = PATH(r"../configuration/project_testdata/example/english_example.xml")

print filepath

document = etree.ElementTree(file = filepath)

root = document.getroot()


activityElement = root.xpath(".//appActivity[@activityName = '.base.UiDrawerBaseAct11']")
print len(activityElement)
print dir(activityElement[0])
print activityElement[0].attrib
print activityElement[0].Value()

class XMLElements():
    def __init__(self):
        self.__filepath = PATH(r"../configuration/project_testdata/example/english_example.xml")
        self.__root = etree(file = filepath).getroot()
    
    def findEleBy_activityName(self,activityName):
        activityElement = self.__root.xpath(activityName)
        if len(activityElement) == 1:
            return activityElement[0]
        elif len(activityElement) == 0:
             
            
        
        