import os
import sys
import time
import urllib
from core.core import *
#This programme is only made for Android Terminal [Termux] It only>
#--- Color  ---#
N = '\033[0m'    # Normal
Y = '\033[1;33m' # Yellow
R = '\033[1;31m' # Red
G = '\033[1;32m' # Green
W = '\033[1;37m' # White                                           D = '\033[1;9;31m'  # DelBold
#---        ---#
os.system("clear")
p=('''%s
  ██████╗  █████╗ ██████╗ ██╗  ██╗     ██████╗ ███████╗
  ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ██╔═══██╗██╔════╝
  ██║  ██║███████║██████╔╝█████╔╝     ██║   ██║███████╗
  ██║  ██║██╔══██║██╔══██╗██╔═██╗     ██║   ██║╚════██║
  ██████╔╝██║  ██║██║  ██║██║  ██╗    ╚██████╔╝███████║
  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝
==============================================================
CODED BY :- IMPERIOR HACKERS| SPECIAL THANKS TO ALL DEVELOPERS
==============================================================

%s''' % (G,Y))
print(p)
print('''%s   [1] Terminal           [2] Ngrok Starter

   [3] Downloader         [4] Metasploit-Framework

   [5] Music              [6] call/Dialer

   [7] System Info  	  [8] Apk Moding/Payload

   [9] Internal Storage   [10] Help /Author Info

   [11] Translator	  [12] T-Speak

   [13] Date/Calender     [14] Termux-Lazyscript-Master

   [15] SMS		  [16] Phishing Attack

   [17] Command HELP 	  [18] EXIT%s''' % (Y,N))

print("")
print("")
IT = input(" Enter Your Option >> ")
if IT.strip() == "01" or IT.strip() == "1":
	os.system("clear")
	os.system("figlet Terminal | lolcat")
	print("%s==================================%s" % (G,N))
	print("%s   HERE IS YOUR TERMINAL %s" % (R,N))
	print("%s==================================%s" % (G,N))
elif IT.strip() == "02" or IT.strip() == "2":
	ngrok()
elif IT.strip() == "03" or IT.strip() == "3":
	lzm()
elif IT.strip() == "04" or IT.strip() == "4":
	msf()
elif IT.strip() == "05" or IT.strip() == "5":
	Music()
elif IT.strip() == "06" or IT.strip() == "6":
	call()
elif IT.strip() == "07" or IT.strip() == "7":
	system()
elif IT.strip() == "08" or IT.strip() == "8":
	hackapk()
elif IT.strip() == "09" or IT.strip() == "9":
	internal()
elif IT.strip() == "10":
	os.system("clear")
	os.system("cat README.md")
	SA = input("Press Enter To exit >> ")
	os.system("python3 os.py")
elif IT.strip() == "11":
	Trans()
elif IT.strip() == "12":
	Tspeak()
elif IT.strip() == "13":
	date()
elif IT.strip() == "14":
	TLM()
elif IT.strip() == "15":
	sms()
elif IT.strip() == "16":
	phish()
elif IT.strip() == "17":
	print("")
	print("%s To Find Command Help. Type:- man [command]%s" % (G,N))
elif IT.strip() == "18":
	exit()
else:
	print("%s<------------------WRONG---INPUT------------------>%s" % (R,N))
	time.sleep(3)
	os.system("python3 os.py")
