# Dictionary: Key-value pairs, unordered, Mutable
# mydict = {"name":"madhav","age":"28","city":"Bengaluru"}

# # print(mydict)

# mydict2 = dict(name = "mary", age=27, city="Boston")
# print(mydict2)

# value = mydict["lastname"]
# # print(value)

# # mydict["email"] = "chimbilimadhav@gmail.com"
# # print(mydict)

# # mydict["email"] = "madhavanaidu1234@gmail.com"
# # print(mydict)

# # del mydict["name"]
# # print(mydict)

# # mydict.popitem( )
# # print(mydict)

# # if "name" in mydict:
# #     print(mydict["name"])
    
# # try:
# #     print(mydict["lastname"])
# # except:
# #     print("Error")

# # for key, value in mydict.items():
# #     print(key, value)

# # mydict_cpy = dict(mydict)

# # mydict_cpy["email"] = "chimbilimadhav@gmail.com"

# # print(mydict_cpy)
# # print(mydict)

# # mydict.update(mydict2)
# # print(mydict)

# # This will be hard and annoying!
# # d['k1'][2]['k2'][1]['tough'][2][0]
# # d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
# # print(d['k1'][2]['k2'][1]['tough'][2][0])

mydict2 = {1:'harsha', 'name':{'location':{'marath', 'white'}, 'che':{1:{'hy', 'ra'}}}}

a = mydict2[1]
print(a)
b = mydict2['name']['location']
print(b)
c = mydict2['name']['location']
print(c)

d = {'key1':{'nestkey':{'subnestkey':'value'}}}


test_dict = {'Gfg' : {"a" : 7, "b" : 9, "c" : 12},'is' : {"a" : 15, "b" : 19, "c" : 20},'best' :{"a" : 5, "b" : 10, "c" : 2}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing key
temp = "c"

# using item() to extract key value pair as whole
res = [val[temp] for key, val in test_dict.items() if temp in val]
  
# printing result 
print("The extracted values : " + str(res))