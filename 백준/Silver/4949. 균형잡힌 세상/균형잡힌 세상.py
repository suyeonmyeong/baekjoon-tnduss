import sys

while True:
	s = list(sys.stdin.readline().rstrip())
	flag=True
	if len(s)==1 and s== ['.']:
		sys.exit()
	stack=[]
	for i in s:
		if i == '[' or i == '(':
			stack.append(i)
		
		elif i == ']'and len(stack)!=0:
			if stack[-1] =='[':
				stack.pop()
			else:
				flag=False
		elif i == ')'and len(stack)!=0:
			if stack[-1] =='(':
				stack.pop()
			else:
				flag=False
		elif (i == ']' or i == ')') and len(stack)==0:
			flag=False
	if len(stack)==0 and flag:
			print('yes')
	else:
			print('no')