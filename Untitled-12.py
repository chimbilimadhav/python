## =, copy() , deepcopy()

# 1. copy
lst1 = [1,2,3,4]
lst2 = lst1
print(lst2,lst1)

lst2[1] = 1000

print(lst2)

print(lst1)

# 2. Shallow Copy

lst1 = [1,2,3,4]
lst2 = lst1.copy()
lst2[1] = 5000
print(lst2, lst1)

#### Shallow copy with respect to Nested List####
lst1 = [[1,2,3,4],[4,5,6,7]]
lst2 = lst1.copy()
print(lst1)

print(lst2)

lst2[1][2] = 9999

print(lst1)

print(lst2)

lst1.append([2,3,4,5])

print(lst1)

print(lst2)

####  DEEP COPY ####

import copy

lst1 = [1,2,3,4]
lst2 = copy.deepcopy(lst1)
lst2[1] = 100
print(lst1)
print(lst2)

# In normal list shallow copy is equal to deep copy

lst1 = [[1,2,3],[3,4,5],[5,6,7]]
lst2 = copy.deepcopy(lst1)
lst2[1][0] = 100
print(lst2)
print(lst1)

