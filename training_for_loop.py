# -*- coding: utf-8 -*-
#numbers = [1, 7, 33, 56, 25, 89, 100, 5, 29, 60]
#for number in numbers:
#    print(number + 1)

#string = input('Введите что-нибудь: ')
#for letter in string:
 #   print(letter)




school_1234 = [
    {'school_class': '1А', 'scores': [5, 5, 5, 4, 3, 5]},
    {'school_class': '1Б', 'scores': [3, 4, 4, 5, 3, 5]},
    {'school_class': '2A', 'scores': [5, 3 ,3, 4, 5, 2]},
    {'school_class': '2Б', 'scores': [5, 5, 5, 5, 5, 5]},
    {'school_class': '3А', 'scores': [5, 3, 5, 2, 3, 5]},
    {'school_class': '3Б', 'scores': [3, 5, 5, 5, 5, 4]},
    {'school_class': '4А', 'scores': [4, 4, 4, 4, 4, 5]},
    {'school_class': '4Б', 'scores': [3, 5, 4, 5, 5, 3]}
]

total_sum = 0
total_len = 0

for school_class in school_1234:
    scores = school_class.get('scores')
    local_sum = sum(scores)
    total_sum = total_sum + local_sum
    local_len = len(scores)
    total_len = total_len + local_len

    print('В классе {0} средний балл {1}'.format(school_class.get('school_class'), round(local_sum/local_len, 1)))

print('В школе средний балл {}'.format(round(total_sum/total_len, 1)))