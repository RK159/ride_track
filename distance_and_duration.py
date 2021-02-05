import pandas as pd
import json
import os

from datetime import timedelta


def get_distance_duration(file_path):
#Get the total distance and duration for 1 json file

    with open(file_path, 'r') as f:
        try:
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

        except UnicodeDecodeError:
            pass

def get_distance_duration_for_a_period (period, root_file_path):
#Get the total distance and duration for a range of years. Need to provide the file path of the directory where all the years are

    for file in os.listdir(root_file_path):

        if int(file) in period:

            # print (file)

            year_directory = os.path.join(root_file_path, file)

            for month in os.listdir(year_directory):
                month_file_path = os.path.join(year_directory, month)

                # print (month_file_path)

                get_distance_duration(month_file_path)

    return duration, distance

# initialise: 
distance = 0
duration = 0
this_root_file_path = 'C:\\Users\\clement.nicolas\\Documents\\Google takeouts\\Takeout\\Location History\Semantic Location History'
period = range(2019,2021)


get_distance_duration_for_a_period(period,this_root_file_path)

duration_format = timedelta(milliseconds=duration)

print ('\n')
print ('period')
print (period)
print ('\n')

print ('Total duration over the period: ')
print (duration_format)
print ('\n')

distance_format = distance/1000
print ('Total distance over the period: (km)')
print (distance_format)
print ('\n')