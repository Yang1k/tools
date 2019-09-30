
import sys
import os
import re
import zipfile
import pymysql
import time

# 解压到的目录
global unpack_path 
unpack_path = "./scan/scan_file/"
# webshell_rule的地址
global rule_path
rule_path = "./scan/rule.txt"

# 存储上传的压缩包的路径
global zip_path
zip_path = "./upload/"

# 解压
def unpack(file_path):
    f = zipfile.ZipFile(file_path,'r')
    global file_name
    file_name = os.path.basename(file_path)[:-4]
    dir_name = '%s%s'%(unpack_path,file_name)
    for file in f.namelist():
        f.extract(file,dir_name)
    return dir_name


#获取所有文件路径
def get_filepath(file_dir):
    file_path = []
    for root,dirs,files in os.walk(file_dir):
        for name in files:
            file_path.append(os.path.join(root,name))
    return file_path


#扫描文件内容
def scan(file_path):
    webshell_list = read_rule('%s'%(rule_path))
    result_file = []
    f = open(file_path,'r',encoding='UTF-8')
    filestr = f.read()
    for rule in webshell_list:
        rule = rule.strip()
        result = re.findall(rule,filestr)
        # print(result)
        if result:
            code_line = get_code(rule,file_path) # 获取具体的那一行代码
            print('-----------')
            result_file = {
                'dubios' : rule,
                'file_path' : file_path,
                'code' : code_line 
            }
            break
    if result_file:
        return result_file
    else:
        return "ok_file"
    # print(result_file)
    
def get_code(rule,file_path):
    f = open(file_path,'r',encoding='UTF-8')
    line_list = f.readlines()
    # print(line_list)
    for line in line_list:
        # print(line)
        result = re.findall(rule,line)
        # print(result)
        if result:
            return line
    if not result:
        return "not found"
    #     if result:
    #         return line
    #     else:
    # return "not found"

def begin(source_pack):
    file_dir  = unpack(source_pack)
    file_path = get_filepath(file_dir)
    re_list = []
    num = 0
    for item in file_path:
        if ('.DS_Store' in str(item)) or ('__MACOSX' in str(item)):
            os.remove(item)
        else:
            if (item[-4:] in '.php') or (item[-4:] in '.txt') or (item[-4:] in '.asp'):
                num += 1
                flag = "ok_file"
                try:
                    flag = scan(item)
                except:
                    pass
                if str(flag) not in  'ok_file':
                    re_list.append(flag)
    return re_list,num
def read_rule(rule_file_path):
    list_webshell = []
    webshell_txt = open(rule_file_path, 'r').readlines()
    for i in webshell_txt:
        list_webshell.append(i)
    return list_webshell

def ins_database(result,now_time):
    db = pymysql.connect("localhost","root","root","scan")
    cursor = db.cursor()
    for item in result[0]:
        if str(type(item)) in "<class 'dict'>":
            try:
                # print("11111")
                # filename 扫描的什么文件，记录的内容是扫描的哪一个网站 ，filepath 恶意文件路径，code 恶意代码
                # project = 'test'
                cursor.execute('insert into scan_table(project,filepath,code,time) value("%s","%s","%s","%s")'%(file_name,str(item['file_path']),str(item['code']),now_time))
                db.commit()
            except:
                db.rollback()
    db.close()

if __name__ == '__main__':
    zip_name = sys.argv[1]
    source_pack = '%s%s'%(zip_path,zip_name)
    result = begin(source_pack)
    print("总计扫描"+str(result[1])+"个文件")
    now_time = int(time.time())
    ins_database(result,now_time)
