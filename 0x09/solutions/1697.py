# Authored by : hyeonjaee
# Co-authored by : -
# http://boj.kr/22130bcdd2f241f58c4e4246bcfa1baa
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
d = deque([n])
vis = [-1] * 100005
vis[n] = 0

while vis[k] == -1:
    cur = d.popleft()
    for nxt in [cur-1, cur+1, 2*cur]:
        if nxt < 0 or nxt > 100000:
            continue
        if vis[nxt] != -1:
            continue
        vis[nxt] = vis[cur] + 1
        d.append(nxt)

print(vis[k])