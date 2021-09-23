f=open('test.txt')
# f.read()
fileLines=f.readlines()
for line in fileLines:
    print(line)

sentence='i am bhoomi, i study in 10th grade'
words= sentence.split()
print(words)

words1= sentence.split(",")
print(words1)