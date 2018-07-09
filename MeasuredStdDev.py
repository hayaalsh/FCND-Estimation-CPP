import fileinput
import pandas

GPSPosXY = pandas.read_csv("./config/log/Graph1.txt", sep=",", header=None, skiprows=1)
AccelXY  = pandas.read_csv("./config/log/Graph2.txt", sep=",", header=None, skiprows=1)

_ , MeasuredStdDev_GPSPosXY = GPSPosXY.std(axis=0)
_ , MeasuredStdDev_AccelXY = AccelXY.std(axis=0)

print('MeasuredStdDev_GPSPosXY = %0.2f' % MeasuredStdDev_GPSPosXY)
print('MeasuredStdDev_AccelXY = %0.2f' % MeasuredStdDev_AccelXY)

#for line in fileinput.input("./config/06_SensorNoise.txt", inplace=True):
#	if line.strip().startswith('MeasuredStdDev_GPSPosXY = '):
#		line = 'MeasuredStdDev_GPSPosXY = %0.2f' % MeasuredStdDev_GPSPosXY
#	elif line.strip().startswith('MeasuredStdDev_AccelXY = '):
#		line = 'MeasuredStdDev_AccelXY = %0.2f' % MeasuredStdDev_AccelXY
#	print line,

