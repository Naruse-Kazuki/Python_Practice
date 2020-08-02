n = int(input())
if n%1000==0:
    ans=0
else:
    x=n%1000
    ans=1000-x
print(ans)