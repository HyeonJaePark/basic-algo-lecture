# Authored by : hyeonjaee
# Co-authored by : -
# http://boj.kr/cc7ee8575d074e7b83bd2576b98acf37

import sys
input = sys.stdin.readline

ans = 0

n = int(input())
for _ in range(n):
    vals = input().rstrip()
    stack = list()
    for val in vals:
        if stack and val == stack[-1]:
            stack.pop()
        else:
            stack.append(val)
    if not stack:
        ans += 1

print(ans)
