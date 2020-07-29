#시간 초과
def merge_sort(unsorted):
    if len(unsorted) == 1:
        return unsorted
    mid = len(unsorted) // 2
    return merge(merge_sort(unsorted[:mid]), merge_sort(unsorted[mid:]))


def merge(small, big):
    i = 0
    j = 0
    temp = []
    while (len(small) > i) & (len(big) > j):
        if small[i][0] < big[j][0]:
            temp.append(small[i])
            i += 1
        elif small[i][0] > big[j][0]:
            temp.append(big[j])
            j += 1
        else:
            if dex.index(small[i]) < dex.index(big[j]):
                temp.append(small[i])
                i += 1
            elif dex.index(small[i]) > dex.index(big[j]):
                temp.append(big[j])
                j += 1
    while len(small) > i:
        temp.append(small[i])
        i += 1
    while len(big) > j:
        temp.append(big[j])
        j += 1
    return temp


import sys
num = int(sys.stdin.readline().strip())
list1 = [sys.stdin.readline().strip().split() for i in range(num)]
dex = list1[:]
for i in merge_sort(list1):
    print(*i)