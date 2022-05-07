#1 Printing Sublist from ListofLists

test_list = [[1,2,3,4],[5, 6, 7, 8, 9]]
for i in test_list[-1:]:
    for j in i:
        print(j, sep=' ',)

#2 ==== lst2 = [{'a':1, 'b':2, 'c':{1: 1, 2: {'a':1, 'b':2, 'c':'harsha'}}}]

list2 = [{'a':1, 'b':2, 'c':{1:2, 2:{'a':5, 'b':7, "c":'harsha'}}}]
print(list2[0]['c'][2]["c"])
x = list2[0]['c'][2]["c"]
print({i:x.count(i) for i in x})

#3 ====TRANSPOSE

list_of_lists = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
transposed = [[row[i] for row in list_of_lists] for i in range(len(list_of_lists[0]))]
print(transposed)

# 4

test_list1 = [1, 3, 4, 6, 8]
test_list2 = [4, 5, 6, 2, 10]

print("Original list 1 : " + str(test_list1))
print("Original list 2 : " + str(test_list2))

res_list = []
for i in range(0, len(test_list1)):
       res_list.append(test_list1[i] + test_list2[i])

print("Resultant list is : " + str(res_list))

#5
mydict2 = {1:'harsha', 'name':{'location':{'marath', 'white'}, 'che':{1:{'hy', 'ra'}}}}
nl = []
nl.append(mydict2[1])
nl.append(mydict2['name']['location'])
nl.append(mydict2['name']['che'][1])
print(nl)

#6
mydict3 = {10:56, 10:4, 20:1, 20:9, 30:1, 50:6}
mydict4 = {}
for x in mydict3:
       if x in mydict4:
              mydict4[x] += 1
       else:
              mydict4[x] = 1
print(mydict4)
