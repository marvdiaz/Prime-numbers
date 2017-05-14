# This program recieves an integer number input and 
# outputs a prime number input amout of times

import math

L = []
print()
m = int(input("Enter the number of Primes to compute: "))
print()
print("The first "+str(m)+" primes are:")

def isPrime(m,L):
   L = []
   for num in range(0,1000000):
      # prime numbers are greater than 1
      if len(L)<m:
         if num > 1:
             for i in range(2,num):
                 if (num % i) == 0:
                     break
             else:
                   L.append(num)
                   if (len(L)%10-1)==0 and len(L)>9:
                      print()
                   print(num, end=' ')
   print()

for num in range(1,m + 1):
# prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
          L.append(num)


isPrime(m,L)
print()
