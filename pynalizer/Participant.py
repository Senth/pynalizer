from .WordCounter import count_words


class Participant:
    def __init__(self, name):
        self.name = name
        self.messages = []
        self.words = {}
        self.sorted_list = []
        self.word_count = 0

    def add_message(self, message):
        self.messages.append(message)

    def count_words(self):
        self.words = count_words(self.messages)

    def get_sorted_word_list(self):
        if len(self.sorted_list) == 0:
            return sorted(self.words.items(), key=lambda kv: kv[1], reverse=True)
        else:
            return self.sorted_list
