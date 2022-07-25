# -*- coding: UTF-8 -*-
# @author: admin
# @createTime: 2022/7/25 14:28 
# @description:

def china(start, end):
    for page in range(start, end + 1):
        yield f'https://tech.china.com/articles/index_{str(page)}.html'
