#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/1 0:09
# @Author  : Geda
import cv2 as cv
from PIL import Image
from pytesser import *
import pytesseract

def get_text_path(img_path):
    '''
    裁剪出验证码的文字部分
    输入：验证码地址
    输出：得到验证码文字部分图片
    '''
    img=Image.open(img_path)
    width=img.size[0]
    height=img.size[1]
    #print width,height
    region=(121,0,270,29,)
    cropimg=img.crop(region)
    cropimg.save('text.jpg')
    return 'text.jpg'


def test_cv(img_path):
    '''

    :param img_path:
    :return:
    '''
    im =Image.open(img_path)
    #创建窗口并显示图像
    cv.namedWindow("Image")
    cv.imshow("Image",im)
    cv.waitKey(0)
    #释放窗口
    cv.destroyAllWindows()

def get_pic_detail_tessract(img_path):

    '''
    用 tessract ocr 识别验证码中图片
    pytesseract.image_to_string函数config配置 如下：'\\'不能用'\'代替，双引号不能缺少
    输入：含有文字图片的地址
    输出：文字ocr识别的内容
    默认是中文简体识别。
    '''
    tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
    text2 = pytesseract.image_to_string(Image.open(img_path),lang='eng' ,config=tessdata_dir_config)
    return text2


def get_pic_path(img_path):
    '''
    把验证码中的图片部分裁剪出来
    输入：验证码的地址
    输出：验证码的图片地址
    地址坐标：00 01 02 04 10 11 12 13 14

    '''
    pic_path=[]
    for i  in range(0,4):
        for j   in range(0,2):
            region = (
                (
                    5*(i+1)+67*i,
                    41+72*j,
                    72 *(i+1),
                    108+72*j,
                )
            )
            img =Image.open(img_path)
            cropimg = img.crop(region)

            cropimg.save('%s%s.jpg'%(i,j))
            pic_path.append('%s%s.jpg'%(i,j))
    return pic_path


if __name__ == '__main__':
    img_path='E:/Pythontest/sptyut/authoncode/image.jpg'
    print get_pic_detail_tessract(img_path)
