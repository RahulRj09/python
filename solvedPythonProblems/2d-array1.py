a = []
tot = 0
list1 = []
for i in range(6):
    l = input()
    l = l.split()
    a.append(l)
for i in a:
    for x in range(6):
        i[x] = int(i[x])
i,j = 0,0
for i in range(4):
    for j in range(4):
        tot = a[i][j]+a[i][j+1]+a[i][j+2]
        tot = tot + a[i+2][j]+a[i+2][j+1]+a[i+2][j+2]
        tot = tot + a[i+1][j+1]
        list1.append(tot)
print(max(list1))
