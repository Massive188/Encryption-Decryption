import keyword
from cryptography.fernet import Fernet


print("Would you like to encrypt or decrypt")

print("A: Encrypt")
print("B: Decrypt")

decide = input("What is your choice:")
print(decide)

class encryption:
   if decide == "A" or "a":
      def e_func():
      
            print(decide)
            #key generation 
            key = Fernet.generate_key()

            #string the key in a file 
            with open('filekey.key', 'wb') as filekey:
               filekey.write(key)
               
            #opening the key
            with open('filekey.key','rb') as filekey:
               keying = filekey.read()
               
            #using the generated key
            fernet = Fernet(keying)

            #opening the original file to encrypt
            with open('words.csv', 'rb') as file:
               original = file.read()

            # encrypting the file
            encrypted = fernet.encrypt(original)

            # Opening the file in write mode and 
            #writing the encrypted data 
            with open('words.csv', 'wb') as encrypted_file:
               encrypted_file.write(encrypted)
               
 # use import os and declare os.remove('filename') to remove the current file if necessary.
 # otherwise, I will start creating the gui and update this project a bit further.
 
      e_func()
# P.S: i know this code looks pretty messed up
if decide == "B" or "b":
   class decryption(encryption):
      def d_func():  
            print("File has been decrypted") 
            # using the key
            object_fernet = Fernet(keying)
            
            # opening the encrypted file 
            with open('words.csv', 'rb') as e_file:
               encrypted = e_file.read()
            
            # decrypting the file
            decrypted = object_fernet.decrypt(encrypted)
            
            #opening the file in write mode and 
            #writing the decrypted data 
            with open('nba.csv', 'wb') as d_file:
               d_file.wirte(decrypted)
      d_func()
