num = int(input("Enter the Value"))
def fibinocci(n):
    pre_last,last = 0,1
    for each in range(n):
        yield pre_last
        pre_last,last = last, pre_last + last
print(list(fibinocci(num)))