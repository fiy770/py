
import requests
import os
from bs4 import BeautifulSoup
import urllib

cs_url ='http://www.javlibrary.com/tw/vl_searchbyid.php'

f_error = open("error.txt","a")
cur_path = os.getcwd() #得知目前路徑
files = os.listdir(cur_path)  
for file in files:
    if file !="" :
        fname=os.path.splitext(file)[0]
        param ={'keyword':fname}
        r = requests.get(cs_url, params = param)
        bs = BeautifulSoup(r.text,"html.parser")
        link=bs.find(id="video_jacket_img")
        if link != None :
            url=link.get('src')
            pngweb = urllib.request.urlopen(url)
            pngin = pngweb.read()
            with open(fname+".jpg","wb") as code:
                code.write(pngin)
        else :
            print(fname)
            f_error.writelines(fname+"\n")
    else :
        break
f_error.close()


