import sys

n= int(sys.stdin.readline().rstrip())
s= (sys.stdin.readline().rstrip())
sum=0

for i in range(len(s)):
	sum+=((ord(s[i])-96)*(31**i)) 

print(sum% 1234567891)