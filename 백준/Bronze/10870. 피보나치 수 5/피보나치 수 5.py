n= int(input())

def fib(n):
	if n <=1:
		return n
	return fib(n-1)+fib(n-2)

arr=[]
arr.append(0)
arr.append(1)
for i in range(2,n+1,1):
	arr.append(arr[i-1]+arr[i-2])

print(fib(n))