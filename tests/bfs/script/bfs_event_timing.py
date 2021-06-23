import subprocess
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlsxwriter
import sys

outputPath = '/home/mrezv002/ROCm-research/HIP-Examples/tests/bfs/result'
numTests = 2

fullTiming = []

for i in range(numTests):
  print('Run ' + str(i))

  filePath = outputPath + '/output' + str(i) + '.txt'
  fp = open(filePath, "w")
  rc = subprocess.run(['bash run.sh'], shell=True, stdout=fp, stderr=subprocess.PIPE)
  fp.close()

  singleRunTiming = []
  
#  label = ['queued', 'submitted', 'start', 'end', 'end-start', 'end-queued']
#  singleRunTiming.append(label)
  
  with open(filePath) as fp:
    line = fp.readline()
    
    while line:
      # Find time in lines and parse it
      times = []
      x = line.split(' ')
      if( x[0] == 'Event' ):
        times.append(int(x[4]))
        times.append(int(x[6]))
        times.append(int(x[8]))
        times.append(int(x[10]))
        times.append(int(x[10])-int(x[8]))
        times.append(int(x[10])-int(x[4]))
      # Store data if we found timings
      if(not(len(times) == 0)):
        singleRunTiming.append(times)
      
      line = fp.readline()
      
  fullTiming.append(singleRunTiming)

#fullTiming = np.array(fullTiming)

print(fullTiming)