N=int(input(" "))
a=0
b=1
for i in range(0,N):
    print(b,end=" ")
    s=a+b
    a=b
    b=s
