def sayhi(name,age):
    print("HELLO!",name,"You are",str(age),"years old!")

def cube(num):
    return num*num*num
    print("Hello")#will not be executed as the return statement marks the end of a function


name=input("Enter name:")
age=int(input("Enter age:"))
sayhi(name,age)
age_cube=cube(age)
print("The cube of your age is",age_cube)