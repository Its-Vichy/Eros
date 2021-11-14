import random, string, requests

class Generator:
    def __init__(self):
        pass

    def get_password(self):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(10)) + '1337'

    def get_username(self):
        return 'RCA_' + ''.join(random.choice(string.ascii_lowercase) for i in range(15))