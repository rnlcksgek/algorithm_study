a = int(input())
if a <= 20:
    b = 0
else:
    b = a - (len(str(a))*9)
while a >= b:
    if a == b + sum(list(map(int,str(b)))):
        break
    b+=1
print([0,b][b<=a])