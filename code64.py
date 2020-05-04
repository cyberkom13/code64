import base64
import sys
import random


"""
For base64 file encoding/decoding:

WINDOWS:
python base64coder.py <encode/decode> <file path>
python base64coder.py help

LINUX:
python3 base64coder.py <encode/decode> <file path>
python3 base64coder.py help


"""

random_n=random.randint(1,9999)

if sys.argv[1] == "help":
    print("\n")
    print("python base64coder.py <encode/decode> <file path> --> For coding or decoding with base64")
    print("python base64coder.py help --> For showing this info")
    print("\n")

elif sys.argv[1] == "decode":

    #This options decode from base64.

    try:
        file1=open(sys.argv[2],"r") #File where the data is storaged...

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

        file2=open(f"{random_n}base64.txt","w") #File where encrypted data will be writen...
                                                #Random number + Prefixed "base64" for file name

        print("Decoding...")
        for i in file_content:
            bytes_data=i.encode() #before being encrypted, data has to be encoded from string to bytes. line by line, from the list.
            decoded_line=(base64.b64decode(bytes_data)).decode() #once in bytes, it is encrypted to base64 and turned back again to str
            file2.write(decoded_line + "\n") #encrypted data writen line by line in the file. 
            
        
        file2.close()
        print("\n")
        print("File decoded")
        print("\n")

elif sys.argv[1] == "encode":

    # Exactly the same than decoding but encoding. 

    try:
        file1=open(sys.argv[2],"r")

    except FileNotFoundError:
        print("File not found...")
        sys.exit()

    else:

        file_content=file1.readlines()
        print(f"File length: {len(file_content)}")
        file1.close()

        file2=open(f"{random_n}base64.txt","w")

        print("Encoding...")

        for i in file_content:
            bytes_data=i.encode() #from string to bytes
            encoded_line=(base64.b64encode(bytes_data)).decode()
            file2.write(encoded_line +"\n")
        
        file2.close()
        print("\n")
        print("File encoded")
        print("\n")

else:
    print("\n")
    print("python base64coder.py <code/decode> <file path> --> For coding or decoding with base64")
    print("python base64coder.py help --> For showing this info")
    print("\n")