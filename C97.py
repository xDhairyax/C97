x=input("enter a string:")
characterCount=0
wordCount=1

for i in x:
    characterCount=characterCount+1
    if (i ==' '):
        wordCount=wordCount+1
print("Number of Characters in a String:")
print(characterCount)
print("Number of Words in the String:")
print(wordCount)


