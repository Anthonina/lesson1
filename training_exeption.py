answers = {
    'привет': 'И тебе привет!',
    'как дела': 'Лучше всех',
    'пока': 'Увидимся'
}


def get_answer(question):
    return answers.get(question)


def ask_user(answers):
    try:
        while True:
            user_input = input('Введите вопрос: ')
            answer = get_answer(user_input)
            print(answer)

            if user_input == 'пока':
                break

    except KeyboardInterrupt:
        return 'Как жаль! До новых встреч'
        

ask_user(answers)

