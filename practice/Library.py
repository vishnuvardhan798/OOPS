# Create a class called Library.

# Requirements:

# __init__() should create an empty list called books.
# Create add_book(title, author) to add a book.
# Create remove_book(title) to remove a book by its title.
# Create search_book(title) to search for a book and display its details if found.
# Create display_books() to display all books.
# Create count_books() that displays the total number of books.
# Create a menu that allows the user to repeatedly choose operations:
# 1. Add book
# 2. Remove book
# 3. Search book
# 4. Display all books
# 5. Count books
# 6. Exit

# The program should continue showing the menu until the user chooses 6.

# Example:

# 1. Add book
# 2. Remove book
# 3. Search book
# 4. Display all books
# 5. Count books
# 6. Exit

# Choose: 1
# Enter title: Python Basics
# Enter author: John


class Library:

    def __init__(self):
        self.books=[]
        self.menu()

    def menu(self):
        user_input=input("\n1.Add book \n2.Remove book \n3.Search book \n4.Display all books \n5.Count books \n6.Exit \nchoose one : ")
        if user_input=="1":
            self.add_book(input("enter book title :"),input("enter book author :"))
        elif user_input=="2":
            self.remove_book(input("enter book title to remove:"))
        elif user_input=="3":
            self.search_book(input("enter book author to serch:"))
        elif user_input=="4":
            self.display_books()
        elif user_input=="5":
            self.count_books()
        else:
            exit()


    def add_book(self,title,author):
        self.books.append({"title":title,"author":author})
        print("book added successfully")
        self.menu()


    def remove_book(self,title):
        for book in self.books:
            if book["title"]==title:
                self.books.remove(book)
                print("book removed successfully")
                self.menu()
                return True
        print("book is not there")
        self.menu()
        return False

    def search_book(self,author):
        for book in self.books:
            if book["author"]==author:
                print("\nAuthor:{}\nTitle:{}".format(book["author"],book["title"]))
                self.menu()
                return True
        print("book not found")
        self.menu()
        return False


    def display_books(self):
        for book in self.books:
            print("\nAuthor:{} \nTitle:{}".format(book["author"],book["title"]))

        self.menu()

    def count_books(self):
        self.count=0
        for book in self.books:
            self.count+=1
        print("\nCount:{}".format(self.count))
        self.menu()

obj=Library()