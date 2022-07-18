'''3. (a)Write function "remove_duplicates" which takes a string argument and returns a string which is the same as the argument except only
the first occurance of each letter is present.Make a function case sensitive.'''

from collections import OrderedDict
string = input("Please enter a string..")

def remove_duplicates1(string):
    new_string="".join(OrderedDict.fromkeys(string))
    if new_string:
        return(new_string,len(string)-len(new_string))
    else:
        print("Please provide only alphabets")

s=remove_duplicates1(string)
print(string,'after duplicates removed ordered is:',s)

def remove_duplicates2(string):
    new_string="".join(set(string))
    if new_string:
        return(new_string,len(string)-len(new_string))
    else:
        print("Please provide only alphabets")

s=remove_duplicates2(string)
print(string,'after duplicates removed unordered is:',s,'\n\n')




#3. (b)Write a function mult_lists(a, b) that takes two lists of the numbers of the same length, and returns the sum of the products of the corresponding elements of each.


l1 = []
l2 = []

while(True):
    n = int(input("Enter number of elements for list1 : "))
    m = int(input("Enter number of elements for list2 : "))
    if(n!=m):
        print("enter same lengths for the lists")
    else:
        break
print("Enter elements into List1:")
for i in range(0,n):
        ele=int(input())
        l1.append(ele)

print("Enter elements into List2:")
for i in range(0,m):
        ele=int(input())
        l2.append(ele)
print("List1 is",l1,"List2 is",l2)
def mult_lists(a,b):
        product = [i*j for i, j in zip(a,b)]
        print(product)
        return sum(product)
print("The sum of the products of corresponding elemenyts is:",mult_lists(l1,l2),'\n\n')



#3. (c)Write a function called flatten_list that takes as input a list which maybe nested and returns a non nested list with all the elements of the input list.

def flatten_list(n_list):
    result_list = []
    if not n_list:
        return result_list
    stack = [list(n_list)]
    print('stack:',stack)
    while stack:
        c_num = stack.pop()
        print('c_num:',c_num)
        next = c_num.pop()
        print('next:',next)
        if c_num:
            stack.append(list(c_num))
        if isinstance(next, list):
            if next:
                stack.append(list(next))
        else:
            result_list.append(next)
        print('stack:',stack)
    result_list.reverse()
    return result_list
n_list=[0,10,[20,30],40,50,[60,70,80],[90,100,110,120]]
print("Original list:",n_list)
print("\nFlatten list: ",flatten_list(n_list))

