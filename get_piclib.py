#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/6 19:31
# @Author  : Geda

import  requests
import deal_code_img
import  time
import baiduapi
import ssl
import xlwt
from PIL import Image
ssl._create_default_https_context=ssl._create_unverified_context()
ssl._create_default_https_context=ssl._create_unverified_context()
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#登录获取验证码
def get_code_path():
    '''

    :param code_path:输入每一个验证码保存的地址
    :return: 验证码保存的地址
    '''
    sess = requests.session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'
    }
    '''
    获取验证码
    '''
    url ='https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&'
    authon_code=sess.get(url,headers=headers,verify=False).content

    with open('code.jpg','wb') as f:
        f.write(authon_code)


    return 'code.jpg'


if __name__ == '__main__':

    n = 0
    # items = []
    # while n<200:
    #
    #     try:
    #         result= baiduapi.get_text_content(deal_code_img.get_text_path(get_code_path(n)))
    #
    #         print (u'第%s识别为%s\n')%(n,result)
    #         items.append(n)
    #         items.append(result)
    #         n += 1
    #         time.sleep(5)
    #     except IOError,e:
    #         items.append(n)
    #         items.append(u'识别失败')
    #
    # new_table = u'100次识别结果.xls'
    # wb = xlwt.Workbook(encoding='utf-8')
    # ws = wb.add_sheet('test1')
    # headDate = ['识别数n', '识别结果']
    # for colnum in range(0, 2):
    #     ws.write(0, colnum, headDate[colnum], xlwt.easyxf('font: bold on'))
    # index = 1
    # j = 0
    # lens = (len(items))
    # while j < lens:
    #     for i in range(0, 2):
    #         ws.write(index, i, items[j])
    #         j += 1
    #     index += 1
    #
    # wb.save(new_table)
    while n < 200:
        try:

            deal_code_img.get_pic_path('piclib/code%s' % n)
            print u'正在处理第%s张验证码' % n
            n += 1
            time.sleep(5)
        except IOError, e:
            print u'第%s张失败' % n


