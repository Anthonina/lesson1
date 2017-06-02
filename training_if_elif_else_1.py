def comparison_strings(first_string, second_string):
    if first_string == second_string:
        return 1
    elif first_string != second_string and len(first_string) > len(second_string):
        return 2
    elif first_string != second_string and second_string == 'learn':
        return 3
    else:
        return 4

first_pre_result = input('Введите первое значение: ')
second_pre_result = input ('Введите второе значение: ')
result = comparison_strings(first_pre_result, second_pre_result)
print(result)