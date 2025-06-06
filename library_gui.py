class Books:
    def __init__(self,book,author,book_id):
        self.book=book
        self.author=author
        self.book_id=book_id
        self.borrowed=False
        
    def __str__(self):
        if self.borrowed==True:
            status="Borrowed"
        else:
            status="Available"
        return f"|ID:{self.book_id}|Name:{self.book}|Author:{self.author}|Status:{status}"#incase we print the object it will be printed in this string format
        
        
class Library():
    def __init__(self):
        self.books=[]#a list of all book objects
    def add_book(self,book):
        self.books.append(book)
        
    def display_all(self):
            return[str(book) for book in self.books]#return a list of books
    
    def Borrow_Book(self,book_id):
        for book in self.books:
            if book.book_id==book_id:
                if book.borrowed==True:
                    return("Book is already borrowed")
                else:
                    book.borrowed=True
                    return("Book borrowed successfully")    
        return("Book not found")
    def Return_Book(self,book_id):
        for book in self.books:
            if book.book_id==book_id:
                if book.borrowed==False:
                    print("The book has not been borrowed")
                else:
                    book.borrowed=False
                    print("The book has been returned successfully")
                return
                
        print("Book not found")


from tkinter import *
root=Tk()
root.title("Library Management System")
root.geometry("400x300")
lbr=Library()

def add_book_window():
    add_window=Toplevel(root)
    add_window.title("Add a book")
    add_window.geometry("300x250")

    #enter the information about the book
    Label(add_window,text="Book Name:").pack(pady=5)
    name_entry=Entry(add_window,width=30)
    name_entry.pack(pady=5)

    Label(add_window,text="Author Name:").pack(pady=5)
    author_entry=Entry(add_window,width=30)
    author_entry.pack(pady=5)

    Label(add_window,text="Book_ID:").pack(pady=5)
    book_id_entry=Entry(add_window,width=30)
    book_id_entry.pack(pady=5)

    def Submit_book():
        name=name_entry.get()
        author=author_entry.get()
        book_id=book_id_entry.get()

        book=Books(name,author,book_id)
        lbr.add_book(book)
        add_window.destroy()
    
    Button(add_window,text="Submit",command=Submit_book).pack(pady=10)

def display_books():
    display_window=Toplevel()
    display_window.title("Books List")
    display_window.geometry("400x300")

    listbox=Listbox(display_window,width=80,height=20)
    listbox.pack(padx=10,pady=10)
    book_list=lbr.display_all()
    for book in book_list:
        listbox.insert(END,book)
    
   
def borrow_book_window():
    borrow_window=Toplevel(root)
    borrow_window.title("Borrow book")
    borrow_window.geometry("300x250")

    Label(borrow_window,text="Book_ID").pack(pady=5)
    book_id_entry=Entry(borrow_window,width=30)
    book_id_entry.pack(pady=5)

    def borrow():
        book_id=book_id_entry.get()
        result=lbr.Borrow_Book(book_id)
        Label(borrow_window,text=result).pack(pady=5)

    Button(borrow_window,text="Borrow",command=borrow).pack(pady=10)


def return_book_window():
    return_window=Toplevel(root)
    return_window.title("Return Book")
    return_window.geometry("300x250")

    Label(return_window,text="Book ID").pack(pady=5)
    book_id_entry=Entry(return_window,width=30)
    book_id_entry.pack(pady=5)
    def return_book():
        book_id=book_id_entry.get()
        result=lbr.Return_Book(book_id)
        Label(return_window,text=result).pack(pady=5) 
    Button(return_window,text="Return",command=return_book).pack(pady=10)

Label(root, text="Library Menu", font=("Arial", 16)).pack(pady=10)

Button(root, text="Add Book", width=20, command=add_book_window).pack(pady=5)
Button(root, text="Display Books", width=20, command=display_books).pack(pady=5)
Button(root, text="Borrow Book", width=20, command=borrow_book_window).pack(pady=5)
Button(root, text="Return Book", width=20, command=return_book_window).pack(pady=5)
#command will link the button to a specific function which on clicking will run the function

root.mainloop()#start the app
