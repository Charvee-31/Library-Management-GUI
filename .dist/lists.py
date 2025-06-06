books=["harry potter","book thief","shatter me","mocking bird","400 days"]
numbers=[7,1,6,1,2]
print(books[0])#to access the 0th index of the list ie harry potter
print(books[-1])#access from the last 
books.append("atomic habits")#adds another value to the end of the list
books.insert(1,"twilight")#inserts value at the specified index
print(books)
print(numbers.sort())#sorts in ascending order or alphabetical order
print(numbers.reverse())#reverses the order of the list
print(numbers.count(1))#counts the numbers of 1s in the list
print(books.index("book thief"))#returns the index of the specified value
numbers.remove(1)#removes all the 1s
numbers.pop()#pops out the last element
print(books.extend(numbers))#adds one list to the other
books2=books.copy()#copies the list books to the list books2
print(books2)
books.clear()#empties out or clears the list

