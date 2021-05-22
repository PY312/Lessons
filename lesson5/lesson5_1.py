x = ['Список задач', 'Добавить задачу']
tasks = []
deadline = []
date = []
while True:
    print(f'\nВыберите операцию:  \n1. {x[0]}\n2. {x[1]}')
    a = int(input())
    if a == 1:
        if len(tasks) != 0:
            j = 0
            print('   Добавить задачу: ')
            for i in tasks:
                print(f'{tasks.index(i) + 1}. {i}, {deadline[j]}, {date[j]}')
                j += 1
        else:
            print('Список пуст')
    elif a == 2:
        print('Добавить задачу:')
        tasks = tasks + [input('Название задачи: ')]
        deadline = deadline + [input('Сроки исполнения: ')]
        date = date + [input('Дата заполнения: ')]
        print('Задача добавлена')
    else:
        print('Не верно выбрана команда!')

