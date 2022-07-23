import sys

sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x-1, y)
        
        return True
    return False
    
T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        y, x = map(int, input().split())
        graph[x][y] = 1
        
    count = 0
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                if dfs(i, j):
                    count += 1
    
    print(count)