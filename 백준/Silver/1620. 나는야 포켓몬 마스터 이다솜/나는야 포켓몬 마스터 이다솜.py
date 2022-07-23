import sys

N, M = map(int, sys.stdin.readline().split())

Name = [None for i in range(N)]
Num = {}

for i in range(N):
    Name[i] = sys.stdin.readline().strip()
    Num[Name[i]] = i

for _ in range(M):
    q = input()
    if q.isnumeric():
        q = int(q)
        print(Name[q-1])
    else:
        print(Num[q] + 1)