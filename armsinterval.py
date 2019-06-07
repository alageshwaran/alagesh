a,b=input("").split()
a=int(a)
b=int(b)
for i in range(a,b):
     s=0
     t=i
     while(i!=0):
          r=i%10
          s=s+r*r*r
          i//=10
     if(t==s):
        print(t,end=" ")
