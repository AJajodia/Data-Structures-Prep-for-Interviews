# string = "asfsdfasdjkfh"
# print(string[2])  # just gets the index
# print(string[2:4])  # it slices at that index exactly

mylist = ["cat", "dog", "rat"]
print(mylist[2])

numlist = [5] * 6
print(numlist)

mylist.insert(2, "squirrel")
print(mylist)

del mylist[3]
print(mylist)

print(list(range(10, 1, -3)))

mystring = "Anurag"
print(mystring.lower())

print(mystring.find("A"))

print(mystring.lower().split("a"))

mytuple1 = (2, 5, 7, 8)
mytuple2 = (5, 9, 5, 2)

print(mytuple1 + (2, 9))

print(5 in set(mytuple1))

list1 = list(mytuple1)
list2 = list(mytuple2)

print(list1)
print(sorted(list2))

names = {"anu": "jajodia", "stephanie": "smith"}
print(names["anu"])




