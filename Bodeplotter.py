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





plt.figure()
plt.subplot(211)
plt.semilogx(freq, gain)
plt.grid()
plt.ylabel('dB Mag.')
#plt.ylim([-120,5])
plt.subplot(212)
plt.semilogx(freq, phase)
plt.xlabel('Freq. (Hz)')
plt.ylabel('Phase (deg.)')
#plt.ylim([-185,10])
#out = plt.yticks(np.arange(-180,5,45))
plt.show()