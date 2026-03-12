import numpy as np
import matplotlib.pyplot as plt
from scipy import signal



'''
x = np.linspace(0, 20, 100)
y = x + 4*np.sin(x) + np.random.randn(x.shape[0])
plt.plot (x, y)
plt.show()
'''



# Eliminate linear trend
'''
new_y =signal.detrend(y)
plt.plot(x, y)
plt.plot (x, new_y)
plt.show()
'''

#Fourier transformation
'''
x = np.linspace(0, 30, 1000)
y = 3*np.sin(x) + 2*np.sin(5*x) + np.sin(10*x)

plt.plot (x, y)
plt.show()
'''
from scipy import fftpack
'''
fourier = fftpack.fft(y)
power = np.abs(fourier)
freq = fftpack.fftfreq(y.size)
plt.plot(abs (freq), power )
plt.show()
'''

# signal filtering

x = np.linspace(0, 30, 1000)
y = 3*np.sin(x) + 2*np.sin(5*x) + np.sin(10*x)+ np.random.random(x.shape[0])*10
'''
#plt.plot (x, y)
#plt.show()
fourier = fftpack.fft(y)
power = np.abs(fourier)
freq = fftpack.fftfreq(y.size)
plt.plot(np.abs (freq), power )
plt.show()
'''
#filtering signal
'''
fourier = fftpack.fft(y)
power = np.abs(fourier)
freq = fftpack.fftfreq(y.size)
fourier[power<400] = 0   # Delete  the noise 
plt.plot(np.abs(freq), np.abs(fourier) )
plt.show()
'''
#Inverse FFT signal
fourier = fftpack.fft(y)
power = np.abs(fourier)
freq = fftpack.fftfreq(y.size)
fourier[power<400] = 0   # Delete  the noise
filtered_signal = fftpack.ifft (fourier)
plt.figure(figsize=(12, 8))
plt.plot(x, y, lw= 0.5)
plt.plot (x, np.abs(filtered_signal), lw=3)
plt.show()