N, r, c = map(int, input().split())

visit = 0

while N != 0:
    N -= 1
    width = 2 ** N
    
    if r < width and c < width:
        visit += 0
        
    elif r < width and c >= width:
        visit += width ** 2
        c -= width
        
    elif r >= width and c < width:
        visit += width ** 2 * 2
        r -= width
        
    else:
        visit += width ** 2 * 3
        r -= width
        c -= width
        
print(visit)