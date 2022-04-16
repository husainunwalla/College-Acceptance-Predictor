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
    def __init__(self, id, label, option1, option2):
        self.id = id
        self.label = label
        self.option1 = option1
        self.option2 = option2
    def get_questions():
        questions = []
        questions.append(PersonalityQuestions(id='ques_1', label='Question 1', option1='expend energy, enjoy groups', option2='conserve energy, enjoy one-on-one'))
        questions.append(PersonalityQuestions(id='ques_2', label='Question 1', option1='expend energy, enjoy groups', option2='conserve energy, enjoy one-on-one'))
        questions.append(PersonalityQuestions(id='ques_3', label='Question 1', option1='expend energy, enjoy groups', option2='conserve energy, enjoy one-on-one'))
        questions.append(PersonalityQuestions(id='ques_4', label='Question 1', option1='expend energy, enjoy groups', option2='conserve energy, enjoy one-on-one'))
        questions.append(PersonalityQuestions(id='ques_5', label='Question 1', option1='expend energy, enjoy groups', option2='conserve energy, enjoy one-on-one'))
        questions.append(PersonalityQuestions(id='ques_6', label='Question 1', option1='expend energy, enjoy groups', option2='conserve energy, enjoy one-on-one'))
        questions.append(PersonalityQuestions(id='ques_7', label='Question 1', option1='expend energy, enjoy groups', option2='conserve energy, enjoy one-on-one'))
        questions.append(PersonalityQuestions(id='ques_8', label='Question 1', option1='expend energy, enjoy groups', option2='conserve energy, enjoy one-on-one'))
        questions.append(PersonalityQuestions(id='ques_9', label='Question 1', option1='expend energy, enjoy groups', option2='conserve energy, enjoy one-on-one'))
        questions.append(PersonalityQuestions(id='ques_10', label='Question 1', option1='expend energy, enjoy groups', option2='conserve energy, enjoy one-on-one'))
        questions.append(PersonalityQuestions(id='ques_11', label='Question 1', option1='expend energy, enjoy groups', option2='conserve energy, enjoy one-on-one'))
        questions.append(PersonalityQuestions(id='ques_12', label='Question 1', option1='expend energy, enjoy groups', option2='conserve energy, enjoy one-on-one'))
        questions.append(PersonalityQuestions(id='ques_13', label='Question 1', option1='expend energy, enjoy groups', option2='conserve energy, enjoy one-on-one'))
        questions.append(PersonalityQuestions(id='ques_14', label='Question 1', option1='expend energy, enjoy groups', option2='conserve energy, enjoy one-on-one'))
        questions.append(PersonalityQuestions(id='ques_15', label='Question 1', option1='expend energy, enjoy groups', option2='conserve energy, enjoy one-on-one'))
        questions.append(PersonalityQuestions(id='ques_16', label='Question 1', option1='expend energy, enjoy groups', option2='conserve energy, enjoy one-on-one'))
        questions.append(PersonalityQuestions(id='ques_17', label='Question 1', option1='expend energy, enjoy groups', option2='conserve energy, enjoy one-on-one'))
        questions.append(PersonalityQuestions(id='ques_18', label='Question 1', option1='expend energy, enjoy groups', option2='conserve energy, enjoy one-on-one'))
        questions.append(PersonalityQuestions(id='ques_19', label='Question 1', option1='expend energy, enjoy groups', option2='conserve energy, enjoy one-on-one'))
        questions.append(PersonalityQuestions(id='ques_20', label='Question 1', option1='expend energy, enjoy groups', option2='conserve energy, enjoy one-on-one'))
        return questions

def generate_secret_key():
    return os.urandom(16)