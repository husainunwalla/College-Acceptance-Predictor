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
from flask_cors import CORS, cross_origin
import predict
from dynamic.utility import University, User, PersonalityQuestions, generate_secret_key

questions = PersonalityQuestions.get_questions();
users = User.get_users();

# Jainam : initializing a flask app
app = Flask(__name__)

# Husain : Setting random secret key to store in session cookies
app.secret_key = generate_secret_key()

# Husain : Used to show information on page after login
@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

# Husain : Page route to login page
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

#Page route to Home
@app.route('/home', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form['Form'] == 'Go to Form':
            return redirect(url_for('form'))
        if request.form['Form'] == 'Go to Personality test':
            return redirect(url_for('personality'))
    return render_template("home.html")

#Husain : Page Route to Personality
@app.route('/personality' , methods = ['GET', 'POST'])
def personality():
    return render_template("personality.html" , ques = questions)

# Husain : Page route to form page
@app.route('/form', methods=['GET', 'POST'])
def form():
    return render_template("form.html")

# Husain : Page route to home page
@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    # Husain - changed default route to login
    # return render_template("index.html")
    return redirect(url_for('login'))

#Husain : new predict method
@app.route('/predictAll', methods=['POST', 'GET'])
def predict_all():
    gre_score = int(request.form['gre_score'])
    toefl_score = float(request.form['toefl_score'])
    #university_rating = int(request.form['university_rating'])
    sop = float(request.form['sop'])
    lor = float(request.form['lor'])
    cgpa = float(request.form['cgpa'])
    is_research = request.form['research']
    if(is_research == 'yes'):
        research = 1
    else:
        research = 0
    predicted = (predict.predict_all(gre_score, toefl_score, sop, lor, cgpa, research))
    unis = []
    for x in predicted:
        unis.append(University(x['name'], x['val']))
    print(type(unis))
    return render_template("table.html", unis = unis)

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001)
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True)
