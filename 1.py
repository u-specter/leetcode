# def max69number(num):
#         s = ""
#         k = 0
#         for i in str(num):
#                 if i == "6" and k == 0:
#                         s = s + "9"
#                         k = 1
#                 else:
#                         s = s + i

#         return int(s)

# print(max69number(9666))


# print(int(str(9666).replace('6', '9', 1)))
# # lst = [1,2,3]
# print(list(int(str(lst))+1))
# a = str(lst)
# b = int(a)
# c = b + 1
# print(list(c))

# a = "".join(str(i) for i in lst)
# a = str(int(a)+1)
# print(list(a))


# lst = [i for i in str(2932)]
    
# a,  b, c, d = sorted(lst)
# print(a,b,c,d)
# print(int(a+d)+int(b+c))


# num = [1,2,3,1,1,3]
# x = 0
# for i in range(len(num)):
#         for y in range(i+1, len(num)):
#                 print(num[i] == num[y])
#                 if num[i] == num[y]:
#                         x+=1
# print(x)                

      
# def productandsum(n):
#         add, prod = 0, 1
#         for i in str(n):
#                 add += int(i)
#                 prod *= int(i)
#         return prod - add

# print(productandsum(234))


# def prodandsum(n):
#         add, prod = 0,1
#         for i in str(n):
#                 add += int(n)
#                 prod *= int(n)
                

# def divide(dividend, divisor):
#         a = dividend/divisor
#         return int(a)      

# print(divide(7,-3))                  

# def squareIsWhite(coordinates):
#         alpha='abcdefgh'
#         print(coordinates[0])
#         a=alpha.index(coordinates[0])+1
#         print(a)
#         b=int(coordinates[1])
#         print(b)
#         return (a+b)%2!=0

# print(squareIsWhite('b3'))        


# alpha = 'abcdefgh'
# a = alpha.index(coordinates[0])+1
# b = int(coordinates[1])
# a = (1+5)%2
# print(a)
from math import gcd
a = [7,5,6,8,3]

print(gcd(min(a), max(a)))