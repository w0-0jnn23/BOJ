T = int(input())

for _ in range(T):
    N = int(input())
    num_zero = 1
    num_one = 0
    temp = 0
    
    for __ in range(N):
        temp = num_one
        num_one = num_one + num_zero
        num_zero = temp
    
    print(num_zero, num_one)