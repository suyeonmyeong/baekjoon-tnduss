import sys
import math
n= int(sys.stdin.readline().rstrip())

result=0



for i in range(0,n//2+1):
	result+= math.comb(n-i,i)

print(result%10007)