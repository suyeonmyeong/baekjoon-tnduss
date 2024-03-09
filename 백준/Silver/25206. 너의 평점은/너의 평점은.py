import sys
d={'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
sum=0
div=1e-13
for i in range(20):
	lst= sys.stdin.readline().rstrip().split()
	if lst[2]== 'P':
		continue
	else:
		div+=float(lst[1])
		sum+= float(lst[1])*d[lst[2]]

print(sum/div)