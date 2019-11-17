class Participant:
    def __init__(self, name):
        self.name = name
        self.messages = list()

    def addMessage(self, message):
        self.messages.append(message)
