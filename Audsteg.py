from cryptography.fernet import Fernet
from sys import exit
from os import system as sus 
from os import name as nam

G = '\033[92m'
Y = '\033[93m' 
B = '\033[94m'  
R = '\033[91m'  
W = '\033[0m' 



"""
This program has been created by Nitya,Mahendra,Shoab,Anand,Kushagra and Syam
"""
def clean():
    if(nam == 'posix'):
        sus("clear")
    else:
        sus("cls")

def encrypt(x):
    key=Fernet.generate_key()
    fernet=Fernet(key)


    
    fernet=Fernet(key) 
    with open('key.png','wb') as filekey: 
        filekey.write(key)

    with open(x,'rb') as file:
        orginalaudio=file.read()

    encrypted=fernet.encrypt(orginalaudio)

    with open ('encryptedata.txt','wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt(x,y):
    with open(y,'rb') as filekey:
        key=filekey.read()

    fernet=Fernet(key)

    with open(x,'rb') as enc_file:
        encrypted=enc_file.read()

    decrypted=fernet.decrypt(encrypted)

    with open('decrypted.mp3','wb') as dec_file:
        dec_file.write(decrypted)


def encryptmenu():
    file=" "
    while True:
        inp=input(B+"\nEncrypt >> "+W)
        listed=inp.split()
        if(listed[0] == "file"):
            file=listed[1]
        elif(listed[0] == "run"):
            encrypt(file)
            print(G+"\n File is been encrypted "+ W)
            res=1
            return

        elif(listed[0]== 'clear'):
            clean()
        elif(listed[0] =="ls" or listed[0]=="help"):
            print(""" \n

                        Help Menu:

                file <filename>  <-- to set the file to be encoded
                run                  <-- to encrypt the audio file

                 """)

        elif(listed[0] == "show"):
            print("\n   Filename :  {}".format(file))
        else:
            print("\n Still bruuuh , 'help' ")
    




def decryptmenu():
    file=" "
    key=" "
    while True:
        inp=input(B+"\nDecrypt >> "+W)
        listed=inp.split()
        if(listed[0] == "file"):
            file=listed[1]
        elif(listed[0] =="key"):
            key=listed[1]
        elif(listed[0] == "run"):
            decrypt(file,key)
            print(G+"\n File is been decrypted "+ W)
            res=1
            return

        elif(listed[0]== 'clear'):
            clean()
        elif(listed[0] =="ls" or listed[0]=="help"):
            print(""" \n

                        Help Menu:

                file <filename>  <-- to set the file to be decrypted
                key <keyname>    <-- to set the key for decryption
                run                  <-- to encrypt the audio file

                 """)

        elif(listed[0] == "show"):
            print("\n   Filename :  {}".format(file))
            print("\n   Key      :  {}".format(key))
        else:
            print("\n Still bruuuh , 'help' ")
    

def banner(x):
    if (x == 0):
        print("\n\n")
        print(R+"      █████╗ ██╗   ██╗██████╗ ███████╗████████╗███████╗ ██████╗    "+W)
        print(R+"     ██╔══██╗██║   ██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝    "+W)
        print(R+"     ███████║██║   ██║██║  ██║███████╗   ██║   █████╗  ██║  ███╗     "+W)
        print(R+"     ██╔══██║██║   ██║██║  ██║╚════██║   ██║   ██╔══╝  ██║   ██║    "+ W)
        print(R+"     ██║  ██║╚██████╔╝██████╔╝███████║   ██║   ███████╗╚██████╔╝"+W)
        print(R+"     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝"+ W)
        print("\n\n\n")

def main():
    k=0
    while True:
        banner(k)
        s=input(G+"\n>>> "+W)
        listed=s.split()
        if(listed[0] == "cd" or listed[0] == "goto"):
            if(listed[1] == "encrypt"):
                encryptmenu()
                k=1
            elif(listed[1] == "decrypt"):
                decryptmenu()
                k=1
        elif(listed[0] == "exit"):
            print(Y+"\n Bye Bye "+W)
            exit()
        elif(listed[0] =="ls" or listed[0] =="help"):
            print(''' \n 

                         Help Menu: 
            
            clear to clear the 

            to access Encrypt function type " cd encrypt " in prompt 

            to access Decrypt Function type " cd decrypt " in prompt         

            ''')
            k=1
        elif(listed[0] == "clear"):
            clean()
            k=0
        else:
            print(Y+"""\n You're still making mistakes with your spelling! You have embarrassed the entire world.
                     Atleast learn to type help.Go Learn Englisss """+W)
            k=1


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Y+"\n \n             Offoo! You chose to leave me..."+W)
    
    except:
        exit()
