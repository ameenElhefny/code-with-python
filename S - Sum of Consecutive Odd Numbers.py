t=int(input())
while t>0:
    n , x=map(int ,input().split())
    if n>x:
         temp=n
         n=x
         x=temp
    ans=0
    for i in range (n+1,x):
        if i&1:
           ans+=i
    print (ans)
    t-=1
