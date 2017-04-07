
import requests
import os
from bs4 import BeautifulSoup
import urllib

cs_url ='http://www.javlibrary.com/tw/vl_searchbyid.php'
cur_path= 'D:\\NB\新增資料夾 (3)'
pic_path= cur_path
error_path= cur_path
f_error = open(error_path+"\\"+"error.txt","a")
#cur_path = os.getcwd() #得知目前路徑
files = os.listdir(cur_path)  
for file in files:
    if file !="" :
        fname=os.path.splitext(file)[0]
        fname2=''
        for word in fname :
            if(word!= '.') :
                fname2 = fname2 + word
            else :
                fname=fname2
                break
        param ={'keyword':fname}
        r = requests.get(cs_url, params = param)
        bs = BeautifulSoup(r.text,"html.parser")
        link=bs.find(id="video_jacket_img")
        if link != None :
            url=link.get('src')
            pngweb = urllib.request.urlopen(url)
            pngin = pngweb.read()
            with open(pic_path+"\\"+fname+".jpg","wb") as code:
                code.write(pngin)
        else :
            print(fname)
            f_error.writelines(cur_path+"\\"+fname+"\n")
    else :
        break
f_error.close()
print("end.")


