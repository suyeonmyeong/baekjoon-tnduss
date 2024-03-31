lst=[]
for i in range(1,10000):
	ths=(i)//1000
	hdr=(i%1000)//100
	ten=(i%100)//10
	one=(i%10)
	result=ths+hdr+ten+one+i
	lst.append(result)

for i in range(1,10000):
	if i not in lst:
		print(i)