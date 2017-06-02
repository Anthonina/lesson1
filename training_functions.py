def get_summ(parameter_1, parameter_2):
    parameter_2_str = str(parameter_2)
    result = parameter_1 + parameter_2_str
    return result

summ_1 = get_summ('Привет', 2)
print(summ_1)


def get_summ_1(parameter_1_1, parameter_2_1, delimeter = ' '):
    result = str(parameter_1_1) + str(delimeter) + str(parameter_2_1)
    result_upper = result.upper()
    return result_upper

summ_1 = get_summ_1('Привет', 'мир')
print(summ_1)
