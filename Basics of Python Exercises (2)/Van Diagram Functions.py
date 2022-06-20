library1= {"harry potter","hunger games","hobits"}
library2={"harry potter","roemo & juliet"}

town_library_books=library1.union(library2)
mutual_books=library1.intersection(library2)
Unique_books1= library1.difference(library2)
Unique_books2= library2.difference(library1)

print(town_library_books)
print(mutual_books)
print(Unique_books1)
print(Unique_books2)



