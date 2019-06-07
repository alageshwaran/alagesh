s = input()
c=0
n=0
for i in range(len(s)):
    if(s[i].isalpha() or s[i].isdigit()):
       c=c+1
    else:
        n=n+1
print(n)
