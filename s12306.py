#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/31 21:50
# @Author  : Geda

import requests
import ssl
import sys
import time
ssl._create_default_https_context=ssl._create_unverified_context()
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
reload(sys)
sys.setdefaultencoding("utf-8")
def get_code():
    list=[];
    code_location=raw_input(u'请输入验证码坐标:')
    for i  in code_location:
        code =(int(i)*2+1)*35
        list.append(code)

    return list
def login(sess):

    print "hello geda"

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

    '''
    验证验证码
    '''
    post_url='https://kyfw.12306.cn/passport/captcha/captcha-check'
    code = get_code()
    data={
        'answer':code,
        'login_site':'E',
        'rand':'sjrand'
    }
    html=sess.post(post_url,data,headers).json()
    print  html['result_message']
    '''
    正经登录
    '''
    login_url='https://kyfw.12306.cn/passport/web/login'
    data={
        'username':'15235153137',
        'password':'g.488666',
        'appid':'otn'
    }
    login_html=sess.post(login_url,data,headers).content
    print login_html
    # time.sleep(1)
    # query_ticket_url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-11-15&leftTicketDTO.from_station=\
    #             TNV&leftTicketDTO.to_station=LHV&purpose_codes=ADULT'
    # result= sess.get(query_ticket_url,headers=headers).content
    # print result


if __name__ == '__main__':
    sess = requests.session()
    login(sess)

