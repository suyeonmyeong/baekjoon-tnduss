import sys
res='No'

lst=[]
lst.append('Never gonna give you up')
lst.append('Never gonna let you down')
lst.append('Never gonna run around and desert you')
lst.append('Never gonna make you cry')
lst.append('Never gonna say goodbye')
lst.append('Never gonna tell a lie and hurt you')
lst.append('Never gonna stop')
n= int(sys.stdin.readline().rstrip())
for i in range(n):
	s= sys.stdin.readline().rstrip()
	if s not in lst:
		res='Yes'

print(res)