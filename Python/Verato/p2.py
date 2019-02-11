import sys

list = []
list = sys.stdin.readline().split(',')
for word in list:
    word.replace('\n','')

list.sort(key=len)

for word in list:
    if word.len() == word[0].len():
        print(word,end = ',')

for word in list:
    if word.len() == word[-1].len():
        print(word,end = ',')
