digits=[0,1,2,3,4,5,6,7,8,9]

#print the first 3 indexes
#print(digits[:3])

#slicing
#print(digits[2:5])
print (digits[2:-2])
#print(digits[2:])

#stride
print(digits[::3])
print(digits [::])
print(digits[2:8:2])
print(digits[2::-2])

print()

#for i in range (len(digits)):
 # print(digits[0:i])

#window_size = 5
#for i in range (len(digits)-(window_size-1)):
#  print(digits[i:i+window_size])

print(digits[::-1])


