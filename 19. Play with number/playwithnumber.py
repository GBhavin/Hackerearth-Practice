a, b = map(int, input().split())
c = list(map(int, input().split()))
z = []
ans = 0
for i in range(0, a):
    ans += c[i]
    z.append(ans)
#print(z)
for i in range(0, b):
    d, e = map(int, input().split())
    if(d == 1):
        print((z[e-1])//(e-d+1))
    else:
        print((z[e-1]-z[d-2])//(e-d+1))
