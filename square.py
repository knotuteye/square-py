#
#   Fourier Square Wave Approx Simulation
#   Made by Kevin Otuteye for Linear Electronics Class - KNUST - 2019
#

# Imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

# Setup
figure(num=None, figsize=(12, 6))

# Create an array of 10k evenly-spaced values between -20 and 20.
domain = np.linspace(-20, 20, 20000)

# Globals
period = 0
harmonics = 0

# Initial interaction


def init():
    global period
    global harmonics
    period = int(input("Enter a period (less than 40): "))
    harmonics = int(input("Enter the number of harmonics: "))

# Function to generate square wave


def squareWave(x):
    global period
    lowerBoundLeft = (-period/2)
    lowerBoundRight = 0
    upperBoundLeft = 0
    upperBoundRight = (period/2)
    one = 1
    negativeOne = -1

    while True:
        if (x >= lowerBoundLeft) and (x <= lowerBoundRight):
            return negativeOne
        elif (x >= upperBoundLeft) and (x <= upperBoundRight):
            return one
        else:
            lowerBoundLeft -= period/2
            lowerBoundRight -= period/2
            upperBoundLeft += period/2
            upperBoundRight += period/2
            if one == 1:
                one = -1
                negativeOne = 1
            else:
                one = 1
                negativeOne = -1

# Bn coefficient function


def bn(n):
    n = int(n)
    if (n % 2 != 0):
        return 4/(np.pi*n)
    else:
        return 0

# Wn coefficient function


def wn(n):
    global period
    wn = (2*np.pi*n)/period
    return wn

# Function to generate fourier approximation


def fourierSeries(n_max, x):
    partialSums = 0
    for n in range(1, n_max):
        try:
            partialSums += bn(n)*np.sin(wn(n)*x)
        except:
            print("pass")
            pass
    return partialSums


init()
signal_codomain = []
fourier_codomain = []
for i in domain:
    signal_codomain.append(squareWave(i))
    fourier_codomain.append(fourierSeries(harmonics, i))


plt.plot(domain, signal_codomain, color="blue", label="Signal")
plt.plot(domain, fourier_codomain, color="red",
         label="Fourier series approximation")
plt.legend(loc='upper right')

graph = plt.gcf()
graph.canvas.set_window_title(
    "Fourier Series approximation number of harmonics: "+str(harmonics))

plt.show()
