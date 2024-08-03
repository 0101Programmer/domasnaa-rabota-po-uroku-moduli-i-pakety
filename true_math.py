from math import inf


def divine(first, second):
    if second == 0:
        return inf
    res = first / second
    return res


