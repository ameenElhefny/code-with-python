n, a = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
arr=arr[::-1]
sumo , ans =[0,0]
for i in arr:
    if not a:
        break
    sumo +=i
    ans =max(ans,sumo)
    a-=1
print(ans)
