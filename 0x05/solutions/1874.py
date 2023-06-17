# Authored by : hyeonjaee
# Co-authored by : -
# http://boj.kr/a2221192b649405a9abfdf63f49ac8f5
import sys
input = sys.stdin.readline

n = int(input())
s = []
ans = []
num = 1
for _ in range(n):
    val = int(input())
    while num <= val:
        ans.append('+')
        s.append(num)
        num += 1
    if s.pop() != val:
        print('NO')
        break
    ans.append('-')
else:
    for i in ans:
        print(i)
