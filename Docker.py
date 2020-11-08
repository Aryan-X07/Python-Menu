import os
print('''MENU LIST :
        1.Installation of  Docker
        2.Start Docker-Service
        3.Stop Docker-Service
        4.Search Docker-Image
        5.Downlod Docker-Image
        6.List all Launched Docker-OS
        7.List Running Docker-OS
        8.Start Docker-OS
        9.Stop Docker-OS
        10.Delete Docker-OS
        11.Delete All launched Docker-OS
        12.Install Docker-OS
        13.Get Docker-Image Terminal
        14.List All Downloaded Docker-Image
        15.About Docker
        16.Exit''')
while True:
    print("Select Your Choice :")
    a=input()
    if (a=="1"):
        os.system("yum install docker-ce --nobest")
    if (a=="2"):
        os.system("systemctl start docker")
        print("Docker-Service is running")
    if (a=="3"):
        os.system("systemctl stop docker")
        print("Docker-Service is stopped")
    if (a=="4"):
        print("Enter Image name to search :")
        b=input()
        os.system("docker search {}".format(b))
    if (a=="5"):
        print("Enter Image name to Download/Pull")
        c=input()
        os.system("docker pull {}".format(c))
    if (a=="6"):
        os.system("docker ps -a")
    if (a=="7"):
        os.system("docker ps")
    if (a=="8"):
        print("Enter Docker Os to start:")
        d=input()
        os.system("docker start {}".format(d))
    if (a=="9"):
        print("Enter Docker OS to stop:")
        e=input()
        os.system("docker stop {}".format(e))
    if (a=="10"):
        print("Enter Image Name to Delete:")
        f=input()
        os.system("docker rm {}".format(f))
    if (a=="11"):
        os.system("docker rm `docker ps -a -q`")
    if (a=="12"):
        print("Enter image name to install:")
        g=input()
        print("Give Name to Your Docker OS")
        osname=input()
        os.system("docker run -it --name {}  {}".format(osname,g))
    if (a=="13"):
        print("Enter Docker-OS Name to get Terminal:")
        h=input()
        os.system("docker attach {}".format(h))
    if (a=="14"):
        os.system("docker images")
    if (a=="15"):
        os.system("docker info")

    if (a=="16"):
        print("Exiting")
        exit()
