#!/usr/bin/env python3
"""     p. 149
IRR:    Internal Rate of Return

Definition:
    The interest rate at which the net present value of all the
    cash flows (both positive and negative) from a project or
    investment equal zero.

Rules:
    IRR > Rc    : Invest
    IRR < Rc    : Not Invest
"""
import scipy as sp


cashflows = [-100, 30, 40, 40, 50]
print(sp.irr(cashflows))

r = sp.irr(cashflows)
print(sp.npv(r, cashflows))
