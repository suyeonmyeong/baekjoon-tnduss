import sys

while True:
	n= sys.stdin.readline().rstrip()
	if n=='0':
		break
	else:
		lst=list(n)

		if lst[-1] == '0':
			print('no')
			continue
		else:
			re=lst[::-1]

			if re == lst:
				print('yes')
			else:
				print('no')