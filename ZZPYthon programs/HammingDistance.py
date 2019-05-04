













def is_isogram(word):
    matched_characters = []
    for character in word.lower():
        if character.isalpha():
            if character in matched_characters:
                return False
            matched_characters += character
    return True




def doit():
       word = 'lumberjacks'
       value = is_isogram(word)
       print(value)