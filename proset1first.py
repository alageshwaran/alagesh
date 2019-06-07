n=int(input())
s=[]
for i in range (0,n):
    m=input()
    s.append(m)
c=[]    
for i in zip(*s):
	if i.count(i[0])==len(i):
		c.append(i[0])
	else:
		break
print(''.join(c))
