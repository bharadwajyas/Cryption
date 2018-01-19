###############################################################################################################
#This Code takes an SHA hash and a password file as an input,find's out what is the hash version and starts
#brute forcing it to crack the hash.However sha384,sha512 are a bit slow according to the processing of the
#system.The main authors of this code is Satyam Dubey and Yash Bharadwaj.If you find any bug or encounter any
#error feel free to email at offpy0987@gmail.com
###############################################################################################################

#!/usr/bin/python

import hashlib
def h51():
  counter=1
  for p in pw_file:
     filesha = hashlib.sha512(p.strip()).hexdigest()
     print 'Trying password no.%d : %s'%(counter,p.strip())
     counter = counter+1
     if filesha == ur_hash:
         print 'Hell yeah!! \n[+]Password Found: \n password is %s' %p
         break
     else:
         print '\n[-]Password not found.'

def h38():
  counter=1
  for p in pw_file:
     filesha1 = hashlib.sha384(p.strip()).hexdigest()
     print 'Trying password no.%d :%s'%(counter,p.strip())
     counter = counter+1

     if filesha1 == ur_hash:
         print 'Hell yeah!! \n[+]password found. \n password is %s' %p
         break
     else:
         print '\n [-]Password not found'

def h25():
  counter=1
  for p in pw_file:
     filesha2 = hashlib.sha256(p.strip()).hexdigest()
     print 'Trying password no.%d :%s'%(counter,p.strip())
     counter = counter+1

     if filesha2 == ur_hash:
         print 'Hell yeah!! \n[+]password found. \n password is %s' %p
         break
     else:
         print '\n [-]Password not found'

def h22():
  counter=1
  for p in pw_file:
     filesha3 = hashlib.sha224(p.strip()).hexdigest()
     print 'Trying password no.%d:%s'%(counter,p.strip())
     counter = counter+1

     if filesha3 == ur_hash:
         print 'Hell yeah!! \n[+]password found. \n password is %s' %p
         break
     else:
         print '[-]Password not found'


def main():
 global pw_file,counter,ur_hash
 ur_hash=raw_input('Enter the SHA hash->')
 pass_file=raw_input('Enter pass file->')
 ln=int(len(ur_hash))
 try:
     pw_file=open(pass_file,'r')
 except:
     print '\n File not found'
     quit()
 if ln==128:
     print'[+]Found SHA 512 hash'
     h51()
 elif ln==96:
     print'\n[+]Found SHA 384 hash'
     h38()
 elif ln==64:
     print'\n[+]Found SHA 256 hash'
     h25()
 else:
     print'\n[+]Found SHA 224 hash'
     h22()
if __name__ == "__main__":
     main()
