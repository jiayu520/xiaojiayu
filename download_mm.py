# -*- coding: utf-8 -*-
import os
import urllib.request

def download_mm(folder='ooxx',pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url = "http://jandan.net/ooxx"
    page_num = int(get_page(url))