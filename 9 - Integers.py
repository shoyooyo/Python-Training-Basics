# talks about numbers
# specifically about math operators
# example
    >>> num1 = 10
    >>> num2 = 15.5
    >>> type(num1)
    <class 'int'>
    >>> type(num2)
    <class 'float'>
    >>> num1+num2
    25.5

    # Math operators
    >>> 2 - 1 //addition
    1
    >>> 7 / 2 //division
    3.5
    >>> 7 // 2 //division but returns only integer not the float
    3
    >>> 1 * 2 // multiplication
    2
    >>> 2 ** 2 // power of
    4
    >>> 2 ** 3 // power of example 2
    8
    >>> 2 ** 4
    16
    >>> 7 %2 //modulo
    1
    >>> 6%2 // modulo 2
    0

    #comparision operators
    >>> 4<=5
    True
    >>> 5>=4
    True
    >>> 5=5
    File "<stdin>", line 1
    SyntaxError: can't assign to literal
    >>> 5==5
    True
    >>> 4!=5
    True
    >>> max(1,2) //returns max value
    2
    >>> min(1,2) //returns min value
    1
    >>> pow(3,2) //another way of raising power
    9

    # Priority of the operators (top to bottom)
    # 1. raising to the power
    # 2. multiplication, division, modulo
    # 3. addition & subtraction
    # what this means, so if there is a equation with multiple operations like below then
    # it will be calculated as per the priority of the operation
    # example: 100 - 5 ** 2 / 5 * 2
    # so it would be calculated as below
    # 5 ** 2 = 25 ==> 100 - 25 / 5 * 2
    # and now since division and multiplcation have same priority they will be evaluated from left to right
    # 25 / 5 = 5 ==> 100 - 5 * 2
    # 5 * 2 = 10 ==> 100 - 10
    # 100 - 10 = 90
    # result is 90
    >>> 100 - 5 ** 2 /5*2
    90.0

    # convertors
    >>> int(19.99) //returns integer type
    19
    >>> float(15) // returns float type
    15.0
    >>> abs(-5) //returns the absolute distance between the number mentioned and zero
    5
    >>> abs(5) //example 2
    5