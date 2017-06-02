def get_occupation(age):
    if age < 7:
        occupation = 'Воспитанник детского сада'
    elif age < 18:
        occupation = 'Школьник'
    elif age < 23:
        occupation = 'Студент'
    else:
        occupation = 'Кто-то'
    
    return occupation

ages = input('Сколько Вам лет: ')
result = get_occupation(int(ages))
print (result)
