import sys
input = sys.stdin.readline

answer = []
n, k = map(int, input().split())

pre = [0] + [n if i == 1 else i - 1 for i in range(1, n + 1)]
nxt = [0] + [1 if i == n else i + 1 for i in range(1, n + 1)]

i = 1
cur = 1
while (n > 0):
    if i == k:
        pre[nxt[cur]] = pre[cur]
        nxt[pre[cur]] = nxt[cur]
        answer.append(cur)
        i = 1
        n -= 1
    else:
        i += 1
    cur = nxt[cur]

print('<', end='')
print(', '.join(map(str, answer)), end='')
print('>')