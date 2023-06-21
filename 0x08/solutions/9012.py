# Authored by : hyeonjaee
# Co-authored by : -
# http://boj.kr/40af7359c2164568a04b908e9745d9af
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    brackets = input().rstrip()
    stack = list()
    for bracket in brackets:
        if bracket == '(':
            stack.append('(')
        elif bracket == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                break
    else:
        if not stack:
            print('YES')
            continue
    print('NO')
