HW_filed= open("HW ID.txt", "r")
#print(HW_filed.readable())
#print(HW_filed.read())
#print(HW_filed.readline()) # It just read the first line and by repeating this command it goesthroug hother lines one by one.
#print(HW_filed.readline())
#print(HW_filed.readlines()) # put all the lines togher inside of an array which we can printit separately by mentioning the index needed.

for index in HW_filed.readlines():
    print(index)



HW_filed.close()