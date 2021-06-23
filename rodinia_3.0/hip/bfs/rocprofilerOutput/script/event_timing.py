import pandas as pd
import xlsxwriter
import sys

num = sys.argv[1]
filepath = '../result/output.txt'
outputpath = '../result/timing'+str(num)+'.xlsx'
timing = []
label = ['queued','submitted','start','end','end-start','end-queued']
timing.append(label)
with open(filepath) as fp:
  line = fp.readline()
  
  while line:
    # Find time in lines and parse it
    time = []
    x = line.split(' ')
    if( x[0] == 'Event' ):
      time.append(int(x[4]))
      time.append(int(x[6]))
      time.append(int(x[8]))
      time.append(int(x[10]))
      time.append(int(x[10])-int(x[8]))
      time.append(int(x[10])-int(x[4]))
    # Store data if we found timings
    if(not(len(time) == 0)):
      timing.append(time)
    
    line = fp.readline()

with xlsxwriter.Workbook(outputpath) as workbook:
    worksheet = workbook.add_worksheet()

    for row_num, data in enumerate(timing):
        worksheet.write_row(row_num, 0, data)
