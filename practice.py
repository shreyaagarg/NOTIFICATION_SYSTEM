T = int(input())

for _ in range(T):

    N,Q = [int(i) for i in input().split()]
    list = [int(i) for i in input().split()]
    numbers  = {}
    j = 0

    for i in list:
        numbers.update({i:j})
        j += 1

    for k in range(Q):
        count = 0
        X = int(input())
        index = numbers[X]
        found = -1
        a = 0
        b = N-1
        while True:
            mid = (a + b)//2
            if list[mid] == X:
                break
            elif index > mid and list[mid] > X:
                count += 1
                a = mid + 1
            elif index < mid and list[mid] < X:
                count += 1
                b = mid - 1
            elif index > mid and list[mid] < X:
                a = mid + 1
            elif index < mid and list[mid] > X:
                b = mid - 1


        print(count)