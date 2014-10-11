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

x = ackermann(1,2)
print x 

if __mame__ == "__main__"