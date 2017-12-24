import pip
import numpy
import jupyter
import matplotlib
matplotlib.use('TkAgg')
import sklearn
import scipy
import pandas
import PIL
import seaborn
import h5py
import tensorflow
import keras

assert(pip.__version__ >= '9.0.1')
assert(numpy.__version__ >= '1.12.0')
assert(matplotlib.__version__ >= '2.0.0')
assert(sklearn.__version__ >= '0.18.1')
assert(scipy.__version__ >= '0.19.0')
assert(pandas.__version__ >= '0.19.2')
assert(PIL.__version__ >= '4.0.0')
assert(seaborn.__version__ >= '0.7.1')
assert(h5py.__version__ >= '2.7.0')
assert(tensorflow.__version__ >= '1.1.0')
assert(keras.__version__ >= '2.0.4')

print("Houston we are go!")