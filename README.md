# vehicle_counting

#### This repo is based on the vehicle counting model of Ahmet ozlu : https://github.com/ahmetozlu/vehicle_counting_tensorflow
You need to add a model from the tensorflow model zoo - 

https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md into the directory.

## For detection on a single video file run : vehicle_detection_main.py 

You can run using the command - 
####  python vehicle_detection_main.py --video video_1_61.mp4 --model model_name
The model argument is optional and Faster_RCNN_resnet50 is the default model.

The roi line changes based on the height and width of your input.
This gives a classified count of the different vehicles - Cars, Trucks, Buses and Person.

## For detection and updation on a csv file run : survey_upd.py
### survey_upd.py file can be used to update a csv file with the counts of different vehicles.

To run the file use the command : 
#### python survey_upd.py --csv csv_file --model model_name --outpath path_to_the_folder_to_store_csv --outfile filename.csv

The model argument is optional and Faster_RCNN_resnet50 is the default model.
Make sure you give a unique file name otherwise it will be overwritten.
You also need to have the permissions to download/open the video in the video link of the csv file.

The Updated csv file will be stored in the given directory with the filename provided as argument.


