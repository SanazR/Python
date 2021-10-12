try:
     #answer= 10/0
     number= int(input("Enter a number: "))
     print (number)

except ZeroDivisionError as err:
    print (err)

except ValueError:
    print("invalid Input")

#Instead of getting errors from python, when we put a incorrect type as an input, it gives "invalid input" as an error 