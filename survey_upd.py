import pandas as  pd

import csv
import vehicle_detection_main_upd as detect
model = "faster_rcnn_resnet50_coco_2018_01_28"

survey = pd.read_csv('survey_s.csv',delimiter=',')



for i in range(len(survey)):
    v_link = survey['Video'][i]
    id = survey['id'][i]
    #print(v_link)
    result = detect.object_detection_function(v_link,id)
    #result=[1,2,3,4,5,6,7,8]
    survey.at[i,10] = result[0]
    
    survey.at[i,11] = result[1]
    survey.at[i,12] = result[2]
    survey.at[i,13] = result[3]
    survey.at[i,14] = result[4]
    survey.at[i,15] = result[5]
    survey.at[i,16] = result[6]
    survey.at[i,17] = result[7]
    



