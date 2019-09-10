import pandas as  pd
import argparse
import csv
import vehicle_detection_main_upd as detect
import os
import sys

parser = argparse.ArgumentParser(description='Vehicle Detection and Classified Counting')
parser.add_argument('--csv',required=True, help='Path to csv file with the video links.')
parser.add_argument('--model',required=False ,help = 'Path to the model you want to use. Default is Faster Rcnn Resnet50.')
parser.add_argument('--outpath',required=True,help = 'Path to the output file where you want to store the updated count.')
parser.add_argument('--outfile',required=True,help = 'Name of the csv file along with the csv extension which gets updated with the count. ')
args = parser.parse_args()

if(args.csv):
    if not os.path.isfile(args.csv):
        print("Input csv file ", args.csv, " doesn't exist")
        sys.exit(1)
    survey = pd.read_csv(args.csv,delimiter=',')
else:
    print("Error . Please Provide a csv file as an argument.")
    sys.exit(1)

if(args.model):
    if not os.path.exists(args.model):
        print("Input model ", args.model, " doesn't exist")
        sys.exit(1)
    model_name = args.model
else:
    model_name = 'faster_rcnn_resnet50_coco_2018_01_28'

if(args.outpath):
    if not os.path.exists(args.outpath):
        print("The path given :",args.outpath, "Does not exist.")
        sys,exit(1)
    
    out_csv = args.outpath + '\\' + args.outfile
else:
    print("Error . Please Provide a path to store the output csv file.")
    sys.exit(1)




for i in range(len(survey)):
    v_link = survey['Video'][i]
    id = survey['id'][i]
    #print(v_link)
    result = detect.object_detection_function(v_link,model_name,id)
    
    survey.iat[i,9] = result[0]
    survey.iat[i,10] = result[1]
    survey.iat[i,11] = result[2]
    survey.iat[i,12] = result[3]
    survey.iat[i,13] = result[4]
    survey.iat[i,14] = result[5]
    survey.iat[i,15] = result[6]
    survey.iat[i,16] = result[7]
survey_csv = survey.to_csv(out_csv,index = None , header = True)
    



