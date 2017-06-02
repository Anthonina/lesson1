def get_answer(question):
    answers = {
        'привет': 'И тебе привет!',
        'как дела': 'Лучше всех',
        'пока': 'Увидимся'
    }
    return answers.get(question)

result = get_answer('Привет'.lower())
print(result)