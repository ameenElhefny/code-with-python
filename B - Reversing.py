n=int(input())
arr=list(map(int,input().split()))
for i in range (0 ,n):
     if arr[i]==0:
         arr[:i]=arr[:i][::-1]
for i in arr:
    print (i,end=" ")
