a=str(input())
dis, l, t = a.split()
dis = int(dis)
l = int(l)
t = int(t)
for i in range(l):
    x1, x2 = str(input()).split()
    dis-=(int(x2)-int(x1))
if dis <= t:
    print("Cm4k3r wo lai la!")
else:
    print("Oh No!")
