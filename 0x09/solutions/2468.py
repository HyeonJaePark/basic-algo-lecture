# Authored by : hyeonjaee
# Co-authored by : -
# http://boj.kr/e17bebac11df4b4195746559d64eab33
import sys
from collections import deque
input = sys.stdin.readline

dxs = [-1, 1, 0, 0]
dys = [0, 0, 1, -1]

def oob(x, y):
    return True if (0 <= x < n and 0 <= y < n) else False

n = int(input())
board = [
    list(map(int, input().split()))
    for _ in range(n)
]
max_height = max(map(max, board))
ans = 0

for height in range(max_height):
    vis = [
        [False for _ in range(n)]
        for _ in range(n)
    ]
    tmp = 0
    for i in range(n):
        for j in range(n):
            if not vis[i][j] and board[i][j] > height:
                de = deque([(i, j)])
                vis[i][j] = True
                while de:
                    cur_x, cur_y = de.popleft()
                    for dir in range(4):
                        nxt_x, nxt_y = cur_x + dxs[dir], cur_y + dys[dir]
                        if oob(nxt_x, nxt_y):
                            if not vis[nxt_x][nxt_y] and board[nxt_x][nxt_y] > height:
                                de.append((nxt_x, nxt_y))
                                vis[nxt_x][nxt_y] = True
                                
                tmp += 1
    ans = max(ans, tmp)

print(ans)