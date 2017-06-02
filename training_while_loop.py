find_name = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']
print(find_name)
x = 0
while x < len(find_name): # Пока индекс меньше количества элементов в списке...
    if find_name[x] == 'Валера': # Если элемент с индексом X равен значению "Валера"
        valera = find_name.pop(x) # Заводим переменную

        print('{} нашёлся'.format(valera))
    x = x + 1    
print(find_name)


