import random
import csv
import pandas as pd
import statistics as stats
import plotly.figure_factory as pff



df = pd.read_csv('StudentsPerformance.csv')
avg_marks = df["math score"]+df["reading score"]+df["writing score"].tolist()

mean = stats.mean(avg_marks)
median = stats.median(avg_marks)
mode = stats.mode(avg_marks)


#fig.show()


stdev = stats.stdev(avg_marks)
print('mean = ',mean)
print('median = ',median)
print('mode = ',mode)
print('stdev = ',stdev)



first_stdev_start, first_stdev_end = mean-stdev , mean+stdev
second_stdev_start, second_stdev_end = mean-(2*stdev) , mean+(2*stdev)
third_stdev_start, third_stdev_end = mean-(3*stdev), mean +(3*stdev)

list_of_data_within_1_std_deviation = [result for result in avg_marks if result > first_stdev_start and result < first_stdev_end]
print("{}% of data lies within one standard deviation".format(len(list_of_data_within_1_std_deviation)*100/len(avg_marks)))


list_of_data_within_2_std_deviation = [result for result in avg_marks if result > second_stdev_start and result < second_stdev_end]
print("{}% of data lies within two standard deviation".format(len(list_of_data_within_2_std_deviation)*100/len(avg_marks)))

list_of_data_within_3_std_deviation = [result for result in avg_marks if result > third_stdev_start and result < third_stdev_end]
print("{}% of data lies within three standard deviation".format(len(list_of_data_within_3_std_deviation)*100/len(avg_marks)))