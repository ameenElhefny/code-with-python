A, B = map(int, input().split())

def is_lucky(n):
    return all(d in "47" for d in str(n))

lucky_numbers = [i for i in range(A, B + 1) if is_lucky(i)]

print(*lucky_numbers if lucky_numbers else [-1])
