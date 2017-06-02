find_name = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']
def find_person(name, find_name):
    x = 0
    while x < len(find_name): # Пока индекс меньше количества элементов в списке...
        if find_name[x] == name: # Если элемент с индексом X равен значению "Валера"
            valera = find_name.pop(x) # Заводим переменную

            return '{} нашёлся'.format(valera)
        x = x + 1    


print(find_person('Валера', find_name))

