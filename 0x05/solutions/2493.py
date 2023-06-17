# Authored by : hyeonjaee
# Co-authored by : -
# http://boj.kr/c28767cfa25c4615ba02ecc277bb309a
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
s = []
ans = [0] * (n + 1)

for idx, ret in enumerate(a, 1):
    while s and ret > s[-1][0]:
        s.pop()
    if s:
        ans[idx] = s[-1][1]
    s.append((ret, idx))
    
print(' '.join(map(str, ans[1:])))
    