# Authored by : hyeonjaee
# Co-authored by : -
# http://boj.kr/d51c9383d6834446a92a26a0af138485
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
d = deque([x for x in range(1, n+1)])
ans = 0

for val in a:
    idx = d.index(val)
    while d[0] != val:
        if idx < len(d) - idx:
            d.append(d.popleft())
        else:
            d.appendleft(d.pop())
        ans += 1
    d.popleft()
    
print(ans)