import IPython.display as ipd
import numpy
import math
import matplotlib.pyplot as plt

sample_rate = 22050

def makesine(frequency, duration):
    t = numpy.linspace(0, duration, math.ceil(sample_rate * duration))
    x = numpy.sin(2 * numpy.pi * frequency * t)
    return x



output = numpy.array(())
y = makesine(261.63, 0.5)  # C for 0.5 seconds

output = numpy.concatenate((output, y))
y = makesine(293.66, 0.5)  # D for 0.5 seconds

output = numpy.concatenate((output, y))
y = makesine(329.63, 0.5)  # E for 0.5 seconds

output = numpy.concatenate((output, y))
ipd.Audio(output, rate=sample_rate)
