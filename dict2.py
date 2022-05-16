'''python Dictionary In-Built Functions
len(), any(), all(), sorted()

Python Dictionary Inbuilt Methods:
keys(), values(), items(), get(), clear(), copy(), pop(), fromkeys(), update()'''

# a = {1:2,2:8,3:9,8:1,5:4,10:'madhav'}
# print(a.get(3, 'Not Found'))
# print(a.pop(3))
# print(a.pop(20, 'Not Found'))
# print(a.popitem())

a = {'name':'madhav','class':10,'rollno':234,}
b = {'name':'naidu','mobile':9972378600}
a.update(b)
print(a)
