# books=[]
# while True:
#     print("====--eLibrary--====")
#     print("1:AddBook\n2:ShowBook\n3:UpdateBook\n4:DeleteBook\n5:Exit")
#     choice=int(input("Enter Choice Number : "))

#     if choice==1:
#         title=input("Enter book title : ").capitalize()
#         if title not in books:
#             books.append(title)
#             print(f"{title} Book added successfully !!")
#         else:
#             print(f"{title} Book is already exists so add another book !!")

#     elif choice==2:
#         if len(books)==0:
#             print("No books available try again")
#         else:
#             print("Available book are:",books)

#     elif choice==3:
#         if len(books)>0:
#             old_book_title=input("Enter book title to update : ").capitalize()
#             if old_book_title in books:
#                 new_title=input("Enter book new title to update : ").capitalize()
#                 books[books.index(old_book_title)]=new_title.capitalize()
#                 print(f"{old_book_title}Book title updated successfully !!")
#             else:
#                 print(f"{old_book_title} Book title not found try again !!")
#         else:
#             print("No books available so first add thr books !!")


#     elif choice==4:
#         if len(books)>0:
#             old_book_title=input("Enter book title to remove : ").capitalize()
#             if old_book_title in books:
                
#                 books.remove(old_book_title.capitalize())
#                 print("Book remove successfully !!")
#             else:
#                 print(f"{old_book_title} Book title not found try again !!")
#         else:
#             print("No books available so first add thr books !!")



#     elif choice==5:
#         print("Thank for using our Service !!")
#         break





















books = []

# Add Book
def add_book():
    title = input("Enter Book Title: ").title()
    author = input("Enter Author Name: ").title()
    year = input("Enter Publication Year: ")

    for book in books:
        if book["title"] == title:
            print("Book already exists!\n")
            return

    books.append({"title": title, "author": author, "year": year})
    print("Book added successfully!\n")


# Show Books
def show_books():
    if not books:
        print("No books available.\n")
        return

    print("\n---- Available Books ----")
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book['title']} | {book['author']} | {book['year']}")
    print()


# Update Book
def update_book():
    title = input("Enter Book Title to Update: ").title()

    for book in books:
        if book["title"] == title:
            book["title"] = input("Enter New Title: ").title()
            book["author"] = input("Enter New Author: ").title()
            book["year"] = input("Enter New Year: ")
            print("Book updated successfully!\n")
            return

    print("Book not found!\n")


# Delete Book
def delete_book():
    title = input("Enter Book Title to Delete: ").title()

    for book in books:
        if book["title"] == title:
            books.remove(book)
            print("Book deleted successfully!\n")
            return

    print("Book not found!\n")


# Search Book
def search_book():
    title = input("Enter Book Title to Search: ").title()

    for book in books:
        if book["title"] == title:
            print("\nBook Found")
            print("Title :", book["title"])
            print("Author:", book["author"])
            print("Year  :", book["year"])
            print()
            return

    print("Book not found!\n")


# Main Program
while True:
    print("====== eLibrary System ======")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Search Book")
    print("6. Exit")

    try:
        choice = int(input("Enter Choice: "))
    except ValueError:
        print("Invalid input. Enter number only.\n")
        continue

    if choice == 1:
        add_book()
    elif choice == 2:
        show_books()
    elif choice == 3:
        update_book()
    elif choice == 4:
        delete_book()
    elif choice == 5:
        search_book()
    elif choice == 6:
        print("Thank you for using eLibrary!")
        break
    else:
        print("Invalid choice. Try again.\n")