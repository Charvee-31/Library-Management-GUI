#build a translator such that it converts the letter c to letter k and vice versa
def translate(phrase):
    translation=""
    for letter in phrase:
        if letter in "Cc":
            if letter.isupper():
                translation=translation+"K"
            else:
                translation=translation+"k"
        elif letter in "Kk":
            if letter.isupper():
                translation=translation+"C"
            else:
                translation=translation+"c"
        elif letter in "AEIOUaeiou":
            translation=translation+"~"
        else:
            translation=translation+letter
    return translation

sentence="Hello! How are you this evening?\nMy name is Kate\nI have completed my masters in mass communication "
print(translate(sentence))