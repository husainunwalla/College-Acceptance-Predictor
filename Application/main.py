
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle
import pandas as pd

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

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
            return render_template('index.html', prediction_text='Admission chance is {}%'.format(output))
            #return render_template('index.html',prediction_text=round(100*prediction[0]))
        


if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001)
	app.run(debug=True)