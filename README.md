# vehicle_counting
You need to add a model from the tensorflow model zoo - https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md into the directory.

Change the model name in line 70 of vehicle_detection_main.py

You can run using the command -  python vehicle_detection_main.py --video "video_1_61.mp4"

Change the roi line based on the height and width of your input.

This gives a classified count of the different vehicles - Cars, Trucks, Buses and Person.

### survey_upd.py file can be used to update a csv file with the counts of different vehicles.

Update the .csv file similar to surveys.csv in line 7 of survey_upd.py and make sure you have the permissions.

In line 25 of survey_upd.py You can choose where to store the updated csv file.
