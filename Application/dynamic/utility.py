import os

from sympy import per
class University:
    def __init__(self, name, val, personality):
        self.name = name
        self.val = val
        self.personality = personality

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
        questions.append(PersonalityQuestions(id='ques_2', label='Question 2', option1='more outgoing, think out loud', option2='more reserved, think to yourself'))
        questions.append(PersonalityQuestions(id='ques_3', label='Question 3', option1='seek many tasks, public activities, interaction with others', option2='seek private, solitary activities with quiet to concentrate'))
        questions.append(PersonalityQuestions(id='ques_4', label='Question 4', option1='external, communicative, express yourself', option2='internal, reticent, keep to yourself'))
        questions.append(PersonalityQuestions(id='ques_5', label='Question 5', option1='active, initiate', option2='reflective, deliberate'))
        questions.append(PersonalityQuestions(id='ques_6', label='Question 6', option1='interpret literally', option2='look for meaning and possibilities'))
        questions.append(PersonalityQuestions(id='ques_7', label='Question 7', option1='practical, realistic, experiential', option2='imaginative, innovative, theoretical'))
        questions.append(PersonalityQuestions(id='ques_8', label='Question 8', option1='standard, usual, conventional', option2='different, novel, unique'))
        questions.append(PersonalityQuestions(id='ques_9', label='Question 9', option1='focus on here-and-now', option2='look to the future, global perspective, “big picture'))
        questions.append(PersonalityQuestions(id='ques_10', label='Question 10', option1='facts, things, “what is', option2='ideas, dreams, “what could be,” philosophical'))
        questions.append(PersonalityQuestions(id='ques_11', label='Question 11', option1='logical, thinking, questioning', option2='empathetic, feeling, accommodating'))
        questions.append(PersonalityQuestions(id='ques_12', label='Question 12', option1='candid, straight forward, frank', option2='tactful, kind, encouraging'))
        questions.append(PersonalityQuestions(id='ques_13', label='Question 13', option1='firm, tend to criticize, hold the line', option2='gentle, tend to appreciate, conciliate'))
        questions.append(PersonalityQuestions(id='ques_14', label='Question 14', option1='tough-minded, just', option2='tender-hearted, merciful'))
        questions.append(PersonalityQuestions(id='ques_15', label='Question 15', option1='matter of fact, issue-oriented', option2='sensitive, people-oriented, compassionate'))
        questions.append(PersonalityQuestions(id='ques_16', label='Question 16', option1='organized, orderly', option2='flexible, adaptable'))
        questions.append(PersonalityQuestions(id='ques_17', label='Question 17', option1='plan, schedule', option2='unplanned, spontaneous'))
        questions.append(PersonalityQuestions(id='ques_18', label='Question 18', option1='regulated, structured', option2='easygoing, “live” and “let live"'))
        questions.append(PersonalityQuestions(id='ques_19', label='Question 19', option1='preparation, plan ahead', option2='go with the flow, adapt as you go'))
        questions.append(PersonalityQuestions(id='ques_20', label='Question 20', option1='control, govern', option2='latitude, freedom'))
        return questions

def generate_secret_key():
    return os.urandom(16)

def init_global_variables():
    global default_personality_type
    default_personality_type = 'All'