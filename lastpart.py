def calculate_correct_answers(user_answers, correct_answers):
    result = 0
    for answer in range(len(correct_answers)):
        if user_answers[answer] == correct_answers[answer]:
            result+=1
    return result

