name=input("Enter your name:")
name=name.strip()#removes the white spaces from the left and right
name=name.title()#capitalizes the first letter of each word of a string(like a title)
first,last=name.split(" ")#splits the string into two parts that are seperated by the given parameter in split
print("You enter the name:",name)
print(f"Welcome {first}")

