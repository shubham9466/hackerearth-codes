import pprint
message='It was a bright cold day in April,and thr clockks were striking thirteen.'
count={}
for char in message:
    count.setdefault(char,0)
    count[char]=count[char]+1
print(pprint.format(2))
