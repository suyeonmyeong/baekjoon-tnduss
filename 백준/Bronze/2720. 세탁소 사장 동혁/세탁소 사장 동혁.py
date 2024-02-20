n=int(input())
lst=[]
coin=[25,10,5]
for i in range(n):
  k= int(input())
  lst.append(k)

for i in lst:
  for j in coin:
    print(i//j,end=" ")
    i%=j
  print(i)