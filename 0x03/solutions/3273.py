# Authored by : hyeonjaee
# Co-authored by : -
# http://boj.kr/efae03424d4e4adb85010f67f1ef59ad
import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
x = int(input())

st, en = 0, n - 1
ans = 0
while st < en:
    tmp = a[st] + a[en]
    if tmp == x:
        ans += 1
        st += 1
    elif tmp < x:
        st += 1
    else:
        en -= 1

print(ans)

'''
정렬과 투포인터를 이용한 풀이
'''