class Library:
    def __init__(self,fileName):
        self.fileName = fileName
        self.file= open(self.fileName,"a+")
      

    def __del__(self):
        self.file.close()

    def listBooks(self):
        self.file.seek(0) 
        books=self.file.read().splitlines()
        if not books:
           print("There are not any books")   
        for book in books:
            bookInfo=book.split(",")
            print("Book Info: "+bookInfo[0]+" by "+bookInfo[1])

    def addBook(self):
        title=input("Enter the book title: ")
        author=input("Enter the author: ")
        releaseDate=input("Enter the release date: ")
        numPages=input("Enter the number of pages: ")
        bookInfo=f"{title},{author},{releaseDate},{numPages}"
        self.file.write(bookInfo)
        print("Book added successfully!")

    def updateBook(self, title):
        self.file.seek(0)
        books = self.file.readlines()
        updatedBooks = []
        for book in books:
            if title.lower() in book.lower():
                updatedInfo = []
                bookInfo = book.split(',')
                for i, info in enumerate(bookInfo):
                    newValue = input(f"Enter the new {info.split(',')[0]} (leave empty to keep the old one): ").strip()
                    if newValue:
                        updatedInfo.append(newValue)
                    else:
                        updatedInfo.append(info.strip())  # Keep the old value
                updatedBook = ','.join(updatedInfo) + '\n'
                updatedBooks.append(updatedBook)
            else:
                updatedBooks.append(book)
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(updatedBooks)
        print(f"Book '{title}' updated successfully!") 

    def removeBook(self, title):
        self.file.seek(0)
        books=self.file.readlines()
        savedBooks= filter(lambda book: title.lower() not in book.lower(),books)
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(savedBooks)
        print(f"Book '{title}' has been removed successfully")

lib= Library("books.txt")

while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Update Book")

    choice = input("Enter your choice: ")

    if choice == "1":
        lib.listBooks()
    elif choice=="2":
        lib.addBook()
    elif choice=="3":
        title=input("Enter the title of the book to remove: ")
        lib.removeBook(title)
    elif choice == "4":
        title=input("Enter the title of the book to update: ")
        lib.updateBook(title)
    else:
        print("Invalid choice!")