books=[]
while True:
    print("====--eLibrary--====")
    print("1:AddBook\n2:ShowBook\n3:UpdateBook\n4:DeleteBook\n5:Exit")
    choice=int(input("Enter Choice Number : "))

    if choice==1:
        title=input("Enter book title : ").capitalize()
        if title not in books:
            books.append(title)
            print(f"{title} Book added successfully !!")
        else:
            print(f"{title} Book is already exists so add another book !!")

    elif choice==2:
        if len(books)==0:
            print("No books available try again")
        else:
            print("Available book are:",books)

    elif choice==3:
        if len(books)>0:
            old_book_title=input("Enter book title to update : ").capitalize()
            if old_book_title in books:
                new_title=input("Enter book new title to update : ").capitalize()
                books[books.index(old_book_title)]=new_title.capitalize()
                print(f"{old_book_title}Book title updated successfully !!")
            else:
                print(f"{old_book_title} Book title not found try again !!")
        else:
            print("No books available so first add thr books !!")


    elif choice==4:
        if len(books)>0:
            old_book_title=input("Enter book title to remove : ").capitalize()
            if old_book_title in books:
                
                books.remove(old_book_title.capitalize())
                print("Book remove successfully !!")
            else:
                print(f"{old_book_title} Book title not found try again !!")
        else:
            print("No books available so first add thr books !!")



    elif choice==5:
        print("Thank for using our Service !!")
        break
