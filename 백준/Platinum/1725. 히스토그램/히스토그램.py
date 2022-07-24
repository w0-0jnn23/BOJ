import sys

n = int(sys.stdin.readline())
graph = []
result = 0
left = 0
a = 0

for _ in range(n):
    graph.append(int(sys.stdin.readline()))

graph.append(0)
stack = [(0, graph[0])]

for now in range(1, n+1):
    left = now
    while stack and stack[-1][1] > graph[now]:
        left, temp = stack.pop()
        result = max(result, (now - left) * temp)
    stack.append((left, graph[now]))
    
print(result)