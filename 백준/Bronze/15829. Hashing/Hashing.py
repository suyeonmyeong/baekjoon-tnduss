import sys

n= int(sys.stdin.readline().rstrip())
s= (sys.stdin.readline().rstrip())
sum=0
r=31
for i in range(len(s)):
	sum+=((ord(s[i])-96)*(r**i)) % 1234567891

print(sum)