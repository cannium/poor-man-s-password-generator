import random

words = []
with open('./dict.txt') as f:
    for line in f:
        w = line.strip()
        if w != '' and len(w) < 7:
            words.append(w)


print random.choice(words) + \
    str(random.randint(0,99)) + \
    random.choice(words).capitalize()