#using and
def max_num(num1,num2,num3):
    if(num1>=num2 and num1>=num3):
        return num1
    elif(num2>=num1 and num2>=num3):
        return num2
    else:
        return num3
#using nested
def max_nested(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

print(max_num(5,5,3))
print(max_nested(3,3,5))
