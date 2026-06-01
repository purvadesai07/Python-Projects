print("=" * 50)
print("      LIBRARY MANAGEMENT SYSTEM")
print("=" * 50)
books = []
while True:
    print("--------------------------------------1. ADD BOOKS--------------------------------------")
    print("--------------------------------------2. ISSUE BOOKS--------------------------------------")
    print("--------------------------------------3. RETURN BOOKS--------------------------------------")
    print("--------------------------------------4. SEARCH BOOKS--------------------------------------")
    print("--------------------------------------5. VIEW ALL BOOKS-------------------------------------")
    print("--------------------------------------6. EXIT-------------------------------------")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        print("ADD BOOKS")
        n = int(input("Enter no. of books you want to add: "))
        for i in range(n):
            book_name = input(f"Enter Book {i+1} Name: ")
            if book_name not in books:
                books.append(book_name)
            else:
                print("Book already exists!")
        print("Books Added Successfully!!")
        print("Current Books:", books)
    elif choice == 2:
        print("ISSUE BOOKS")
        book = input("Enter book name to issue: ")
        if book in books:
            books.remove(book)
            print("Book issued successfully!")
        else:
            print("Book not available.")
    elif choice == 3:
        print("RETURN BOOKS")
        book = input("Enter book name to return: ")
        if book not in books:
            books.append(book)
            print("Book returned successfully!")
        else:
            print("Book is already available in the library.")
    elif choice == 4:
        print("SEARCH BOOKS")
        book = input("Enter book name to search: ")
        if book in books:
            print(f'"{book}" is available in the library.')
        else:
            print(f'"{book}" is not available in the library.')
    elif choice == 5:
        if len(books) == 0:
            print("No books available in the library.")
        else:
            print("Available Books:")
            for book in books:
                print(book)
    elif choice == 6:
        print("EXIT")
        print("THANK YOU!!")
        break
    else:
        print("Invalid Choice! Please try again.")