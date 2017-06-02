def get_answer(question):
    if question == 'Как дела?':
        answer = 'Хорошо'
    elif question == 'Что делаешь?':
        answer = 'Занимаюсь'
    else:
        answer = 'Не понимаю вопрос'

    return answer




def ask_user():
    while True:
        question = input('Введите вопрос: ')
        if question == 'Пока':
            break
        else:
            print(get_answer(question))
ask_user()