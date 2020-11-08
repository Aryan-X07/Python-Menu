import os
print('''MENU LIST :
        1.AWS CLI-2 Version
        2.Create a Key Pair
        3.Create a security group 
        4.Launch EC-2 Instance
        5.Create an EBS Volume
        6.Attach EBS Volume to Ec-2 Instance
        7.Exit''')
while True:
    print("Select Your Choice :")
    a=input()
    if (a=="1"):
        os.system("aws --version")
    if (a=="2"):
        print("Enter Key Name:")
        b=input()
        os.system("aws ec2 create-key-pair --key-name {}".format(b))
    if (a=="3"):
        print("Enter Security-Group Name:")
        c=input()
        print("Give Description Here:")
        d=input()
        os.system("aws ec2 create-security-group --group-name {} --description \"{}\" ".format(c,d))
    if (a=="4"):
        print("Enter Image-ID")
        e=input()
        print("Enter Instance-Type")
        f=input()
        print("Enter Key-Pair Name")
        g=input()
        print("Enter Security-Group ID:")
        h=input()
        os.system("aws ec2 run-instances --image-id {} --instance-type {} --count 1 --subnet-id subnet-601c1508 --key-name {} --security-group-ids {} ".format(e,f,g,h))
    if (a=="5"):
        print("Enter the Zone Name:")
        i=input()
        os.system("aws ec2 create-volume --availability-zone {} --size 1 --volume-type gp2".format(i))
    if (a=="6"):
        print("Enter Instance-ID:")
        j=input()
        print("Enter Volume-ID:")
        k=input()
        os.system("aws ec2 attach-volume --instance-id {} --volume-id {} --device /dev/sdk".format(j,k))
    if (a=="7"):
        print("Exiting")
        exit()
