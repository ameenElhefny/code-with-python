n = int(input())
arr = list(map(int, input().split()))
for i,val in enumerate(arr):
     if val>0:
          arr[i]=1
     elif val<0:
          arr[i]=2
print (*arr,end=" ")
