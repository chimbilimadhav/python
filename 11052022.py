#  using while loop------------------------

list1 = [1,2,3,4,5,6]

list2 =len(list1)

i = 0

while i < list2:
    print(i)
    i+=1

#1.2 using for loop----------------------

list1 = [2,4,6,7,8,10]

for i in list1:
    print(i)
    i+=1

#disply only even  numbers-------------------

list_even = [2,44,3,12,41,47,33,30,6,8,10]

for each in list_even:
    if (each) %2 == 0:
        print(each)

#Disply elements by index wise------------------

list_index = [2,3,-4,6,-2,1,-7,4]

for each in list_index:
    if each >0:
        print("+Ve number", each)
    else:
        print("-ve number",each)


#Information about list (len),(count),(index), Function-------------------



list1 = [1,2,4,5,4,6,8,9,10,4,23,5]

x = list1.count(4)
print("The lenght of the list is",len(list1))
print("count of charecters is",x)
print("Index of the charecter is ",list1.index(4))


#append Method----------

list1 = [5,4,6,8,9,10,4,23,5]

list1.append(22)
print(list1)

  
#insert Method---------------

list1 = [5,4,6,8,9,10,4,23,5]

print(list1)
list1.insert(5,-11)
print(list1)

#extend method adds all the elements of an iterable (list,tuple,string) to the end of the list.

list1 = [1,4,5]
list2 = [2,6,5,7]

list2.extend(list1)

print("after the Extend method",list2)


#remove-------------------------------

#Remove() method Removes the first matching element from the list

list1 = [1,4,5,2,6,4,7,6]

list1.remove(6)
print(list1)

#pop()--------------------
#pop() method will removes the given index from the list and returns the  removed item

list1 = [1,4,5,2,6,4,7,6]
list1.pop(1)
print(list1)


#pop() removes the value by indexing 




#reverse() It reverse the Sequance of a list 

list1 = [1,4,5,2,6,7,6]
list1.reverse()
print(list1)



#sort() method sorts the items of a list in ascending or descending order.

list1 = [1,4,5,2,6,7,6]
list1.sort()
print(list1)


#Aliasing and Cloning of List objects:----------------------------
c = [21,23,20]
d = [21,23,20]

#1
print(c == d) #true
print(c is d) # false

#2
c == d
print(c == d) #true
print(c is d) #true





#slicing is taking part of the statement
#ex 1
list_b = (1,2,6,7,3,4,5,6,8,9,10)
x = slice(4)
print(list_b[x])

#ex 2
list_b = (1,2,6,7,3,4,5,6,8,9,10)
x = slice(4,6)
print(list_b[x])


# ex 3

my_list = ['cow','bird',4,78,6.1]
new_list = my_list.copy()
print('The Original List is', my_list)
print("this is new list is", new_list)




#list Comprehesion

sentence="the quick brown fox jumps over the lazy dog"

print([[word, len(word)] for word in sentence.split()])

# Write a Python program to convert a given list of tuples to a list of lists. 

ls1 = [(1,2),(2,3),(3,4)]
print('The Original List is: ',ls1)
print('List of List is: ',[list(ns1) for ns1 in ls1])

# Finding common items from two lists
        
def common_items(lst1,lst2):
    com_itms = [i for i in lst1 if i in lst2]
    return com_itms
lst1 = [1,2,3,4,5,6]
lst2 = [2,3,6,5,8,9]

print("The common elements in the two lists are: ")
print(common_items(lst1, lst2))

# Replace the last element in a list with another list

a = [1,2,3,6,8,9]
a[5] = [1,3,5,6]
print(a)

# Extend a list without append

b = [10,20,30,40,50]
c= (500,600,700)
b.extend(c)
print(b)

# ########## TUPLE ######################

# Accessing elements of tuple: 
# 	1. By using index:
a = (12,252,5252,662,10,10)
print(a[0],a[1],a[2],a[3],a[4],a[5])

# 	2. By using slice operator:

a = (12,252,5252,662,10,10)

print(a[1:4])

# Mathematical operators for tuple:
# 	+ and * operators for tuple

t1 = (1,2,3,4)
t2 = (5,6,7,8)
t3 = zip(t1,t2)
mapped = map(sum,t3)
sum = tuple(mapped)
print(sum)

# * operators for tuple

mt1 = [(1,2),(4,5),(6,8),(8,10),(0,500)]
x = [(x * y) for x,y in mt1]
print(x)

# Write a Python program to check if a specified element presents in a tuple of tuples.

Orig_list = (('Red','White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))

if any('white' in i for i in Orig_list):
    print(True)
elif any('olive' in i for i in Orig_list):
    print(False)
elif any("Green" in i for i in Orig_list):
    print(True)
else:
    print(False)

    # Write a Python program to convert a given tuple of positive integers into an integer

def tuple_in_Int(nums):
      int(''.join(map(str,nums)))

