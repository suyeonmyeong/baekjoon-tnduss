import sys
n= int(sys.stdin.readline().rstrip())
wrd=[]
st=[]

for i in range(n):
	lst= sys.stdin.readline().rstrip().split()
	ltr=list(lst[1])
	str=''
	for i in ltr:
		for j in range(int(lst[0])):
			str+=i
	st.append(str)

for i in st:
	print(i)