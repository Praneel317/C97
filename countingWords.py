introString = input("Enter Your Intro:")
print(introString)
characterCount=0
wordCount=1
for i in introString:
    characterCount=characterCount+1
    print(characterCount)
    if(i==" "):
        wordCount=wordCount+1
        print("number of words in the string:")
        print(wordCount)
        print("number of characters in the string:")
        print(characterCount)