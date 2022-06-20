list1=[1,2,3,4,5]
list2= ['one', "two", 'three', 'four', 'five']
#list3=["jan",'feb','march','april','may']

zipped = list (zip(list1, list2))
print(zipped)
print()
#If the lists don't have the same length , the zip function will cut off the extra element, which in this case in 6.

unzipped= list(zip(*zipped))
print(unzipped)
print ()

#for (li1, li2) in zip(list1,list2):
#  print(li1)
#  print(li2)
  

items=["pear",'apple',"orange"]
counts=[4,2,6]
prices=[0.99,0.25,0.50]


sentences= []
for(item,count, price) in zip(items,counts,prices):
  item, count, price= str(item), str(count), str(price)
  sentence= 'I bought '+ count + " "+ item + 's at '+ price + ' cents each.'
  sentences.append(sentence)

print(sentences)


