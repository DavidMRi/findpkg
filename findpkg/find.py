def find(f, y, a, b):
    """Finds an integer n within [a,b] that solves f(n)=y for an increasing f

    Parses an increasing function f looking for an integer n within the range
    [a,b] of non-negative integers for which it solves f(n)=y. If found,
    n will be returned, otherwise, if no such n exists, -1 is returned.
    The assertions on this function are compute-intensive, so using -O or -OO
    for deployments is advised.

    Args:
        f (function): increasing function f of an integer argument that
                      evaluates to a floating point value.
        y (float): arbitrary floating point number for which to solve.
        a (int): lower bound of the range of non-negative integers to analyze.
        b (int): upper bound of the range of non-negative integers to analyze.

    Returns:
        An integer n within the range [a,b] that solves f(n)=y, or -1 if no
        such n exists.

    """
    assert a <= b, "Invalid range: b must be equal or greater than a."
    assert a >= 0 and b >= 0, "Invalid range: a and b must be non-negative."
    assert __f_is_increasing(f, a, b), "Invalid function: f is not an " \
                                       "increasing function for every " \
                                       "integer in the [a,b] range."

    if f(a) > y or f(b) < y:    # n is out of range
        return -1
    else:
        return __recursive_find(f, y, a, b)


def __recursive_find(f, y, a, b):
    # Using binary search to find n
    if a > b:   # no n could be found
        return -1

    n = a + int((b-a)/2)
    aux = f(n)
    if aux == y:
        return n
    else:
        if aux > y:     # n is on the lower half
            return __recursive_find(f, y, a, n-1)
        else:           # n is on the upper half
            return __recursive_find(f, y, n+1, b)


def __f_is_increasing(f, a, b):
    if a < b:
        low = f(a)
        for i in range(a+1, b):
            y = f(i)
            if y < low:
                return False
            else:
                low = y
    return True
