import re
cleaned_tokens = re.findall('\b[a-zA-Z]\b', text)

answers = []
for i in range(len(cleaned_tokens)):
    if (i+1) == 10:
        answers += i
        cleaned_tokens[i] = "___"

task = " ".join(cleaned_tokens)

    