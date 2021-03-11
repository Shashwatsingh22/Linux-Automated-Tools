import os
import function 


os.system("tput setaf 1")
function.render("Logical Volume Management","big",0)
os.system("tput setaf 7")

os.system("tput setaf 2")
print("    ************** Main Menu****************  ")

while True:

    print("""\t\t\t
          Press 1: Number Of Hardisk Inserted In the Machine.
          Press 2: Mounted Disk to Some Folder.
          Press 3: Physical Volume.
          Press 4: Volume Group.
          Press 5: Logical Volume.
          Press 6: Format & Mount.
          Press 7: Extend The Size and Format the LV On the Fly.
          Press 8: Exit.
          """)
    print("Enter the Choice: ", end=" ")
    ch=input()

    if int(ch) == 1:
        output = os.system("fdisk -l")
        print(output)

    elif int(ch) == 2:
        output = os.system("df -hT")
        print(output)
    
    elif int(ch) == 3:
        while True:
            print(" ******* Physical Volume ******* ")
            function.sh_menu()
            choice = input()

            if int(choice)==1:
                fold_name=input("Enter the Folder Name of the HDD (Like, /dev/sdc): ")
                output = os.system("pvcreate "+fold_name)
                print(output)

            elif int(choice)==2:
                output=os.system("pvdisplay")
                print(output)

            elif int(choice)==3:
                fold_name=input("Enter the Fold Name of Hdd : ")
                output=os.system("pvdisplay "+fold_name)
                print(output)

            else:
                break    
    
    elif int(ch) == 4:
        while True:
            print(" ******** Volume Group ******** ")
            function.sh_menu()
            choice=input()

            if int(choice)==1:
                name_vg = input("Enter the Name for the VG:")
                n=input("Number of the PV wants to attach with vg :")
                list_fold_name_hdd=[]
                i=1;
                while(n):
                    list_fold_name_hdd.append(input("Enter the Name Of "+i+"Fold Name :"))
                    n=n-1;
                    i=i+1;

                output=os.system("vgcreate "+name_vg+" "+list_fold_name_hdd[0]+" "+list_fold_name_hdd[1])
                print(output)

            elif int(choice)==2:
                print(os.system("vgdisplay"))

            elif int(choice)==3:
                name_vg = input("Enter the Name of the VG:")
                print(os.system("vgdisplay "+name_vg))

            else:
                break    

    elif int(ch) == 5:
        while True:
            print("  ********** Logical Volume ********* ")
            function.sh_menu()

            choice=input()
            if int(choice)==1:
                size=input("How Much Size You Wants to Take from VG ?(In Complete Manner like 500M or 4G)")
                name_lv=input("Enter the Name of LV :")
                name_vg=input("Enter the Name of VG :")
                print(os.system("lvcreate --size "+ size + " --name "+name_lv+" "+name_vg))

            elif int(choice)==2:
                print(os.system("lvdisplay"))

            elif int(choice)==3:
                name_lv=input("Enter the Name of LV :")
                name_vg=input("Enter the Name of VG :")
                print(os.system("lvdisplay "+name_vg+"/"+name_lv))

            else:
                break    

    elif int(ch)==6:

        while True:
            print(" ********** Format & Mount ********* ")
            print("From Here Find The LV Path : ")
            name_lv=input("Enter the Name of LV :")
            name_vg=input("Enter the Name of VG :")
            print(os.system("lvdisplay "+name_vg+"/"+name_lv))
            lv_path=input("Enter the LV path: ")
            print("""\t\t
                  Press 1: Fromat.
                  Press 2: Mount.
                  \n Enter the Choice: """,end=" ")
            choice=input()
            
            if int(choice)==1:
                print(os.system("mkfs.ext4 "+lv_path))

            elif int(choice)==2:
                print("First We Need Creat an Folder For Mount !")
                dir=input("Enter the Folder name with Suitable path (like /drive")
                os.system("mkdir "+dir)
                os.system("mount "+ lv_path +" "+dir)
                print(os.system("df-h"))

            else:
                break

    elif int(ch)==7:
        print("From Here Find The LV Path : ")
        name_lv=input("Enter the Name of LV :")
        name_vg=input("Enter the Name of VG :")
        print(os.system("lvdisplay "+name_vg+"/"+name_lv))
        lv_path=input("Enter the LV path: ")
        
        size=input("How Much You to increase the Size ?")
        print(os.system("lvextend --size +"+size+" "+lv_path))

        print("As You See that LV Size is Increases ! /n"+os.system("lvdisplay "+name_lv))

        print("But Here Drive Size Is not Increases Becoz the Extended Size is Not Formated !\n"+os.system("df -h"))

        print("Formating the Extended Size !\n"+os.system("resize2fs "+lv_path))

        print("Now As You See that Your Drive Got the Extended Size too !\n"+os.system("df -h"))

    else:
        break    