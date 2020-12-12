import requests,os,re
#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'
W='\033[0;37m'

try:
 os.system('clear')
 print ("Masukan Username")
 print ""
 print ""
 print ""
 u = raw_input(Y+'Masukkan username > ')
 url = 'https://www.facebook.com/'+u
 r = requests.get(url).text
 name = re.search('Title">(.*?)</', r).group(1).strip('| Facebook')
 id = re.search('profile/(.*?)" ', r).group(1)

 print B+'\nNAMA > '+R+name
 print B+'ID   > '+R+id+'\n'
 
except requests.exceptions.ConnectionError:
 	print 'Koneksi tidak ada'
except AttributeError:
	print 'Username tidak di temukan'
print input("KEMBALI?" )
os.system("python2 fb2.py")
