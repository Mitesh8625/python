# # tuple:collection different data element cnclosed into () parenthesies
# #it is sequare,index follows,orderd but it is imutable means cant do crud operation


# # create tuple
# tup=()
# print(tup,type(tup))
# t1=tuple()
# print(t1,type(t1))


# t2=(500)
# print(t2,type(t2))


# t3=(500,100,"hello",True,5j,45.8448)
# print(t3,type(t3))

# # t4=tuple(45,45,67)
# t4=tuple((45,67,54))
# print(t4,type(t4))


# my_tuple=(3,45,65,4545,55,677)
# print(my_tuple)


# # index
# print("first element=",my_tuple[0])
# print("last element=",my_tuple[-1])

# #slicing
# print(my_tuple[::-1])
# print(my_tuple[2:5])

# #operation
# tuple1=(1,2,3)
# tuple2=(4,5,6)
# print(tuple1+tuple2)
# # print(tuple1+100)

# #tuple function
# tuple3=(1,5,4,2,3)
# print(tuple3)
# print(sorted(tuple3))
# print(sorted(tuple3)[::-1])
# print(sorted(tuple3,reverse=True))

# tuple4=("helo","read","orange","green",1000,300,700)
# print(tuple4.index(300))
# print(tuple4.count(300))


# tuple4[0]="welcome"
# print(tuple4)

my_tuple=(100,200,300,400,1,2,3)
# for i in my_tuple:
#     print(i)


for  i in sorted(my_tuple)[::-1]:
    print(i)