import pandas as pd
import pickle 
import os

def predict_all(gre_score, toefl_score,  sop, lor, cgpa, research):
        df=pd.read_csv(r"uni_dataset.csv", usecols = ['School Name','Acceptance rate'])
        list_json = []
        i=0

        this_folder = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(this_folder, 'finalized_model.pickle')
        # loading the model file from the storage
        loaded_model = pickle.load(open(filename, 'rb'))
        university_rating = 1
        for index, row in df.iterrows():
                i+= 1
                #limit number of unis
                #if i >= 20: break
                
                temp_json = {}
                temp_json['name'] = row[0]

                '''if(row[1] < 5):
                        university_rating = -20
                elif(row[1] < 1):
                        university_rating = 1
                elif(row[1] < 20):
                        university_rating = 2
                elif(row[1] < 40):
                        university_rating = 3
                elif(row[1] < 60):
                        university_rating = 4
                else:
                        university_rating = 5'''
                university_rating = int(row[1])
                

                # predictions using the loaded model file
                prediction = loaded_model.predict([[gre_score, toefl_score, university_rating, sop, lor, cgpa, research]])
                #print('predicted value is', prediction)
                # showing the prediction results in a UI
                output = round(prediction[0]*100, 2)
                if output > 100 : output = 99.99
                temp_json['val'] = output
                temp_json['rating'] = university_rating
                list_json.append(temp_json)
                
        return list_json