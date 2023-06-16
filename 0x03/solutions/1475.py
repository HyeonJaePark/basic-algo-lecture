# Authored by : hyeonjaee
# Co-authored by : -
# http://boj.kr/c1fab487ebe44823affe180507b7d849
import sys
input = sys.stdin.readline

n = input().rstrip('\n')

a = [0] * 10
ret = True

for i in a:
    if (i == 6 or i == 9):
        if ret:
            a[6] += 1
        else:
            a[9] += 1
        ret = not ret
    else:
        a[int(i)] += 1

print(max(a))
