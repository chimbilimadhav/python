
test_list = [[1,2,3,4],[5, 6, 7, 8, 9]]
for i in test_list[-1:]:
    for j in i:
        print(j, sep=' ',)
    
# Prinnting of one value from Dictionary

Dict1 = [{'a':1,'b':2,'c':{'1':1,'2':{'a':1,'b':2,'c':'HARSHA'}}}]
generator = ( item ['c'] for item in Dict1 )
for i in generator:
    print(i)

#3. Transpose

def transpose(l1, l2):
    l2 = list(map(list, zip(*l1)))
    return l2
l1 = [[1,2,3], [4,5,6], [7,8,9]]
l2 = []
print(transpose(l1, l2))

#4.matrices

matrix=[(1,2,3),(4,5,6)]
for column in matrix:
	print(column)
print("\n")
t_matrix = zip(*matrix)
for column in t_matrix:
	print(column)

#
my_own = {'1':'harsha','name':{'location':{'bangalore':{'marath','white'},'che':{1:{'hy','ra'}}}}}










[ 'harsha','marath','white','hy','ra']
    
# 

A = (1,2,3)
B = (4,5,6)

for x in range(len(A)):
    
   for y in range(len(A[0])):

       result[x][y] = A[x][y] + B[x][y]

for q in result[x][y]:

   print(q)
    