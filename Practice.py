# Strings
#1. length of string
#using built in

lnstr = "madhav"
print(len(lnstr))

# using for loop
def findLen(lnstr1):
    m = 0 
    for i in lnstr1:
        m += 1
    print(m)
lnstr1 = "madhav"
# print(findLen(lnstr1))

# 1.3 using if else:

def findLen(str):
    if not str:
        return 0
    else:
        some_random_str = 'py'
        return ((some_random_str).join(str)).count(some_random_str) + 1
  
str = "madhav"
print(findLen(str))

# 1.4
def findLen(str):
    y = 0
    while str[y:]:
        y += 1
    return y

    # 

import re
d_string = 'The horror, the horror.'
print(len(re.findall('o', d_string)))
  
str = "madhav"
print(findLen(str))

#2 Count occurences characters in string

test_str1 = 'HI MY IS MADHAV, I AM RESIDING IN BANGALORE AND MY HOMETOWN IS ANANTAPUR'
record = {}
for char in test_str1:
    if char in record:
        record[char] += 1
    else:
        record[char] = 1
print(record)


# 
test_str = 'MADHAV RANGA NAIDU'
str_occur = {} 
for i in test_str: 
    if i in str_occur: 
        str_occur[i] += 1
    else: 
        str_occur[i] = 1
print(str_occur)

#

def count(s, c):
    res = 0
    for i in range(len(s)):
        if (s[i] == c):
            res += 1
    return res
str= "MADHAVA RANGA NAIDU"
c = 'A'
print(count(str, c))


# if else


#3 String slicing
String ='ELEPHANTEARS'
  
#3.1 Using slice constructor
s1 = slice(3)
s2 = slice(1, 5, 2) 
s3 = slice(-1, -12, -2)
  
print("String slicing") 
print(String[s1]) 
print(String[s2]) 
print(String[s3])

#3.2# Python program to demonstrate

# String slicing
String ='ELEPHANTEARS'

# Using indexing sequence
print(String[:3])
print(String[1:5:2])
print(String[-1:-12:-2])

print("\nReverse String")
print(String[::-1])

# 3.3 
str1 = "ELEPHANTEARS"  
slic = slice(0,10,3) # prints slice object  
slic2 = slice(-1,0,-3) # prints slice object  
# We can use this slice object to get elements  
str2 = str1[slic]  
str3 = str1[slic2] # prints elements in reverse order  
# Displaying result  
print(str2)  
print(str3)  

# 3.4 indices method

colors = ['red', 'green', 'blue', 'orange']

s = slice(0, 4, 2)
t = s.indices(len(colors))

for index in range(*t):
    print(colors[index])



#4 Swapping chars in string
# 4.1 