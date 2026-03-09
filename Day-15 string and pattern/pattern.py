# for i in range(3):
#      print("*")

# for i in range(3):
#     print("*",end="")

# for i in range(3):
#     for j in range(3):
#      print(i,end=" ")
#     print()



# for i in range(3):
#     for j in range(3):
#      print(j,end=" ")
#     print()



# row=int(input("Enter row count : "))
# column=int(input("Enter column count="))
# for i in range(row):
#     for i in range(row):
#         for j in range(column):
#             print("*",end="")
#         print()


# row=int(input("Enter row count : "))
# column=int(input("Enter column count="))
# for i in range(row):
#     for j in range(column):
#         if i==j:
#             print("1",end="")
#         else:
#             print("0",end="")

#     print()



# count=int(input("Enter row count="))
# for i in range(count):
#     for j in range(i+1):
#             print(i,end="")
#     print()


# count=int(input("Enter row count="))
# for i in range(count):
#     for j in range(i+1):
#             print(j,end="")
#     print()




count=int(input("Enter row count="))
n=1
for i in range(count):
    for j in range(i+1):
            print(n,end="")
            n+1
    print()