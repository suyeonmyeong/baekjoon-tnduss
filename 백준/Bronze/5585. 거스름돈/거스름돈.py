n=1000-int(input())
coin=[500,100,50,10,5]
result=0
for i in coin:
  result+=n//i
  n%=i
result+=n
print(result)