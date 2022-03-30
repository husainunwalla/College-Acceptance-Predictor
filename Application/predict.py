import pandas as pd 
import os
from os.path import dirname, abspath 
from joblib import load


def predict_all(gre_score, toefl_score,  sop, lor, cgpa, research):
        this_folder = os.path.dirname(os.path.abspath(__file__))
        parent_folder = dirname(dirname(abspath(__file__)))
        uni_data_path = os.path.join(this_folder, 'uni_dataset.csv')
        df=pd.read_csv(uni_data_path, usecols = ['School Name','Acceptance rate'])
        list_json = []
        i=0

        filename = os.path.join(parent_folder + '/Model' , 'filename.joblib')
        # loading the model file from the storage
        loaded_model = load(filename) 
        university_rating = 1
        for index, row in df.iterrows():
                i+= 1
                #limit number of unis
                #if i >= 20: break
                
                temp_json = {}
                temp_json['name'] = row[0]

                '''if(row[1] < 5):
                        university_rating = 5
                elif(row[1] < 20):
                        university_rating = 4
                elif(row[1] < 40):
                        university_rating = 3
                elif(row[1] < 60):
                        university_rating = 2
                else:
                        university_rating = 1'''
                university_rating = int(row[1])
                

                # predictions using the loaded model file
                prediction = loaded_model.predict([[gre_score, toefl_score, university_rating, sop, lor, cgpa, research]])
                #print('predicted value is', prediction)
                # showing the prediction results in a UI
                output = round(float(prediction[0]*100) , 2)
                if output>=100 : output = 99.99
                if output <= 0 : output = 0.01
                temp_json['val'] = output
                temp_json['rating'] = university_rating
                list_json.append(temp_json)
                
        return list_json