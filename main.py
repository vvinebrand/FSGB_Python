# 1. Найдите сумму цифр трехзначного числа.
def f_task():
    num = int(input('Введите трехначное число: '))
    if 999 > num > 100:
        units = num % 10
        num = num // 10
        dozens = num % 10
        num = num // 10
        print(f'Сумма цифр трехзначного чисра равна {units+dozens+num}')
    else:
        print('Вы ввели не трехзначное число!')

# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
def sec_task():
    sum = int(input('Введите четное количество журавликов: '))
    if sum % 2 != 0:
        print('Вы ввели нечетное число!')
    else:
        g = int((sum/3)*2)
        b = int((sum/2)/2)
        print(f'Катя сделала {g} журавликов, а Петя и Сережа — {b}')


def third_task():


def fourth_task():







stp = True
while stp:
    print('\n1. Найдите сумму цифр трехзначного числа\n'
          '2. Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.\n '
          '  Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,\n '
          '  а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?\n'
          '3. Нахождение счастливого автобсуного билета\n'
          '4. Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,\n '
          '  если разрешается сделать один разлом по прямой между дольками'
          '\nЧтобы выйти из программы наберите 0')
    n = int(input('\nВведите номер задачи: '))
    if n == 1:
        f_task()
    elif n == 2:
        sec_task()
    elif n == 3:
        third_task()
    elif n == 4:
        fourth_task()
    else:
        print('Программа завершена')
        stp = False