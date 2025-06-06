import random
def roll_dice(num):
    return random.randint(1,num)

def factorial(num):
    fact=1
    for number in range(1,num+1):
        fact=fact*number
    return fact

def sum_of_individual(num):
    sum=0
    while num>0:
        rem=num%10
        sum=sum+num
        num=num//10
    return sum

def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True



