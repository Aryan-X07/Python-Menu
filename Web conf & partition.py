import os


while True:
	print("\n")
	print("press :1 to look for configuration of web server menu")
	print("press :2 to look for partition menu")
	print("press :3 to Quit")
	print("\n")

	print("enter your choice:" , end='')
	p=input()
	print(p)

	if int(p) == 1:
		while True:
			print("\n")
			print("press :1 to install web server")
			print("press :2 to see web pages")
			print("press :3 to start web service")
			print("press :4 to run the webpage on localhost")
			print("press :5 to stop web service")
			print("press :6 to check the status of web service")
			print("press :7 to exit from web server menu")
			print("\n")

			print("enter your choice:" , end='')
			n=input()
			print(n)

			if int(n) ==1:
				os.system("yum install httpd")
			if int(n) ==2:
				os.system("ls /var/www/html")	
			if int(n) ==3:
				os.system("systemctl start httpd")
			if int(n) ==4:
				a=input("enter webpage name:")
				os.system("firefox http://localhost/{}".format(a))
			if int(n) ==5:
				os.system("systemctl stop httpd")
			if int(n) ==6:
				os.system("systemctl status httpd")
			elif int(n) ==7:
				break
		else:
			print("doesnt support")
			#os.system("clear")



	elif int(p) == 2:
		while True:
			print("\n")
			print("Welcome to partition menu")
			print("press :1 to see all the which storage are attached to operating system")
			print("press :2 to create partition")
			print("press :3 to format")
			print("press :4 to mount")
			print("press :5 to get block details of partition")
			print("press :6 to exit")
			print("\n")

			print("enter your choice:" , end='')
			n=input()
			print(n)
			if int(n) == 1:
				os.system("fdisk -l")
			if int(n) == 2:
				c=input("Enter the name of storage which you want to format:")
				os.system("fdisk /dev{}".format(c))
			if int(n) == 3:
				a=input("Enter the name of storage which you want to format:")
				os.system("mkfs.ext4  /dev{}".format(a))
			if int(n) == 4:
				b=input("enter name of storage which you want to mount")
				os.system("mount /dev{} /fold".format(b))
			if int(n) == 5:
				os.system("lsblk")			
			if int(n) ==6:
				break

			else:
				print("")
	elif int(p) == 3:
		break
	else:
		print("dont support")

