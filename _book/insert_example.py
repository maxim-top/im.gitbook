#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import re
import os

repo = sys.argv[1]
inFilePath = sys.argv[2]
tmpFilePath = inFilePath + '.tmp'
inFile = open(inFilePath)
tmpFile = open(tmpFilePath, 'w')
className = ""
line1 = '''**Example**:'''
line2 = '''```'''
line4 = '''```'''
example = ''
begin = False

patternClass = r'^title: .*:(.*)'
patternFunc = r'^### function (.*)'

if repo == 'lanying-im-ios':
    patternClass = r'# (.*) (Class|Protocol) Reference'
    patternFunc = r'^### (.*)'
if repo != 'lanying-im-ios':
    begin = True

while True:
    lines = inFile.readlines(10000)
    if not lines:
        break
    for line in lines:
        matchObj = re.match(patternClass, line)
        if matchObj:
            className = matchObj.group(1) # 获取类名
        if repo == 'lanying-im-ios' and (re.match(r'^## Class Methods$', line) or re.match(r'^## Instance Methods$', line)):
            begin = True
        matchObj = re.match(patternFunc, line)
        if begin and matchObj:
            funcName = matchObj.group(1) # 获取函数名
            line3 = ''.join(['{% lanying_code_snippet repo="', repo, '",class="', className, '",function="', funcName, '" %}{% endlanying_code_snippet %}'])
            if not len(example) == 0:
                tmpFile.write(example)
            example = ''.join([line1, '\n', line2, '\n', line3, '\n', line4, '\n'])
        if repo != 'lanying-im-ios' and re.match(r'^-------------------------------$', line):
            tmpFile.write(example)

        tmpFile.write(line)
if repo == 'lanying-im-ios':
    tmpFile.write(example)
inFile.close()
tmpFile.close()
os.rename(tmpFilePath, inFilePath)
