#This is Developed by Imperior Hackers
import os
import sys
from googletrans import Translator
os.system("clear")
os.system("figlet Translator | lolcat")
K = input("Do You Have Stable Internet Connection [Yes/No] :>> ")
if K == "No" or K == "no":
		os.system("exit")
		os.system("python3 os.py")
elif K == "Yes" or K == "yes":
	A = input("Enter Your Word/Text >> ")
	translator = Translator()
	result = translator.translate(A)
	print(result)
	D = input("Press Enter To continue")
	os.system("python3 os.py")
else: os.system("python3 os.py")
