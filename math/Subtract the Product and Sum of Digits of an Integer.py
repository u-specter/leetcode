def subtractProductAndSum(n):
    add, prod = 0, 1
    for i in str(n):
        add += int(i)
        prod *= int(i)
    return (prod - add)

print(subtractProductAndSum(234))    