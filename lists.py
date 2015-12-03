roomies=[]
print('Enter the name of all the roomies:')
while True:
    name=input()
    if name=='':
        break
    roomies=roomies+[name]
print('The name of the roomies are')
for i in roomies:
    print(' '+ i)
