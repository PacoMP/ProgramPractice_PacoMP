import sys

n,s = map(int,sys.stdin.readline().split())
text = []
decrypted = []
decrypline = []

for i in range(n):
    line = list(input())
    text.append(line)

    s=(s%26)

for lines in text:
    for letter in lines:
        if(ord(letter)>64 and ord(letter)<91):
            letter = chr((ord(letter)-s))
            if ord(letter)<65:
                #print('entre1')
                letter = chr(ord(letter)+26)
            #decrypline.append(letter)
        elif (ord(letter)>96 and ord(letter)<123):
            #print('entre0')
            letter = chr(ord(letter)-s)
            #print(letter)
            if ord(letter)<96:
                #print('entre2')
                letter = chr(ord(letter)+26)
        decrypline.append(letter)
    decrypted.append(list(decrypline))
    decrypline[:] = []

for lines in decrypted:
    print(''.join(lines))
