# list1=[21,54,29,54,87,89]
# print(list1)

# # operation
# x=[1,2,3]
# y=[4,5,6]
# print(x+y)

# x.append(100)
# print(x)
# x[2]=222
# print(x)

colors=[]
print(colors)
colors.append("red")
print(colors)
colors.append("green")
colors.append(["blue","white"])
print(colors)
print("--------------------")
print(colors[-1])
print(colors[2])
print("--------------------")
colors.append(("cyan","grey"))
print(colors)
colors.append({"black","yello"})
print(colors)
colors.append({"black","yello"})
print(colors)
colors.append({"#0ef455":"litegreen"})
print(colors)
print("--------------------")
#update last element
colors[-1]="maroon"
print("--------------------")
# add elementby using insert

colors.insert(0,"orange")

print(len(colors))
colors.pop()
print(colors)
print(len(colors))
colors.pop(2)
print(colors)
colors.remove("red")
print(colors)
del colors[0]
print(colors)
print("----------------------------------------------------------")
# traversing list

for i in colors:
    print(i)



















