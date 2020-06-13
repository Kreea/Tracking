import sys
import math
import date_util

start_date = 201905000000 #The start day is day 0 of may, aka april 30

if len(sys.argv) > 1:
    hist_file = sys.argv[1]
else:
    hist_file = 'history_out.csv'
start_date = date_util.date_interp(start_date)

total = [[0], [0.0]]
total_out = [[0], [0.0]]
total_in = [[0], [0.0]]
with open(hist_file) as f:
    for line in f:
        line_list = line.strip().split(',')
        if len(line_list)<2:
            continue
        date_time = int(line_list[0])
        date_time = date_util.date_interp(date_time) - start_date
        value = float(line_list[1])
        if value > 0:
            total_in[0].append(date_time)
            total_in[1].append(total_in[1][len(total_in[1]) - 1])
            total_in[0].append(date_time) #Why is this here twice? It's for the plot. Otherwise, moving from 0 to 100 in 5 days is a diagonal line, but really you just got 100 dollars at one point in the middle
            total_in[1].append(value + total_in[1][len(total_in[1]) - 1])
        elif value < 0 and not "invest" in line_list[2]:
            total_out[0].append(date_time)
            total_out[1].append(total_out[1][len(total_out[1]) - 1])
            total_out[0].append(date_time)
            total_out[1].append(value + total_out[1][len(total_out[1]) - 1])
        total[0].append(date_time)
        total[1].append(total[1][len(total[1]) - 1])
        total[0].append(date_time)
        total[1].append(value + total[1][len(total[1]) - 1])
total_file = open('total.csv','w+')
total_out_file = open('total_out.csv','w+')
total_in_file = open('total_in.csv','w+')

for i in range(len(total[0])):
    total_file.write('{0:.2f}'.format(total[0][i])+ "," +  '{0:.2f}'.format(total[1][i])+ '\n')
for i in range(len(total_in[0])):
    total_in_file.write('{0:.2f}'.format(total_in[0][i]) + "," + '{0:.2f}'.format(total_in[1][i]) + '\n')
for i in range(len(total_out[0])):
    total_out_file.write('{0:.2f}'.format(total_out[0][i]) + "," + '{0:.2f}'.format(total_out[1][i]) + '\n')
total_file.close
total_out_file.close
total_in_file.close

