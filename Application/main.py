# importing the necessary dependencies
# Husain - Added new import for addional functionality
#from flask import Flask, render_template, request,jsonify
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
import pickle
import predict
import json
# Husain - class to store user type data

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

# Husain = create usersnames and passwords that will work during login
users = []
users.append(User(id=1, username='Husain', password='password'))
users.append(User(id=2, username='Jainam', password='password'))
users.append(User(id=3, username='Isha', password='password'))

# Jainam : initializing a flask app
app = Flask(__name__)

# Husain : Setting random secret key to store in session cookies
app.secret_key = 'somesecretkeythatonlyishouldknow'

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
            return redirect(url_for('form'))

        return redirect(url_for('login'))

    return render_template('login.html')

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

#Jainam : route to show the predictions in a web UI
'''@app.route('/predict', methods=['POST', 'GET'])
@cross_origin()
def index():
    #  reading the inputs given by the user
    gre_score = int(request.form['gre_score'])
    toefl_score = float(request.form['toefl_score'])
    university_rating = int(request.form['university_rating'])
    sop = float(request.form['sop'])
    lor = float(request.form['lor'])
    cgpa = float(request.form['cgpa'])
    is_research = request.form['research']
    if(is_research == 'yes'):
        research = 1
    else:
        research = 0
    filename = 'finalized_model.pickle'
    # loading the model file from the storage
    loaded_model = pickle.load(open(filename, 'rb'))
    # predictions using the loaded model file
    prediction = loaded_model.predict(
        [[gre_score, toefl_score, university_rating, sop, lor, cgpa, research]])
    #print('predicted value is', prediction)
    # showing the prediction results in a UI
    output = round(prediction[0], 2)*100
    return render_template('form.html', prediction_text='Admission chance is {}%'.format(output))
    # return render_template('index.html',prediction_text=round(100*prediction[0]))'''

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
    '''
    #  reading the inputs given by the user
    gre_score = int(request.form['gre_score'])
    toefl_score = float(request.form['toefl_score'])
    university_rating = int(request.form['university_rating'])
    sop = float(request.form['sop'])
    lor = float(request.form['lor'])
    cgpa = float(request.form['cgpa'])
    is_research = request.form['research']
    if(is_research == 'yes'):
        research = 1
    else:
        research = 0
    filename = 'finalized_model.pickle'
    # loading the model file from the storage
    loaded_model = pickle.load(open(filename, 'rb'))
    # predictions using the loaded model file
    prediction = loaded_model.predict(
        [[gre_score, toefl_score, university_rating, sop, lor, cgpa, research]])
    #print('predicted value is', prediction)
    # showing the prediction results in a UI
    output = round(prediction[0], 2)*100
    return render_template('form.html', prediction_text='Admission chance is {}%'.format(output))'''
    # return render_template('index.html',prediction_text=round(100*prediction[0]))

#Husain : dummy method to print message in javascript
@app.route('/test', methods=['GET', 'POST'])
def testfn():
    # GET request
    if request.method == 'GET':
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001)
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True)
