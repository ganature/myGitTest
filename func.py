#coding=utf-8

import os


def readTxt(file_name):
    data=[]
    with open(file_name,'rb')as file_content:
        for f in file_content.readlines():
            data.append(f)
    return data
