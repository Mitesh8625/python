# count=int(input("Enter row count : "))
# for i in range(count):
#     for j in range(i+1):
#         print("*",end="") 
#     print()

# count=int(input("Enter row count : "))
# for i in range(count):
#     for j in range(count,i,-1):
#         print("*",end="") 
#     print()


# count=int(input("Enter row count :"))
# for i in range(count):
#     for k in range(count,i+1,-1):
#         print(end="") 

#     for j in range(i+1):
#         print("*",end="")
#     print()                                                          


5

# count=int(input("Enter row count :"))
# for i in range(count):
#     for k in range(count,i+1,-1):
#         print(end="") 

#     for j in range(i+1):
#         print("*",end="")
#     print()                                                          


# for i in range(num,0,-1):
#     print("*"*(2*i-1))


num=int(input("Enter row count :"))
for i in range(num):
    print(" "*i+"*"*(2*(num-i)-1)) 