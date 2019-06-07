a,b=input().split()
a=int(a)
b=int(b)
P=a+1
count=0
for num in range(P,b):
    for num2 in range(1,num+1):
        if(num%num2==0):
            count=count+1
    if(count==2):
        print(num,end=' ')
    count=0
