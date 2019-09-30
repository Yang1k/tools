import sys
import os
import re
import zipfile

# 解压
def unpack(file_path):
    f = zipfile.ZipFile(file_path,'r')
    for file in f.namelist():
        f.extract(file,"D:\write\scan\\file")
unpack("D:\write\scan\scan.zip")

#获取所有文件路径
def get_filepath(file_dir):
    file_path = []
    for root,dirs,files in os.walk(file_dir):
        for name in files:
            file_path.append(os.path.join(root,name))
    return file_path
print(get_filepath("D:\write\scan\\file"))

# for name in all_file:
#     f = open(name)
#     lines = f.readlines();