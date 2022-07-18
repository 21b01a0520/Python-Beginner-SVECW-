'''5. Create a module 'Prime" to include the following functions.
a. isPrime(number)-returns boolean whether the given number is prime number or not.
b. isPalindromePrime(number)-returns boolean whether the given number is prime with palindromic prime.
c. isEmirp(number)-returns boolean whether the given number and its reversal number are also prime number.
d. MersennePrime(p)-returns 2p-1 value for given integer p if the given value is prime number.
e. printTwinPrimes(range)-prints all twin prime numbers below given range.'''


def isPrime(n):
    if(n==1):
        return False
    elif(n==2):
        return True
    else:
        for x in range(2,n):
            if(n%x==0):
               return False
        return True

def isPalindromePrime(n):
    flag=False
    rev=0
    num=n
    while(num>0):
        rem=num%10
        rev=(rev*10)+rem
        num=num//10
    if n==rev:
        flag=True
    if(n==1):
        return False
    elif(n==2):
        return True;
    else:
        for x in range(2,n):
         if(n%x==0):
           return False
         if flag==True:
             return True;
         else:
             return False


def isEmirp(n):
    flag=False
    rev=0
    num=n
    while(num>0):
        rem=num%10
        rev=(rev*10)+rem
        num=num//10
    if(isPrime(n)==True and isPrime(rev)==True):
        return True
    else:
        return False
def MersennePrime(n):
    if(isPrime(n)):
        return ((2**n)-1)
    else:
        return False
        


def printTwinPrimes(r):
    for i in range(2,r+1):
        for j in range(2,r+1):
          if isPrime(i) and isPrime(j) and j-i==2:
              print('(',i,',',j,')','are twin primes')



              
              
                     
              
