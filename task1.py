students = ['Иванов', 'Петров', 'Сидоров', 'Иванов']

# добавляем студента
def addStudent():
    name = input('Кого добавить? (можете ввести несколько студентов через пробел)\n')
    students.extend(name.split())

# ищем в списке имя студента, оно может встречаться неоднократно, возвращаем массив индексов найденного имени
def findStudentsNums(name):
    nums = []
    i = 0
    while True:
        try:
            nums.append(students.index(name, i))
            i = students.index(name, i) + 1
        except ValueError:
            break
    return nums

# удаляем студентов
def delStudent():
    name = input('Кого удалить? (можете ввести несколько студентов через пробел)\n')
    for n in name.split():
        nums = findStudentsNums(n)
        if len(nums) > 1:
            print('В списке найдены несколько студентов с именем %s, их номера: %s' % (n, ', '.join(map(str, map(lambda x: x + 1, nums)))))
            try:
                numToDelete = int(input(f'Введите номер студента с именем {n}, которого желаете удалить\n'))
                if numToDelete - 1 in nums:
                    students.pop(numToDelete - 1)
                    print('Студент %s удалён из списка' % n)
                else:
                    print('Неверный ввод')
            except ValueError:
                print('Неверный ввод')
        elif len(nums) == 1:
            students.pop(nums[0])
            print('Студент %s удалён из списка' % n)
        else:
            print('Студент %s не найден в списке' % n)

# ищем студентов
def findStudent():
    name = input('Кого хотите найти? (можете ввести несколько студентов через пробел)\n')
    for n in name.split():
        nums = findStudentsNums(n)
        if nums:
            print('Студент(ы) %s в списке под номером(ами) %s' % (n, ', '.join(map(str, map(lambda x: x + 1, nums)))))
        else:
            print('Студент %s не найден в списке' % n)


while True:
    print('Список студентов:', ', '.join(students))
    oper = input('Какую операцию хотите выполнить? (1 - добавить студента, 2 - удалить студента, 3 - найти студента, 0 - выход из программы)\n')
    match oper:
        case '1':
            addStudent()
        case '2':
            delStudent()
        case '3':
            findStudent()
        case '0':
            break
        case _:
            print('Неверный ввод')






