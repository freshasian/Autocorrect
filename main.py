from textblob import TextBlob # correcter library.
import enchant # word suggester library.
while True:
 UserInput=input("Enter: ")
 A=TextBlob(UserInput)
 B= A.correct()
 print(B)
 c = enchant.Dict("en_US") 
 c.check(UserInput)
 print(c.suggest(UserInput)) 

# source
# textblob from textblob website
# enchant from geeksforgeeks 
