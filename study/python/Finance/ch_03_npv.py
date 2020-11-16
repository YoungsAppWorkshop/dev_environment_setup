#!/usr/bin/env python3
"""     p. 146
NPV:    Net Present Value

Definition:
    A measurement of profit calculated by subtracting the present values(PV)
    of cash outflows (including initial cost) from the present values of cash
    inflows over a period of time

Rules:
    NPV > 0     : Invest
    NPV < 0     : Not Invest
"""
import scipy as sp
import matplotlib.pyplot as pyplot

rate = 0.112
cashflows = [-100, 50, 60, 70, 100, 20]
print(sp.npv(rate, cashflows))

rate = []
npv = []
for i in range(1, 100):
    rate.append(0.01 * i)
    npv.append(sp.npv(0.01 * i, cashflows))
pyplot.plot(rate, npv)
pyplot.show()
