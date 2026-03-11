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
        pass



    elif choice==4:
        pass



    elif choice==5:
        print("Thank for using our Service !!")
        break
