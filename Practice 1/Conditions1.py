is_male = True
is_tall= False

if is_male and is_tall:
    print ("Yes, you are!")
    
elif is_male and not(is_tall):
    print ("You are short!")  

elif not (is_male) and is_tall:
    print ("You are female!")

else:
    print ("No, you are not!")    