def spin_words(sentence):
  string = " "
  for i in sentence:
        string = i + string 
  return string

sentence = "Hello"
print("The original sentence is:",sentence)
print("The reverse sentence is:", spin_words(sentence)) 



