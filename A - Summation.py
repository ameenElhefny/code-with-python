n=int(input())
arr=list(map(int,input().split()))
sum=0
for i in arr:
    sum+=i
if(sum<0):
    sum *=-1
print (sum)
