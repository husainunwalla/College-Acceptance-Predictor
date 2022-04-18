from colorama import init
from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
    jsonify
)
from flask_cors import  cross_origin
import predict
import dynamic.utility as utility
from dynamic.utility import University, User, PersonalityQuestions, generate_secret_key, init_global_variables
from dynamic.personality import find_personality

questions = PersonalityQuestions.get_questions();
users = User.get_users();
app = Flask(__name__)
app.secret_key = generate_secret_key()

@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('home'))
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/home', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form['Form'] == 'Go to Form':
            return redirect(url_for('form', personality = utility.default_personality_type))
        if request.form['Form'] == 'Go to Personality test':
            return redirect(url_for('personality'))
    return render_template("home.html")

@app.route('/personality' , methods = ['GET', 'POST'])
def personality():
    return render_template("personality.html" , ques = questions)

@app.route('/form', methods=['GET', 'POST'])
def form():
    personality = request.args['personality']
    return render_template("form.html", my_personality = personality)

@app.route('/', methods=['GET'])
@cross_origin()
def homePage():
    return redirect(url_for('login'))

@app.route('/predictAll', methods=['POST', 'GET'])
def predict_all():
    gre_score = int(request.form['gre_score'])
    toefl_score = float(request.form['toefl_score'])
    cgpa = float(request.form['cgpa'])
    is_research = request.form['research']
    personality = request.form['personality']
    if(is_research == 'yes'):
        research = 1
    else:
        research = 0
    predicted = (predict.predict_all(gre_score, toefl_score,personality, cgpa, research))
    unis = []
    for x in predicted:
        unis.append(University(x['name'], x['val'], x['personality']))
    print(type(unis))
    return render_template("table.html", unis = unis, personality = personality)

@app.route('/predictPersonality', methods=['POST'])
def predict_personality():
    answers = []
    if request.method == 'POST':
        for question in questions:
            answers.append(request.form.get(question.id))
        personality_type = find_personality(answers)
        global current_personality
    return redirect(url_for('form', personality = personality_type))

if __name__ == "__main__":
    init_global_variables()
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True)