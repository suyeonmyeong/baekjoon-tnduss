n=int(input())
time=[300,60,10]

if n%10 !=0:
  print(-1)
else:
  for i in time:
    print(n//i,end=" ")
    n%=i