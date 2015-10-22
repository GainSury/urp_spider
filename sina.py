import urllib2
import requests
import HTMLParser  
import urlparse
import cookielib  
import string  
import re 
from PIL import ImageEnhance
from PIL import Image
import urllib
import StringIO
import os
from bs4 import BeautifulSoup




usr = "2404798534@qq.com"
passw = "sina3216"
login_url = "http://login.weibo.cn/login/"
traget_url = "http://login.weibo.cn/login/?ns=1&revalid=2&backURL=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=4"
sina = requests.session()
index = sina.get(login_url)
#################################################
sina_data = {'mobile':usr,
             "password_3616":"sina3216",
             "remember":"on",
             "backURL":"http%3A%2F%2Fweibo.cn%2F",
             "backTitle":"%E5%BE%AE%E5%8D%9A",
             "tryCount":"",
             "vk":"3312_bac4_1775844356",
             "submit":"%E7%99%BB%E5%BD%95"}
header = { 'User-Agent' : 'spider' }
#####################################################3
response = sina.post(traget_url,data = sina_data,headers = header)
soup = BeautifulSoup(response.text, 'html.parser')
