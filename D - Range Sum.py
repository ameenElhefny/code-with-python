n=int(input())
while n>0:
    a,b=map(int,input().split())
    if(a>b):
        temp=b
        b=a
        a=temp
    a-=1
    sum=(b*(b+1)//2) -(a*(a+1)//2)
    print (sum)
    n-=1
