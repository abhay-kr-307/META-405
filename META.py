#coding=utf-8
import os, sys, platform
os.system('rm -rf METAX')
os.system('git pull')
try:
    if sys.argv[1]=='update':
        os.system('rm -rf METAX')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('METAX'):
        os.system('curl -L https://github.com/abhay-kr-307/META-405/blob/main/METAX?raw=true -o METAX')
        os.system('chmod 777 METAX;./METAX')
    else:
        os.system('chmod 777 METAX;./METAX')
