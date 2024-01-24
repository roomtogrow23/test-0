def hanoi_tower(n, fr, tmp, to) :
    global count
    count+=1
    
    if (n == 1):
        print("원판 1: %s --> %s" %(fr,to))
    else :
        hanoi_tower(n-1, fr, to, tmp)
        print("원판 %d: %s --> %s" %(n,fr,to))
        hanoi_tower(n-1, tmp, fr, to)

count = 0
print("=====1개일 때=====")
hanoi_tower(1, 'A', 'B', 'C')
print("총횟수 : ", count)

count = 0
print("=====2개일 때=====")
hanoi_tower(2, 'A', 'B', 'C')
print("총횟수 : ", count)

count = 0
print("=====3개일 때=====")
hanoi_tower(3, 'A', 'B', 'C')
print("총횟수 : ", count)

count = 0
print("=====4개일 때=====")
hanoi_tower(4, 'A', 'B', 'C')
print("총횟수 : ", count)
