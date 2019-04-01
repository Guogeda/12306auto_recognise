#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/4 1:00
# @Author  : Geda


from aip import AipOcr
from aip import AipImageClassify
from aip import AipImageSearch
import os
import json

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#识别验证码中的文字部分
def get_text_content(text_path):

    """ 我的 APPID AK SK """
    APP_ID = '10326210'
    API_KEY = '1UR5GCdXV6ZPpRGXBU5T2gGj'
    SECRET_KEY = '1v9cyHl4inmySnG8fqEY6uAiUAvN36Ga'

    def get_file_content(filePath):
         with open(filePath, 'rb') as fp:
             return fp.read()

    aipOcr=AipOcr(APP_ID,API_KEY,SECRET_KEY)
    #调用通用文字识别接口
    try:
        result = aipOcr.basicGeneral(get_file_content(text_path))['words_result'][0]['words']
    except IndexError,e:
        return None

    return result

#获取验证码中的图片信息，识别内容有菜名，汽车，动物，植物
def get_pic_detail():
    """ 你的 APPID AK SK """
    APP_ID = '10327698'
    API_KEY = 'xe7uEVwG7aPfIwrYdCpbBBke'
    SECRET_KEY = 'rEdBGcYjOPmq8ZZG2GVF4XXjkvva3UGC'

    aipImageClassify = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    image = get_file_content('00.jpg')
    options={}
    print (aipImageClassify.objectDetect(image, options))

#图片搜索功能入库
def pic_indatebase(filePath,Name):
    """ 你的 APPID AK SK """
    APP_ID = '10327828'
    API_KEY = 'PGmsAVMTBtahp6X7PWGbfgur'
    SECRET_KEY = 'xLQGw2bscQXDZgBQpIs36x2W3g8qcedz '

    aipImageSearch = AipImageSearch(APP_ID, API_KEY, SECRET_KEY)
    """ 读取图片 """

    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    image = get_file_content(filePath)
    """ 如果有可选参数 """
    options = {}
    options["brief"] = "{\"name\":\"%s\",}"%Name

    """ 带参数调用相似图检索—入库 """
    result=aipImageSearch.similarAdd(image, options)

       # """ 调用相似图检索—检索 """
    # result =aipImageSearch.sameHqSearch(image)

    print result

#图片检索
def pic_search(pic_path):
    '''

    :param pic_path: 要识别图片地址
    :return: 返回list 结果
    '''
    """ 你的 APPID AK SK """
    result1=[]
    APP_ID = '10327828'
    API_KEY = 'PGmsAVMTBtahp6X7PWGbfgur'
    SECRET_KEY = 'xLQGw2bscQXDZgBQpIs36x2W3g8qcedz '

    aipImageSearch = AipImageSearch(APP_ID, API_KEY, SECRET_KEY)
    """ 读取图片 """

    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    image = get_file_content(pic_path)


    """ 调用相似图检索—检索 """
    result =aipImageSearch.similarSearch(image)['result']
    for i in result[:3]:
        #print i['brief'][9:11]
        result1.append(i['brief'][9:11])

    return result1

def get_local_path():
    start_path='C:/Users/GUO/Desktop/pic_lib'
    for i  in os.listdir(start_path):
        #print  i.decode('gbk').encode('utf-8')
        path=start_path+'/'+i
        name=i.decode('gbk').encode('utf-8')
        #print name
        for j in  os.listdir(path):
            path=start_path+'/'+name+'/'+j
            path=u'%s'%path
            print path
            pic_indatebase(path,name)
            # '''
            # 清除已经存在的图片库文件
            # '''
            # if os.path.exists(path):
            #     os.remove(path)

    path = 'C:/Users/GUO/Desktop/pic_lib'


if __name__ == '__main__':
    #print get_text_content('text.jpg')
    # get_pic_detail()
    #print get_text_content('text.jpg')
    get_local_path()
