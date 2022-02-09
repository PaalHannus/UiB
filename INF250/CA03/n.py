
f = open("dataCheap.txt")
a = f.read().split()
#b = list(map(int, a))

a = list(a[:200])
l = len(a)
xs = []
ys = []
b = True
for i in a:
    if b:
        b = False
        xs.append(float(i))
    elif not b:
        b = True
        ys.append(float(i))


for i in range(len(ys)):
    print(f"{xs[i]} {ys[i]};")
#    p = a[i]
#    r = a[i+1]
#    print(p, r)
#for i in range(1, 2, len(a)):
#    x = a[i]




