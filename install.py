#--- Color  ---#
N = '\033[0m'    # Normal
Y = '\033[1;33m' # Yellow
R = '\033[1;31m' # Red
G = '\033[1;32m' # Green
W = '\033[1;37m' # White
D = '\033[1;9;31m'  # DelBold
#---        ---#
import os
import sys
import time
os.system("clear")

print("%s DARK OS INSTALLATION WINDOW %s" % (R,N))

print("%s This programme is only made for Android Terminal [Termux] It only works when executed only in Termux. The Develoder of This programme is Not Responsible for any illegal use of this script by the USER. so enjoy Using this Os . For more Info refer to the README.md %s" % (R,N))
print("")
print("%s=================================================%s" % (R,N))
print('''%s DEVELOPER:- Imperior Hackers
	    Version:- v1.1
	    Name :- DARK OS
	    Requirements:- Android OS (above v5.0)
			  2GB RAM OR ABOVE 
			  16GB ROM OR ABOVE
      %s''' % (G,N))
print("%s=================================================%s" % (R,N))
time.sleep(3)
a=input("would you like to install DARK OS {Yes/No} :-  ")
if a=="Yes" : os.system("bash install.sh")
if a=="No"  : sys.exit()

