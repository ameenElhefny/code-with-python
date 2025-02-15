n = int(input())
arr = list(map(int, input().split()))
ok = 0
for i in range(n // 2):
    if arr[i] != arr[-(i + 1)]:
        ok = 1
        break

if ok:
    print("NO")
else:
    print("YES")
