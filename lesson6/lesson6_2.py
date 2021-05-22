# def print_name_surname(name, surname):
#     print(name)
#     print(surname)
#     print ('Ваше имя', name)
#     print ('Фамилия ', surname)
# print_name_surname(input(), input())

def print_name_list(names_list):
    for i in names_list:
        print()
        print_name_list(i[0],i[1])

print_name_list([['qwerty','asdasdasd'], ['erergdfg','asdasdasdasd']])
