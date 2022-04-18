import pandas as pd 
import os
from os.path import dirname, abspath 
from joblib import load
import dynamic.utility as utility


def predict_all(gre_score, toefl_score, personality ,cgpa, research):
        this_folder = os.path.dirname(os.path.abspath(__file__))
        parent_folder = dirname(dirname(abspath(__file__)))
        uni_data_path = os.path.join(this_folder, 'uni_dataset.csv')
        df=pd.read_csv(uni_data_path, usecols = ['School Name','Acceptance rate', 'Personality'])
        predicted_list = []
        filename = os.path.join(parent_folder + '/Model' , 'filename.joblib')
        # loading the model file from the storage
        loaded_model = load(filename) 
        university_rating = 1
        for index, row in df.iterrows():
                if personality != row[2] and personality!=utility.default_personality_type : continue
                current_uni = {}
                current_uni['name'] = row[0]
                university_rating = int(row[1])
                # predictions using the loaded model file
                prediction = loaded_model.predict([[gre_score, toefl_score, university_rating, cgpa, research]])
                #print('predicted value is', prediction)
                # showing the prediction results in a UI
                output = round(float(prediction[0]*100) , 2)
                if output>=100 : output = 99.99
                if output <= 0 : output = 0.01
                current_uni['val'] = output
                current_uni['rating'] = university_rating
                current_uni['personality'] = row[2]
                predicted_list.append(current_uni)
        return predicted_list