birthdays={'alice':'April 1','shubham':'march 30','sumedha':'aug 3'}
while True:
    print('Enter a name:(Blank to Quit)')
    name = input()
    if name=='':
        break
    if name in birthdays:
        print(birthdays[name]+' is the birthday of '+name)
    else:
        print('New data for '+name)
        bday=input()
        birthdays[name]=bday
        print('Birthday database updated')

