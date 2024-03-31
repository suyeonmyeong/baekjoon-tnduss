import math
import sys
input = sys.stdin.readline

lst=[0]*9
n=input().rstrip()
for i in n:
	num=int(i)
	if num == 6 or num == 9:
		lst[6]+=1
	else:
		lst[num]+=1
lst[6]=math.ceil(lst[6]/2)
print(max(lst))