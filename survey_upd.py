import pandas as  pd

import csv
import vehicle_detection_main_upd as detect


survey = pd.read_csv('su.csv',delimiter=',')



for i in range(len(survey)):
    v_link = survey['Video'][i]
    id = survey['id'][i]
    #print(v_link)
    result = detect.object_detection_function(v_link,id)
    
    survey.iat[i,9] = result[0]
    survey.iat[i,10] = result[1]
    survey.iat[i,11] = result[2]
    survey.iat[i,12] = result[3]
    survey.iat[i,13] = result[4]
    survey.iat[i,14] = result[5]
    survey.iat[i,15] = result[6]
    survey.iat[i,16] = result[7]
survey_csv = survey.to_csv(r'C:\Users\HP\Desktop\Intrn\vehicle_counting_tensorflow\export.csv',index = None , header = True)
    



