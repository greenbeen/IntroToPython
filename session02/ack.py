def ack(m, n):
    """Computes the ack fuction for two values"""
    if m < 0 or n < 0:
        return None
    else:
        if m == 0:
            return n + 1
        elif m > 0 and n == 0:
            return ack(m-1, 1)
        elif m > 0 and n > 0:
            return ack(m-1, ack(m, n-1))

x = ack(1,2)
print x 

if __name__ == '__main__':
    print "running program: add assertions here"