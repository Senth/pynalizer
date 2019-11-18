import re


replace_with = {'^_^': '😊', '<3': '❤️', '❤': '❤️', ':)': '🙂', ':d': '😃', ':-d': '😛', ':*': '😙', ':-*': '😙', ';*': '😘', ';)': '😉', ':p': '😛'}

def word_normalizer(word):
    word = word.lower()

    if word in replace_with:
        word = replace_with[word]
    
    word = re.sub('[!\.\(\)\?\*,]', '', word)

    if len(word) == 0:
        return None

    return word

def word_filter(word):
    pass

def count_words(messages):
    words = {}
    for message in messages:
        for word in message.content.split():
            word = word_normalizer(word)
            if word is None:
                continue
            elif word in words:
                count = words[word] + 1
            else:
                count = 1

            words[word] = count
    return words
