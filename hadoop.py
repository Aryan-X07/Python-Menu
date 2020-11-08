import os
print('''MENU LIST :
        1.Start namenode service
        2.Check report
        3.hadoop list
        4.Create the file
        5.To upload a file in hadoop
        6.To delete a file in hadoop
        7.Exit''')
while True:
    print("Select Your Choice :")
    a=input()
    if (a=="1"):
        os.system("hadoop-daemon.sh start namenode")
    if (a=="2"):
        b=input()
        os.system("hadoop dfsadmin -report")
        print("hadoop report")
    if (a=="3"):
        os.system("hadoop fs -ls /")
    if (a=="4"):
        print("Create the file")
        b=input()
        os.system("touch {} ".format(b))
    if (a=="5"):
        print("Enter the file name to upload:")
        c=input()
        os.system("hadoop fs -put {} // ".format(c))
    if (a=="6"):
        print("Enter the filename to delete:")
        d=input()
        os.system("hadoop fs -rm /{} ".format(d))
    if (a=="7"):
        print("Exiting")
        exit()
