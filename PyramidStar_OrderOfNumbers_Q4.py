'''4.(a)Write a Python program to print pyramid star pattern using a for loop up to given number of rows.
This python example uses multiple for loop nested inside another to print thepyramid pattern.'''

def row(n):
   space=n-1
   for i in range(n):
     for j in range(space):
       print("",end=' ');
     for k in range(i+1):
        print("*",end=' ');
     print("\n")
     space-=1
n= int(input("Enter the number of rows : "))
row(n)
print("\n")



'''4.(b)Write a python program to detremine the direction ('increasing' or 'decreasing') of monotonic sequence numbers.'''
def order(lst):  
   cnti=0
   cntd=0
   for i in range(len(lst)-1):
     if(lst[i]<lst[i+1]):
        cnti+=1
     elif(lst[i]>lst[i+1]):
         cntd+=1
     else:
       pass
   if(cnti==(len(lst)-1)):
         print("increasing")
   elif(cntd==(len(lst)-1)):
         print("decreasing")
   else:
    print("neither increasing nor decreasing")
 
n = int(input("Enter number of elements: "))
lst = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
print('The list is : ',lst)
order(lst)
