# #method-count,find,replace,join,index,split,split

# #iterate string
# name="Itvedant"
# for i in name:
#     print(i)

# withputvowel_str=""
# for i in name:
#     if i not in "aeiouAEIOU":
#         withputvowel_str=withputvowel_str+i
# print(withputvowel_str)

# str=input("enter string=")
# char=input("enter character=")
# count=0
# for i in str:
#     if char==i:
#         count+=1

# print(f"{char} character count into{str} is {count}")


str=input("enter string=")
chkstr=input("enter char/word to find and show count=")
count=0
chkstr=""
for i in range(len(str)):
    # print(i,str[i])
    k=i
    for j in range(len(chkstr)):
        try:
            check+str[k]
            k+=1
        except:
            None
    if check==chkstr:
        count+1
    check=""
if count!=0:
    print(f"{chkstr} found in {str} and count={count}")
else:
    print(f"{chkstr} not found in {str}")