from cryptography.fernet import Fernet
from sys import exit

"""
This program has been created by Nitya,Mahendra,Shoab,Anand,Kushagra and Syam
"""


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

def main():
    print('''
         █████╗ ██╗   ██╗██████╗ ███████╗████████╗███████╗ ██████╗ 
        ██╔══██╗██║   ██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝ 
        ███████║██║   ██║██║  ██║███████╗   ██║   █████╗  ██║  ███╗
        ██╔══██║██║   ██║██║  ██║╚════██║   ██║   ██╔══╝  ██║   ██║
        ██║  ██║╚██████╔╝██████╔╝███████║   ██║   ███████╗╚██████╔╝
        ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝


            Please enter the number to the corrosponding option 

            ( If it's not in the same folder, specify the location. )

            1 --> Encode an audio file
            2 --> Decode an Text file
            3 --> exit 

            Enter your option   -->''', end = ' ')
    r=int(input(" "))

    if (r == 1):
        pos=input("\n            Enter the name of the file  :")
        encrypt(pos)
    elif(r ==2 ):
        pos=input("\n            Enter the name of the file :")
        kimg=input("\n           Enter the location of the key image : ")
        decrypt(pos,kimg)
    else:
        print("\n            Not now?, OK but play with me later")
        exit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n \n             Offoo! You chose to leave me...")
        