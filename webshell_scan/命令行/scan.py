import sys
import os
import re

# webshell_rule的地址
global rule_path
rule_path = "./rule.txt"

def logo():
    print(""" 
    _____________
   < Webshell_Scan >
    -------------
 _    _       __  __            
| |  | |     |  \/  |           
| |__| |_   _| \  / | ___ _ __  
|  __  | | | | |\/| |/ _ \ '_ \ 
| |  | | |_| | |  | |  __/ | | |
|_|  |_|\__,_|_|  |_|\___|_| |_|
                                
      """)

#获取所有文件路径
def get_filepath(file_dir):
    file_path = []
    for root,dirs,files in os.walk(file_dir):
        for name in files:
            file_path.append(os.path.join(root,name))
    return file_path

# 获取正则
def read_rule(rule_file_path):
    list_webshell = []
    webshell_txt = open(rule_file_path, 'r').readlines()
    for i in webshell_txt:
        list_webshell.append(i)
    return list_webshell

#扫描文件内容
def scan(file_path):
    webshell_list = read_rule('%s'%(rule_path))
    result_file = []
    f = open(file_path,'r',encoding='UTF-8')
    filestr = f.read()
    for rule in webshell_list:
        rule = rule.strip()
        result = re.findall(rule,filestr)
        if result:
            # 将恶意文件路径存入result_file
            result_file = {
                'file_path' : file_path,
            }
            break
    if result_file:
        return result_file
    else:
        return "ok_file"


# 开始扫描
def begin(file_path):
    file_path = get_filepath(file_path)
    file_num = len(file_path)
    re_list = []
    webshell_num = 0
    for item in file_path:
        if (item[-4:] in '.php') or (item[-4:] in '.txt') or (item[-4:] in '.asp'):
            flag = "ok_file"
            try:
                flag = scan(item)
            except:
                pass
            if str(flag) not in  'ok_file':
                webshell_num += 1
                re_list.append(flag)
    return re_list,file_num,webshell_num

if __name__ == '__main__':
    logo()
    file_path = sys.argv[1]
    result = begin(file_path)
    print("总计扫描"+str(result[1])+"个文件,检测到"+str(result[2])+'个webshell！！！')
    for item in result[0]:
        print('\033[1;31m恶意文件路径：'+item['file_path']+' \033[0m')




















