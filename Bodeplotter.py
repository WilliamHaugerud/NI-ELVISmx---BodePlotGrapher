import matplotlib.pyplot as plt
import numpy as np

f = open("op.txt", "r")
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


absolute_difference_function = lambda list_value : abs(list_value - (max(gain)-3))
closest_value = min(gain, key=absolute_difference_function)
gain.index(closest_value)
freq_comment = str(freq[gain.index(closest_value)])


plt.figure()
plt.subplot(211)
plt.semilogx(freq, gain)
#Comment out these lines to plot withou the -3 dB point
plt.scatter(freq[gain.index(closest_value)], gain[gain.index(closest_value)], color = 'red')
plt.annotate('-3dB at {}Hz'.format(freq_comment), (freq[gain.index(closest_value)], gain[gain.index(closest_value)]))

plt.grid()
plt.ylabel('dB Mag.')
#plt.ylim([-120,5])
plt.subplot(212)
plt.semilogx(freq, phase)
plt.grid()
plt.xlabel('Freq. (Hz)')
plt.ylabel('Phase (deg.)')
#plt.ylim([-185,10])
#out = plt.yticks(np.arange(-180,5,45))
plt.show()
