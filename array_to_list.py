# -*- coding: utf-8 -*-

import re

wlist = []
with open('w1.h') as file:
    while True:
        line = file.readline()
        if not line: break
        dataline = re.search('{(.+)}', line)
        if dataline != None:
            dataline = dataline.group()
            stringlist = re.sub('{|}','',dataline).split(',')
            wlist.append([float(i) for i in stringlist])

