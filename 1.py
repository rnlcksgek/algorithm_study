a = int(input())
list1 = [a]
cnt = 0
while True:
    if 1 in list1:
        print(cnt)
        break
    temp = []
    for i in list1:
        if i%3 == 0:
            temp.append(i//3)
        if i%2 == 0:
            temp.append(i//2)
        temp.append(i-1)
    cnt += 1
    list1 = temp
