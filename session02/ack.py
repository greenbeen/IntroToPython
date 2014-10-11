def ackermann(m, n):
    """Computes the Ackermann fuction for two values"""
    if m < 0 or n < 0:
        return None
    else:
        if m == 0:
            return n + 1
        elif m > 0 and n == 0:
            return ackermann(m-1, 1)
        elif m > 0 and n > 0:
            return ackermann(m-1, ackermann(m, n-1))

#print ackermann(1,2)


# Test function
if __name__ == "__main__":
    assert ackermann(0, 0) == 1
    assert ackermann(1, 1) == 3
    assert ackermann(2, 2) == 7
    assert ackermann(3, 3) == 61
    print "All tests passed"
