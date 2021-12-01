import matplotlib.pyplot as plt
import numpy as np

f = open("oputenADC.txt", "r")
line1 = f.readline()
date, time = line1.split()
line2 = f.readline()
amplitude = line2
line3 = f.readline()

freq = []
gain = [] 
phase = []

line = f.readline().strip('\n')

while line !="":
    freqRaw, gainRaw, phaseRaw =  line.split()
    freq.append(float(freqRaw.replace(',', '.')))
    gain.append(float(gainRaw.replace(',', '.')))
    phase.append(float(phaseRaw.replace(',', '.')))
    line = f.readline()

#Finding the -3 dB value and finding the value nearest this value in the list.
absolute_difference_function = lambda list_value : abs(list_value - (max(gain)-3))
closest_value = min(gain, key=absolute_difference_function)
peak_dB_ELVIS = max(gain)
x_coord_ELVIS = freq[gain.index(closest_value)]
y_coord_ELVIS = gain[gain.index(closest_value)]
freq_comment = str(freq[gain.index(closest_value)])

#dB plot
plt.figure()
plt.subplot(211)
plt.semilogx(freq, gain)
#Comment out these lines to plot without the -3 dB point
plt.scatter(x_coord_ELVIS, y_coord_ELVIS, color = 'red')
plt.annotate('-3dB at {}Hz'.format(freq_comment), (x_coord_ELVIS, y_coord_ELVIS))
plt.legend(['Peak value {}dB'.format(peak_dB_ELVIS)], loc ="lower left") #Use this to change the location

plt.ylabel('dB Mag.')
plt.grid()
#Phaseplot
plt.subplot(212)
plt.semilogx(freq, phase)
plt.xlabel('Freq. (Hz)')
plt.ylabel('Phase (deg.)')
plt.grid()
plt.show()

