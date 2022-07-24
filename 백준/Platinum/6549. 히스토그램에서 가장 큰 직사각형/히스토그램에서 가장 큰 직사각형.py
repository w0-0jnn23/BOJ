from collections import deque
import sys

while True:
    rec = list(map(int, sys.stdin.readline().split()))
    n = rec.pop(0)
    
    if n == 0:
        break

    stack = deque()
    ans = 0
    
    for i in range(n):
        while stack and rec[stack[-1]] > rec[i]:
            temp = stack.pop()
            
            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1] - 1
            ans = max(ans, width * rec[temp])
        stack.append(i)
            
    while stack:
        temp = stack.pop()
        
        if len(stack) == 0:
            width = n
        else:
            width = n - stack[-1] - 1
        ans = max(ans, width * rec[temp])
        
    print(ans)