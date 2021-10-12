#[] is for Lists
#() is for Tuples
#{} is for Sets & Dictionaries

s={"blueberry", "rasberry"}

s.add(4)
s.add("strawberry")
s.add("blueberry")

print(s)
# There is no order in sets.

list1= [1,2,3,3,4,4,4,5,"abc",'abc']
No_duplicate_set=set(list1)
No_duplicate_list = list(No_duplicate_set)

print(No_duplicate_set)

list1 = No_duplicate_list

print(No_duplicate_list)

