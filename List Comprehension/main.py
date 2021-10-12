names=['joe','mike',"george",'john']

list1=[]
for person in names:
  list1.append(person)

print(list1)


print([person for person in names])
print()
#In this way we put the name or the elements that we want to print first in the list, person, and then we write the for loop. So instead few lines ofcode we just make a new list in one line of code.

list2=[]
for person in names:
  list2.append(person+" has been dumped")

print(list2)
print()

#Using operations
print([person + " has been dumped" for person in names])
print()


movies_and_ratings={"hobits": 6, "harry potter": 8, "interstellar": 9,"inception": 9, "irishman":5}

list3=[]
for movie in movies_and_ratings:
  if movies_and_ratings[movie]>8:
    list3.append(movie)

print(list3)

print([movie for movie in movies_and_ratings if movies_and_ratings[movie]>8 ])