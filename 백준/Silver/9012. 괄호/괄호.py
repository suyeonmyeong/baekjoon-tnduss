import sys

n= int(sys.stdin.readline().rstrip())

flag=True
for i in range(n):
	flag=True
	stack=[]
	s= sys.stdin.readline().rstrip()
	lst=list(s)
	for j in lst:
		if j =='(':
			stack.append(i)
		else:
			try:
				stack.pop()
			except:
				print('NO')
				flag=False
				break
	if len(stack)==0 and flag:
		print('YES')
	elif flag and len(stack)!=0:
		print('NO')