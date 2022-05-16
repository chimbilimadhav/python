# def is_prime(num):
#     for n in range(2,num):
#         if num % n == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, 'is prime number')


import math
def is_prime2(num):
    if num % 2 == 0 and num > 2:
        return False
    for i in range(3, int(math.sqrt(num))+1,2):
        if num % i ==0:
            return False
    return True


