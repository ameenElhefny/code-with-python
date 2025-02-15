n=int(input())
arr=list(map(int,input().split()))
a=int(input())
ok =1
for i in range (0,n):
    if (arr[i]==a):
        print(i)
        ok=0
        break
if ok:
    print(-1)
