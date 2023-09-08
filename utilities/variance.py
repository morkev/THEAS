from math import sqrt, hypot
import operator


def variance(values):
    m = mean(values)
    return sum((v - m) ** 2 for v in values) / len(values)


def mean(values):
    return sum(values) / float(len(values))


def stdev(values):
    return sqrt(variance(values))


def dist(a, b):
    return hypot(b[0] - a[0], b[1] - a[1])


def weighted_geometric_mean(values, weights):
    assert (len(values) == len(weights))
    n = 1
    for v, w in zip(values, weights):
        n *= v ** w
    return n ** (1.0/sum(weights))
