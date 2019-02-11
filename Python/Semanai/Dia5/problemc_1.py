import sys

n,s = map(int,sys.stdin.readline().split())
text = []
decrypted = []
decrypline = []

for i in range(n):
    line = list(input())
    text.append(line)

    s=(s%26)
