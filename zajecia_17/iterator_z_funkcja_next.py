import random
import string


class PasswordIterator:
    def __init__(self, limit):
        self.limit = limit
        self.position = 0
        self.letters = string.ascii_letters
        print(self.letters)

    def get_random_letter(self):
        return random.choice(self.letters)

    def __iter__(self):
        return self

    def __next__(self):
        print("wywolanie nexta")
        if self.position < self.limit:
            self.position += 1
            return self.get_random_letter()
        else:
            raise StopIteration()

password_iterator = PasswordIterator(limit=32)
for letter in password_iterator:
    print(letter)
next(password_iterator)
next(password_iterator)
next(password_iterator)
