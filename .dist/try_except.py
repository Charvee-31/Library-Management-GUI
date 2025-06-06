try:
    value=10/0
    num=int(input("Enter a number:"))
    print(num)

except ZeroDivisionError as err:#am error when any number is divided by 0
    print(err)

except ValueError:#an error when a number of a different datatype other than the specified is entered
    print("INVALID INPUT")