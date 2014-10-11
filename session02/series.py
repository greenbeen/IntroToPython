def fibonacci(n):
    """return nth value in fibonacci series"""
    series = [0,1]
    for i in range(n-2):  #n-2 because we start with 2 in series
        series.append(series[i] + series[i+1])
    return series[-1]


def lucas(n):
    """return nth value in lucas series"""
    series = [2, 1]
    for i in range(n-2):
        series.append(series[i] + series[i+1])
    return series[-1]


def sum_series(n, num1=0, num2=1):
    """return nth value in series created adding num1 and num2
    for example num1=0 num2=1 produces 0,1,1,2,3,5
    last two in series are added and added to list, then repeat"""
    series = [num1, num2]
    for i in range(n-2):
        series.append(series[i] + series[i+1])
    return series[-1]


#print fibonacci(5)
#print lucas(5)
#print sum_series(5, 2, 3)

if __name__ == "__main__":
    assert fibonacci(5) == 3  #confirms 5th value in fibonacci series function is 3
    assert lucas(5) == 7  #confirms 5th value in lucas series fuction is 7
    assert sum_series(5) == 3  #confirms entering 1 parameter calculate nth value in fibonacci series
    assert sum_series(5, 2, 1)  #confirms entering 3 parameters calculates nth value in user generated series, incl. lucas
    print "All tests passed"

