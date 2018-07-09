import fileinput
import pandas
import numpy as np

GPSPosXY = pandas.read_csv("./config/log/Graph1.txt", sep=",", header=None, skiprows=1)
AccelXY  = pandas.read_csv("./config/log/Graph2.txt", sep=",", header=None, skiprows=1)


print(str(GPSPosXY.std(axis=0)))

print(str(AccelXY.std(axis=0)))

#for line in fileinput.input("./config/06_SensorNoise.txt", inplace=True):
#	if line.strip().startswith('MeasuredStdDev_GPSPosXY = '):
#		line = 'MeasuredStdDev_GPSPosXY = %0.2f\n' % GPSPosXY.std(axis=0)
#	elif line.strip().startswith('MeasuredStdDev_AccelXY = '):
#		line = 'MeasuredStdDev_AccelXY = %0.2f\n' % AccelXY.std(axis=0)
#	print line,
