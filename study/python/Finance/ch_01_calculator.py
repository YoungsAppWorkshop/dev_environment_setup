#!/usr/bin/env python3


def fv_f(pv, r, n):
    """ Objective: Estimate future value

        Formula:
            fv = pv * (1 + r) ^ n

                fv: future value
                pv: present value
                r : discount periodic rate
                n : number of periods
    """
    return pv * (1 + r)**n


def pv_f(fv, r, n):
    """ Objective: Estimate present value

        Formula:
                        fv
            pv = -----------------
                   (1 + r) ^ n

                fv: future value
                pv: present value
                r : discount periodic rate
                n : number of periods
    """
    return fv / (1 + r)**n


def npv_f(rate, cashflows):
    total = 0.0
    for i, cashflow in enumerate(cashflows):
        total += cashflow / (1 + rate)**i
    return total


def irr(cashflows):
    lst, r = [], 0
    while r < 1.0:
        r += 0.000001
        npv = npv_f(r, cashflows)
        if abs(npv) <= 0.0001:
            lst.append(r)
    return lst


if __name__ == '__main__':
    r = 0.035
    cashflows = [-100, -30, 10, 40, 50, 45, 20]
    print(npv_f(r, cashflows))

    cashflows = (550, -500, -500, -500, 1000)
    print(irr(cashflows))
