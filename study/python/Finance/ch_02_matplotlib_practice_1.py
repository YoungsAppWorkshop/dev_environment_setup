#!/usr/bin/env python3
"""     p. 96 ~
"""
from matplotlib.pyplot import *
import numpy as np


# Basic Usage
plot([1, 2, 3, 9])
xlabel("x- axis")
ylabel("y- axis")
title("My Figure")
show()

# Cosign, Sign
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(x), np.sin(x)
plot(x, C)
plot(x, S)
show()
