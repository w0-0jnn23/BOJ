n = int(input())

X = [0 for _ in range(n+1)]

for i in range(2, n+1):
    X[i] = X[i-1] + 1
    
    if i % 2 == 0:
        X[i] = min(X[i], X[i//2] + 1)
    
    if i % 3 == 0:
        X[i] = min(X[i], X[i//3] + 1)

print(X[n])