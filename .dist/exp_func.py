def pow(num,exp):
    result=1
    for i in range(1,exp+1):
        result=result*num
    return result

number=int(input("Enter a number:"))
power=int(input("Enter a power:"))
ans=pow(number,power)
print(ans)