# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qfIhXjH4sGwLhSXrBwQus6NZ04EgZ66_
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50) * 10
y = np.random.rand(50) * 10
plt.scatter(x, y)
plt.show()

