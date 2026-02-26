class Library:
    def __init__(self, list, name):
        self.bookList = list
        self.name = name    
        self.lendDict = {}
        
    def showBooks(self):
        print("welcome to the {} library. We have following books in our library.".format(self.name))
        sno = 1
        for book in self.bookList:
            print("{}. {}".format(sno, book))
            sno+=1
    
    def borrowBook(self, book, name):
        if book in self.bookList:
            if book not in self.lendDict:
                self.lendDict.update({book:name})
                print("Borrowing successful. You can take the book.")
            else:
                print(f"This book is currently unavailable. Borrowed by {self.lendDict[book]}.")
        else:
            print("The selected book does not exist in the library collection.")
                
    def addBook(self, book):
        self.bookList.append(book)
        print("The book has been successfully added to the library collection.")
        
    def returnBook(self, book):
        if book in self.bookList:
            if book in self.lendDict.keys():
                self.lendDict.pop(book)
                print("Book has been returned, thank you!")
            else:
                print(f"The book '{book}' is not currently borrowed.")
        else:
            print("This book is not registered in the library system.")
            
            


# EXECUTION WORK
if __name__ == '__main__':
    pythonLibrary = Library(
    [
        "Atomic Habits",
        "Rich Dad Poor Dad",
        "The Alchemist",
        "Think and Grow Rich",
        "How to Win Friends and Influence People",
        "The Psychology of Money",
        "Deep Work",
        "The 7 Habits of Highly Effective People",
        "Start With Why",
        "The Subtle Art of Not Giving a F*ck"
    ],
    "Python"
)
    
    while (True):
        print("Welcome to the {} Library. Please select an option.".format(pythonLibrary.name))
        print("1. Show all books")
        print("2. Borrow a book")
        print("3. Add a new book")
        print("4. Return a book")
        print("press 'q' to quit the program.")
        
        
        user_choice = input()
        if user_choice not in ['1', '2', '3', '4']:
          print("Invalid selection. Please select a valid option.‼️")
          continue
        else:
            user_choice = int(user_choice)
            
            
        # user chooses an option
        if user_choice == 1:
            pythonLibrary.showBooks()
            
        elif user_choice == 2:
            user_inputed_book = input("Enter the book title: ")
            user_inputed_name = input("Enter your name: ")
            pythonLibrary.borrowBook(user_inputed_book, user_inputed_name)
            
        elif user_choice == 3:
            user_inputed_book = input("Enter the title of the book to add: ")
            pythonLibrary.addBook(user_inputed_book)
            
        elif user_choice == 4:
            user_inputed_book = input("Enter the title of the book to return: ")
            pythonLibrary.returnBook(user_inputed_book)  
            
        else:
            print("Invalid selection. select a valid option.‼️")
            
            
        print("Press 'c' to continue or 'q' to quit.")
        user_choice_exit_continue = input()
        while (user_choice_exit_continue !="c" and user_choice_exit_continue !="q"):
            user_choice_exit_continue == input()
        if user_choice_exit_continue == "q":
            print("The program has been terminated.")
            exit()
        
        elif user_choice_exit_continue == "c":
            continue