import sys
import os
import re

# 解压
f = zipfile.ZipFile("zipfilePath",'r')
for file in f.namelist():
    f.extract(file,"./file/")