#talks about slicing using a step

#example data: 
    >>> my = "0123456789"
    >>> my [0]
    '0'
    >>> my [3]
    '3'
    >>> my [9]
    '9'
    # slicing syntax with step
    # variable[start:stop:step]

# example of start:stop
    >>> my [1:5]
    '1234'

# example of step
    >>> my [::2]
    '02468'

# example of start::step
    >>> my [1::2]
    '13579'

# example of start:stop:step
    >>> my [1:7:2]
    '135'