'''Write a test program to import the prime module and perform the following operations using the functions of prime module
prints first 100 prime numbers
prints first 100 Palindrome prime numbers
prints first 100 Emirp numbers
prints all Mersenne prime numbers for the p value below 32
prints all twin prime numbers below 1000'''

import prime
print('The first 100 prime numbers are:')
for i in range(2,101):
    if(prime.isPrime(i)):
        print(i,end=' ')

print('\nThe first 200 palindrome prime numbers are:')
for i in range(2,201):
    if(prime.isPalindromePrime(i)):
        print(i,end=' ')

print('\nThe first 100 emirp numbers are:')
for i in range(2,101):
    if(prime.isEmirp(i)):
        print(i,end=' ')

print('\nMersenne prime numbers for the p value below 32:')
for i in range(2,33):
    if(prime.MersennePrime(i)):
        print(i,end=' ')

print('\nTwin prime numbers numbers below 1000:')
prime.printTwinPrimes(1000)

