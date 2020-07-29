 '''n = int(input())
list1 = [list(map(int,input().split())) for i in range(n)]
result = []
while len(list1)!=0:
   for i in list1:
       cnt = 0
       x = i[0]
       y = i[1]
       for j in list1:
           if x > j[0]:
               cnt = 1
               break
           elif x==j[0]:
               if y > j[1]:
                   cnt =1
                   break
       if cnt == 0:
           result.append(i)
           list1.remove(i)
for i in result:
   print(*i)  시간초과 '''

'''import sys
n = int(sys.stdin.readline())
list1 = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
result = []
while len(result) < n:
    x = list1[0][0]
    y = list1[0][1]
    for j in list1:
        if x > j[0]:
            x = j[0]
            y = j[1]
        elif x==j[0]:
            if y > j[1]:
                y= j[1]
    result.append([x,y])
    list1.remove([x,y])

for i in range(len(result)):
    print(result[i][0],result[i][1])'''

'''import sys

n = int(sys.stdin.readline())
list1 = [sys.stdin.readline().split() for i in range(n)]
for i in range(n):
    x = list1[0][0]
    y = list1[0][1]
    for j in list1:
        if x > j[0]:
            x = j[0]
            y = j[1]
        if x == j[0]:
            if y > j[1]:
                y = j[1]
    print(x, y)
    list1.remove([x, y]) 시간초과'''

'''import sys
n = int(sys.stdin.readline())
list1 = [sys.stdin.readline().split() for i in range(n)]
for i in range(n):
    a= min(list1)
    print(*a)
    list1.remove(a) 시간초과 '''

n = int(input())

list2 = [list(map(int, input().split())) for i in range(n)]
list2 = sorted(list2)
for i in list2:
    print(*i)

