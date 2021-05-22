name = input()
while len(name) < 8:
    print('Wrong password')
    name = input()
print(name)