# coding=utf-8
###### LOGO #####
import os

os.system("clear")
#### colours ###
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'
W='\033[0;37m'
##############


###########÷÷÷#÷
print (S+'====================================================')
print (S+'            [1] '+R+'Masuk')
print (S+'            [2] '+R+'Masukin Token')
print (S+'=====================================================')
bm=raw_input(S+ 'Pilih? ')
if bm =='':
   print ("Pilih Yang Bener Sayang")
elif bm =='1':
     os.system("python2 .fb2.py")
elif  bm =='2':
     os.system("python2 .09091.py")
