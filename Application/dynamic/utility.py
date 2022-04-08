import os
class University:
    def __init__(self, name, val):
        self.name = name
        self.val = val

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
    def __repr__(self):
        return f'<User: {self.username}>'
    def get_users():
        users = []
        users.append(User(id=1, username='Husain', password='password123'))
        users.append(User(id=2, username='Jainam', password='password'))
        users.append(User(id=3, username='Isha', password='password'))
        return users

class PersonalityQuestions():
    def __init__(self, id, label):
        self.id = id
        self.label = label
    def get_questions():
        questions = []
        questions.append(PersonalityQuestions(id='ques_1', label='Question 1'))
        return questions

def generate_secret_key():
    return os.urandom(16)