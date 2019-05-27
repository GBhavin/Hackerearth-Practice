t=int(input())
while(t>0):
    a=input()
    b=input()
    k=0
    l1=len(a)
    l2=len(b)
    if(l1<=l2):
        for i in range(l1):
            if a[i] in b:
                k=k+1
                gh=b.index(a[i])
                b[gh]='0'
    else:
        for j in range(l2):
            if b[j] in a:
                k=k+1
                gh=a.index(b[j])
                a[gh]='0'
    print(l1+l2-2*k)
    t-=1
