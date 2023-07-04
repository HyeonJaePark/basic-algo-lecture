import sys
from collections import deque
input = sys.stdin.readline
        
answer = []
n, k = map(int, input().split())
d = deque([x for x in range(1, n + 1)])
for _ in range(n):
    for i in range(k - 1):
        d.append(d.popleft())
    answer.append(d.popleft())

print('<', end='')
print(', '.join(map(str, answer)), end='')
print('>')