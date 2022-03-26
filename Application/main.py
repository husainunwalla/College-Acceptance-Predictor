
# importing the necessary dependencies
#Husain - Added new import for addional functionality
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
from flask_cors import CORS,cross_origin
import pickle
import pandas as pd

#Husain - class to store user type data
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='Husain', password='password'))
users.append(User(id=2, username='Jainam', password='password'))
users.append(User(id=3, username='Isha', password='password'))

app = Flask(__name__) # initializing a flask app
app.secret_key = 'somesecretkeythatonlyishouldknow'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return render_template("form.html")

        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    return redirect(url_for('form'))

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    #Husain - changed default route to login
    #return render_template("index.html")
    return redirect(url_for('login'))

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
            #  reading the inputs given by the user
            gre_score=int(request.form['gre_score'])
            toefl_score = float(request.form['toefl_score'])
            university_rating = int(request.form['university_rating'])
            sop = float(request.form['sop'])
            lor = float(request.form['lor'])
            cgpa = float(request.form['cgpa'])
            is_research = request.form['research']
            if(is_research=='yes'):
                research=1
            else:
                research=0
            filename = 'finalized_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[gre_score,toefl_score,university_rating,sop,lor,cgpa,research]])
            #print('predicted value is', prediction)
            # showing the prediction results in a UI
            output = round(prediction[0], 2)*100
            return render_template('form.html', prediction_text='Admission chance is {}%'.format(output))
            #return render_template('index.html',prediction_text=round(100*prediction[0]))
        
if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001)
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug = True)