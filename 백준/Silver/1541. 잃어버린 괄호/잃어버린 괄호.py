import sys
import re

sik=sys.stdin.readline().split('-')

total=0

for i in sik[0].split('+'):
    total+=int(i)

for i in sik[1:]:
    for j in i.split('+'):
        total-=int(j)

print(total)