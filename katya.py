def clean_tokens (formatted_text):
    answers = []
    for i in range(len(cleaned_tokens)):
        if (i+1) == 10:
            answers += i
            cleaned_tokens[i] = "___"
            task = " ".join(cleaned_tokens)
    return task, answers
