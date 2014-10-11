def fibonacci(n):
    """return nth value in fibonacci series"""
    series = [0,1]
    for i in range(n-2):  #n-2 because we start with 2 in series
        series.append(series[i] + series[i+1])
    return series[-1]


def lucas(n):
    """return nth value in lucas series"""
    series = [2,1]
    for i in range(n-2):
        series.append(series[i] + series[i+1])
    return series[-1]

print fibonacci(5)
print lucas(5)

