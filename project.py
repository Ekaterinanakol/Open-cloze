def display_text_with_gaps(quiz_text):
    formatted_text = " ".join(quiz_text)
    print("Текст с пропусками:")
    print(formatted_text)


def get_answers(num_gaps):
    answers = []
    for i in range(num_gaps):
        answer = input(f"Ответ для пропуска {i+1}: ").strip()
        answers.append(answer)
    return answers
