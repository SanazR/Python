groceries= {"apples":2, "oranges": 5}

print(groceries["apples"])

#The function below is same as above but the only diffence is if we don't the item in out Dic instead of error it just shows "None" 
print(groceries.get("bananas"))
print()


Contacts={
  "Joe": {"phone": 125045,"email":"joe@gmail.com"},
  "kyle":["458-200","k@yahoo.com"]
}

print(Contacts.get("Joe"))
print()

Sentence="I love drawing the nature with the birds"
word_count={
 "I":1,
 "love":1,
 "drawing":2,
 "with":1,
 "birds":1
}

word_count["the"]=2
print(word_count)
print()

print(list(word_count.items()))
print()
print(list(word_count.keys()))
print()
print(list(word_count.values()))
print()

#Remove sth from Dic
#print(word_count.pop("I"))

#word_count.pop("I") 
#print(word_count)

print(sorted(list(word_count.values())))


print(word_count.clear())



 

