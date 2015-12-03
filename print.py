import sys
test=int(input())
while test>0:
    a,b,n,m=map(int,sys.stdin.readline().split())
    spam=[]
    spam.append(a)
    spam.append(b)
    for i in range(2,n):
        x=a+b
        a=b
        b=x
        z=x%m
        spam.append(z)
    spam.sort()
    xy=spam[0]
    count=1
    tcount=0
    for i in range(1,n):
        if spam[i]==xy:
            count=count+1
        else:
            tcount+=(count*count)
            xy=spam[i]
            count=1

    tcount+=(count*count)
    print(tcount)
    test=test-1
    
