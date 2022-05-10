##1. Table of the given number##
def table(num):
    for i in range(1,11):
        print(num,'x', i, '=', num*i)
no = int(input("enter any number for multiplication table: "))
table(no)

#2(a) sum all the numbers in a list
list1 = [11, 5, 17, 18, 23]

def sumofList(l,s):
   if (s == 0):
    return 0
   else:
     return l[s - 1] + sumofList(l, s - 1)
   
total = sumofList(list1, len(list1))
 
print("Sum of all elements in given list: ",total)

#2(a) sum all the numbers in a Tuple
l1 = [(1, 6), (3, 4), (5, 8)]
print ("The original list is : " + str(l1))
res = [sum(i) for i in zip(*l1)]
print ("The position summation of tuples  : " + str(res))

#3 - Multiplication of  all the numbers in a list
def mul(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(mul([8, 2, 3, 1, 7]))

#3(a)Multiplication of numbers in tupple
def mutiple_tuple(nums):
    temp = list(nums)
    product = 1 
    for x in temp:
        product *= x
    return product

nums = (4, 3, 2 ,1,8)
print ("Original Tuple: ")
print(nums)
print("Product of given tuple is :",mutiple_tuple(nums))


# 4.Accepts a string and calculate the number of upper-case letters and lower case  letters

def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])
string_test(str(input('Enter your String with Upper n Lower case to count upper and Lower chars: ')))

# 5. Take a list and return a new list with unique elements of the first list

def unique_list(l):
    x = []
    for a in l:
     if a not in x:
      x.append(a)
    return x

print(unique_list([1,2,3,3,3,3,4,5]))

# 7.determine whether a given string is Palindrome

string = "ROTATOR";  
flag = True;   
string = string.lower();  
for i in range(0, len(string)//2):  
    if(string[i] != string[len(string)-i-1]):  
        flag = False;  
        break;  
if(flag):  
    print("Given string is palindrome");  
else:  
    print("Given string is not a palindrome");  

# 6. Print given Pascal's triangle

def printPascal(n) :
    
    for line in range(0, n) :
         
        for i in range(0, line + 1) :
            print(binomialCoeff(line, i),
                " ", end = "")
        print()
def binomialCoeff(n, k):
    result = 1
    if (k > n - k):
        k = n - k 
    for i in range(0, k):
        result = result * (n - i)
        result = result // (i + 1)
    return result

n = 10
printPascal(n)

# 8.check whether a number falls in a given range

def test_range(numb):
    if numb in range(1,10):
        print( " %s is in the range"%str(numb))
    else :
        print("The number is outside the given range.")
test_range(5)