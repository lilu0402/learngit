import random

import matplotlib.pyplot as plt
import numpy as np


def draw_test(x, y):
    plt.plot(x,y,'ro-')
    f = plt.gca()
    f.minorticks_on()
    f.legend('haha')
    f.grid(True, which='minor',axis='both')
    plt.show()
a = np.arange(10)
b = list(np.linspace(10,100,10))
bb = np.array(b)
draw_test(a, bb)
