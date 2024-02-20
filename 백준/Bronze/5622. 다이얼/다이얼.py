import sys

n= list(sys.stdin.readline().rstrip())
sum=0
for i in n:
	if ord('A')<=ord(i)<=ord('C'):
		sum+=3
	elif ord('D')<= ord(i) <=ord('F'):
		sum+=4
	elif ord('G')<= ord(i) <=ord('I'):
		sum+=5
	elif ord('J')<= ord(i) <=ord('L'):
		sum+=6
	elif ord('M')<= ord(i) <=ord('O'):
		sum+=7
	elif ord('P')<= ord(i) <=ord('S'):
		sum+=8
	elif ord('T')<= ord(i) <=ord('V'):
		sum+=9
	else:
		sum+=10
print(sum)