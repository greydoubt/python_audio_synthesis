import IPython.display as ipd
import matplotlib.pyplot as plt
import numpy
import math

sample_rate = 22050

def addsine(frequency, duration, amplist):
    i = 1
    t = numpy.linspace(0, duration, math.ceil(sample_rate * duration))
    output = numpy.zeros(t.size)

    for amp in amplist:
        x = numpy.multiply(makesine(frequency * i, duration), amp)
        output = output + x
        i += 1

    if numpy.max(output) > abs(numpy.min(output)):
        output = output / numpy.max(output)
    else:
        output = output / -numpy.min(output)
    return output


t = numpy.linspace(0, 1, sample_rate)
sinewave = addsine(440, 1, [1])
plt.plot(t, sinewave)
plt.xlim(0, 0.005)
ipd.Audio(sinewave, rate=sample_rate)
