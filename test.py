import pandas as pd
import json
import os
import datetime

def get_distance_duration(file_path):
    with open(file_path, 'r') as f:
        this_json = json.load(f)

    for i in this_json['timelineObjects']:
        activitySegment = i.get('activitySegment')
        if activitySegment is not None:
            activityType = activitySegment.get('activityType')
            if activityType == "MOTORCYCLING":
                global distance
                global duration
                distance += activitySegment.get('distance')

                this_duration_end = int(activitySegment.get('duration').get('endTimestampMs'))
                this_duration_start = int(activitySegment.get('duration').get('startTimestampMs'))
                this_duration = this_duration_end - this_duration_start
                duration +=  this_duration

def get_distance_duration_for_a_period (period, root_file_path):


    for file in os.listdir(root_file_path):

        if int(file) in period:

            print (file)

            year_directory = os.path.join(root_file_path, file)

            for month in os.listdir(year_directory):
                month_file_path = os.path.join(year_directory, month)

                print (month_file_path)

                get_distance_duration(month_file_path)

                duration_format = datetime.timedelta(milliseconds=duration)
                print (duration_format)


    

    print ('duration:')
    print (duration_format)
    print ('\n')
    print ('distance:')
    print ( distance)

# initialise: 
distance = 0
duration = 0
this_root_file_path = 'C:\\Users\\clement.nicolas\\Documents\\GitHub\\ride_track\\Takeout\\Location History\Semantic Location History'

get_distance_duration_for_a_period(range(2019,2021), this_root_file_path)