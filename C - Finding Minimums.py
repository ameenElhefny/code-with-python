n, a = map(int, input().split())
j = 0
k = int(1e9 + 100)
s = []

arr = list(map(int, input().split()))

for i in range(n):
    if j % a == 0 and j!=0:
        s.append(str(k))
        k = int(1e9 + 100)
    k = min(arr[i], k)
    j += 1
s.append(str(k))
k = int(1e9 + 100)
print(" ".join(s))
