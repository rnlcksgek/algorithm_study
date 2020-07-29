#시간초과
def quick(unsorted):
    if len(unsorted) <= 1:
        return unsorted
    pivot = unsorted[-1]
    maximum, minimum, equal = [], [], []
    for i in unsorted:
        if pivot[0] < i[0]:
            maximum.append(i)
        elif pivot[0]> i[0]:
            minimum.append(i)
        else:
            if check.index(pivot) < check.index(i):
                maximum.append(i)
            elif check.index(pivot) > check.index(i):
                minimum.append(i)
            else:
                equal.append(pivot)
    return quick(minimum)+equal+quick(maximum)

import sys
n = int(sys.stdin.readline().strip())
list1 = [sys.stdin.readline().strip().split() for i in range(n)]
check = list1[:]
for i in quick(list1):
    print(*i)