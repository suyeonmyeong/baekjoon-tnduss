import sys
a= int(sys.stdin.readline().rstrip())
b= list(sys.stdin.readline().rstrip())
res=0
t1=a*int(b[2])
t2=a*int(b[1])
t3=a*int(b[0])
print(t1)
print(t2)
print(t3)
print(t1+10*t2+100*t3)