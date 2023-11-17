import numpy as np
from Lazyfitter import LazyFitter
from Rbf import Rbf
import matplotlib as plt
from matplotlib import pyplot

coords = np.array([[1], [2], [3], [4]])
vals = np.array([1, 2, 3, 4])

ftr = LazyFitter(coords, vals)

print(ftr.min_error)

xs = np.linspace(0, 5, 100)
fs = [ftr.Interpolate([x]) for x in xs]

pyplot.plot(xs, fs)
pyplot.show()

ftr.OptimizeShape()

print(ftr.min_error)
print(ftr.epsilon)

xs = np.linspace(0, 5, 100)
fs = [ftr.Interpolate([x]) for x in xs]

pyplot.plot(xs, fs)
pyplot.show()