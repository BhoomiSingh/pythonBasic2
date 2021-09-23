sentence= input('enter a sentence')
characterCount = 0
wordCount=1
for i in sentence:
    characterCount=characterCount+1
    if i==' ':
        wordCount=wordCount+1
print('number of words in the sentence ',wordCount)
print('number of characters in the sentence ', characterCount)