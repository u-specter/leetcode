def binary(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b

a = input("a = ")
b = input("b = ")   

# print((binary(a) + binary(b)))

def addBinary(x, y):
        return bin(int(x, 2) + int(y, 2))[2:]
        
print(addBinary(a,b))