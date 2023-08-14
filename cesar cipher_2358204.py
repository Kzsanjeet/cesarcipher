import os
def welcome():
    print("Welcome to the caesar cipher")
    print("This program encrypt and decrypt the text with caesae cipher.")
def enter_message():
    # making the enter message function to enter the message given by user#
    while True:
        user=input("Would you like to encrypt(e) or decrypt(d):").lower()
        if user != "e" and user != "d":
            print("Invalid Mode")
            continue
        elif user=="e":
            message = input("What message would you like encrypt:")
            break
        elif user == "d":
            message = input("What message would you like decrypt:")
            break
        message= message.upper()
    while True:
        try:
            shift=int(input("What is your shift number:"))
            break
        except ValueError:
                print("Invalid shift")
    return user,message,shift
def encrypt(message,shift):
    #using a function to encrypt message by given shift nunber.#
    e_result=""
    message = message.upper()
    for char in message:
        if char.isalpha():
            code=ord(char)
            code+=shift
            if code>ord('Z'):
                code-=26
            e_result+=chr(code)
        else:
            e_result+=char
    return e_result

def decrypt(message,shift):
    #using the decrypt function  to decrypt the message.#
    d_result = ""
    message=message.upper()
    for char in message:
        if char.isalpha():
            code = ord(char)
            code -= shift
            if code < ord('A'):
                code += 26
            d_result += chr(code)
        else:
            d_result += char
    return d_result

def process_file(filename, mode, shift):
    # using the function to encrypt or decrypt the code afte reading the file#
    try:
        with open(filename, 'r') as f:
           text = f.read()
        if mode == 'e':
            encrypted_text =""
            for char in text.upper():
                if char.isalpha():
                    encrypted_text+= chr(ord(char)+shift)
                else:
                    encrypted_text+=char
            write_message(encrypted_text)
            print(encrypted_text)
        elif mode=="d":
            decrypted_text==""
            for char in text.upper():
                if char.isalpha():
                    decrypted_text+=chr(ord(char)-shift)
                else:
                    decrypted_text+=char
            write_message(decrypted_text)
    except FileNotFoundError:
        print("File not found:",filename)
    
def is_file(filename):
    # creating the fucntion to see if file exists#
    return os.path.isfile(filename)

def write_message(text):
    #using the function to encrypt or decrypt the file and print to result.txt#
    with open("result.txt","w") as f:
        f.write(text)

def message_or_file():
    #cresting the function ask user for mode and whether to console or do it form file#
    while True:
        Vmode=['e','d']
        mode=input("Would you like to encrypt(e) or decrypt(d)?:").lower()
        while mode not in Vmode:
            print("Invalid mode.\n Enter again")
            mode=input("Would you like to encrypt(e) or decrypt(d)?:").lower()
            break
        while True:
            decode=input("Would you like to read form file(f) or console(c)?:").lower()
            if decode  not in ('f','c'):
                print("Invalid mode")
                decode=input("Would you like to read form file(f) or console(c)?:").lower()
            break
        while True:
            try:
                shift=int(input("Enter the shift number:"))
                break
            except ValueError:
                print("Invalid shift")
        if decode=="c":
            message=input("What message would you like to {}:".format(
                'encrypt' if mode=='e'else 'decrypt'))
            if mode=='e':
                eyn=encrypt(message,shift).upper()
                print(eyn)
            elif mode=='d':
                dyc=decrypt(message,shift).upper()
                print(dyc)
            elif decode=="f":
                print("Invalid shift")
            if decode=="c":
                message=input("what message would you like to {}?:".format(
                    'encrypt'if mode=='e' else'decrypt'))
                if mode=='e':
                    eyn=encrypt(message,shift).upper()
                    print(eyn)
                elif mode=='d':
                     decrypt(message,shift).upper()
                     dyc=decrypt(message,shift)
                     print(dyc)
        elif decode=='f':
            while True:
                filename=input("Enter the file name")
                if not is_file(filename):
                    print('file not found:',filename)
                    continue
                else:
                    process_file(filename,mode,shift)
                    print("printed to result.txt")
                    break
            break
        break
def main():
     welcome()
     while True:
        message_or_file()
        nextmessage=input('Would you like to encrypt or decrypt(y/n)?:').upper()
        if nextmessage not in ("N","Y"):
            print("Invalid")
        # nextmessage=input('Would you like to encrypt or decrypt(y/n)?:').upper()
        if nextmessage=="N":
             print('Thank you for using the prigram.goodbye')
             break
        

main()

    


            










        

