n, m = map(int, input().split())
noHeard = set()
noSeen = set()

ans_count = 0
ans = []

for _ in range(n):
    noHeard.add(input())
for _ in range(m):
    noSeen.add(input())

ans = list(noHeard & noSeen)

print(len(ans))
ans.sort()
for name in ans:
    print(name)