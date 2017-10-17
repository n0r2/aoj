n = int(input())
a = [int(input()) for i in range(n)]
minr = a[0]
ans = -float('inf')
for i in range(1, n):
    ans = max(a[i] - minr, ans)
    minr = min(a[i], minr)
print(ans)
