
# Standard Library
from sys import argv
from math import exp


def fp(interest, period, continuous_compounding=False):
    """Compound Amount"""
    if continuous_compounding:
        return exp(period * interest)
    else:
        return pow(1 + interest, period)


def pf(interest, period, continuous_compounding=False):
    """Present Worth"""
    if continuous_compounding:
        return 1 / exp(period * interest)
    else:
        return 1 / pow(1 + interest, period)


def fa(interest, period, continuous_compounding=False):
    """Series Compound Amount"""
    if continuous_compounding:
        return (exp(period * interest) - 1) / (exp(interest) - 1)
    else:
        return (pow(1 + interest, period) - 1) / interest


def af(interest, period, continuous_compounding=False):
    """Sinking Fund"""
    if continuous_compounding:
        return (exp(interest) - 1) / (exp(period * interest) - 1)
    else:
        return interest / (pow(1 + interest, period) - 1)


def ap(interest, period, continuous_compounding=False):
    """Capital Recovery"""
    if continuous_compounding:
        return (exp(period * interest) * (exp(interest) - 1)) / (
            exp(period * interest) - 1)
    else:
        return (interest * pow(1 + interest, period)) / (pow(1 + interest, period) - 1)


def pa(interest, period, continuous_compounding=False):
    """Series Present Worth"""
    if continuous_compounding:
        return (exp(period * interest) - 1) / (exp(period * interest) * (exp(interest) - 1))
    else:
        return (pow(1 + interest, period) - 1) / (interest * pow(1 + interest, period))


def pg(interest, period, continuous_compounding=False):
    """Arithmetic Gradient Present Worth"""
    if continuous_compounding:
        return (exp(period * interest) - 1 - period * (exp(interest) - 1)) / (exp(period * interest) * pow(exp(interest) - 1, 2))
    else:
        return (pow(1 + interest, period) - (interest * period) - 1) / (pow(interest, 2) * pow(1 + interest, period))


def ag(interest, period, continuous_compounding=False):
    """Arithmetic Gradient Uniform Series"""
    if continuous_compounding:
        return (pow(exp(interest) - 1, -1)) - (period / (exp(period * interest) - 1))
    else:
        return (pow(1 + interest, period) - (interest * period) - 1) / (interest * pow(1 + interest, period) - interest)


if __name__ == '__main__':

    period = float(argv[argv.index('-n') + 1])
    interest = float(argv[argv.index('-i') + 1])
    precision = int(argv[argv.index('-p') + 1]) if '-p' in argv else 4
    continuous_compounding = True if '--cc' in argv else False

    print('Compounding Factor Calculator', 'Continuous' if continuous_compounding else 'Discrete', sep=' - ')
    print(f'(F/P, {interest * 100}%, {period}) =', round(fp(interest, period, continuous_compounding), precision))
    print(f'(P/F, {interest * 100}%, {period}) =', round(pf(interest, period, continuous_compounding), precision))
    print(f'(P/A, {interest * 100}%, {period}) =', round(pa(interest, period, continuous_compounding), precision))
    print(f'(A/P, {interest * 100}%, {period}) =', round(ap(interest, period, continuous_compounding), precision))
    print(f'(F/A, {interest * 100}%, {period}) =', round(fa(interest, period, continuous_compounding), precision))
    print(f'(A/F, {interest * 100}%, {period}) =', round(af(interest, period, continuous_compounding), precision))
    print(f'(P/G, {interest * 100}%, {period}) =', round(pg(interest, period, continuous_compounding), precision))
    print(f'(A/G, {interest * 100}%, {period}) =', round(ag(interest, period, continuous_compounding), precision))
