import sys
test=int(input())
while test>0:
    m,n=map(int,sys.stdin.readline().split())
    #while n>0:
    z=0
    while m>=1:
        y=m%10
        z+=(y*y)
        m=m/10
     #   n=n-1
     #   m=z
    print(z)
    test=test-1
            
