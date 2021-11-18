n, m, a = map(int, input().split())

if m % a == 0:
    res1 = m // a
else:
    res1 = m // a + 1

if n % a == 0:
    res2 = n // a
else:
    res2 = n // a + 1

print(res1 * res2)
