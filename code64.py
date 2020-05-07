import base64
import sys
import random


def base64_function(file_path,mode):
    mode=mode
    result=b""
    file_path=file_path

    random_n=random.randint(1,9999)

    #This option decode from base64.
    if mode == "decode":
    

        try:
            file1=open(file_path,"r") #File where the data is storaged...

        except FileNotFoundError:

            #if file is not found in the directory or path...

            print("File not found...")
            sys.exit()

        else:

            # Data extraction line by line into file_content list. 
            # With the file_content list length will also be possible to know the encryptation progress percent.

            file_content=file1.readlines()
            print(f"File length: {len(file_content)}")
            file1.close() #File object not neccessary at the moment, so it is closed. 

            file2=open(f"{random_n}code64.txt","w") #File where encrypted data will be writen...
                                                    #Random number + Prefixed "base64" for file name

            print("Decoding...")
            for i in file_content:
                bytes_data=i.encode() #before being encrypted, data has to be encoded from string to bytes. line by line, from the list.
                decoded_line=(base64.b64decode(bytes_data)).decode() #once in bytes, it is encrypted to base64 and turned back again to str
                file2.write(decoded_line) #encrypted data writen line by line in the file. 
                
            
            file2.close()
            print("\n")
            print("File decoded to base64")
            print("\n")

    elif mode == "encode":

        try:
            file1=open(file_path,"r") #File where the data is storaged...

        except FileNotFoundError:

            #if file is not found in the directory or path...

            print("File not found...")
            sys.exit()

        else:

            # Data extraction line by line into file_content list. 
            # With the file_content list length will also be possible to know the encryptation progress percent.

            file_content=file1.readlines()
            print(f"File length: {len(file_content)}")
            file1.close() #File object not neccessary at the moment, so it is closed. 

            file2=open(f"{random_n}code64.txt","w") #File where encrypted data will be writen...
                                                    #Random number + Prefixed "base64" for file name
            print("encoding...")
            for i in file_content:
                bytes_data=i.encode() #before being encrypted, data has to be encoded from string to bytes. line by line, from the list.
                encoded_line=(base64.b64encode(bytes_data)).decode() #once in bytes, it is encrypted to base64 and turned back again to str
                file2.write(encoded_line + "\n") #encrypted data writen line by line in the file. 
                
            file2.close()
            print("\n")
            print("File encoded to base64")
            print("\n")

"""
For base64 file encoding/decoding:

WINDOWS:
python code64.py <encode/decode> <file path> <algorithm>
python code64.py help

LINUX:
python3 code64.py <encode/decode> <file path> <algorithm>
python3 code64.py help

"""

main_title= """ 

  ____ ___  ____  _____ __   _  _   
 / ___/ _ \|  _ \| ____/ /_ | || |  
| |  | | | | | | |  _|| '_ \| || |_ 
| |__| |_| | |_| | |__| (_) |__   _|
 \____\___/|____/|_____\___/   |_|  
 ________________________________________________________________________

"""

print(main_title)

random_n=random.randint(1,9999)

if sys.argv[1] == "help":
    print("\n")
    print("python code64.py <encode/decode> <file path> --> For coding or decoding with base64")
    print("python code64.py help --> For showing this info")
    print("\n")

elif sys.argv[1] == "decode":

    if sys.argv[3] == "base64":

        base64_function(sys.argv[2],sys.argv[1])

   

elif sys.argv[1] == "encode":

    if sys.argv[3] == "base64":

        base64_function(sys.argv[2],sys.argv[1])

else:
    print("\n")
    print("python code64.py <code/decode> <file path> --> For coding or decoding with base64")
    print("python code64.py help --> For showing this info")
    print("\n")