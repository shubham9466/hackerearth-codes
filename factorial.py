x=int(input())
while x>0:
    num=int(input())
    fact=1
    if num==0 or num==1:
        print('1')
    elif num>1:
        for i in range(1,num+1):
            fact=fact*i
        print(fact)
    x=x-1
