# talks about Booleans - true or false

# "==", "!=", "<=", ">=", "and", "or", "not", "bool()"
# None, 0, 0.0, 0L, 0j, "", [], (), {} //these values always evaluate to False
    >>> (1 == 1) and (2 == 2)
    True
    >>> (1 == 1) or (2 == 2)
    True
    >>> not(1==1)
    False
    >>> not(1==2)
    True
    >>> bool(None)
    False
    >>> bool(0
    ... 
    KeyboardInterrupt
    >>> bool(0)
    False
    >>> bool("")
    False
    >>> bool(oj)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    NameError: name 'oj' is not defined
    >>> bool(0j)
    False
    >>> bool("happy")
    True
    >>> bool(0)
    False
    >>> bool(1)
    True

    #print(bool("Python 3") and not(23 == 23))
    above is false

    # result = int (6 % 5 + 9 - 2 - 4 ** 2 / 2)
    # x = bool(result) <add the appropriate logical operator> (7 + 2) == (3**2)
    # print (x)
    # x should be "true"
    # 6 % 5 + 9 - 2 - 4 ** 2 / 2
    # 4 ** 2 = 16 ==> 6 % 5 + 9 - 2 - 16 / 2
    # 6 % 5 = 1 ==> 1 + 9 - 2 - 16 / 2
    # 16 / 2 = 8 ==> 1 + 9 - 2 - 8
    # 1 + 9 = 10 ==> 10 - 2 - 8
    # 10 - 2 = 8 ==> 8 - 8
    # 8 - 8 = 0
    # bool(result) = ?
    # result = 0
    # bool(0) = false
    # x = false <?> (7+2) == (3**2)
    # 3**2 = 9
    # 7+2 = 9
    # (7+2) == (3**2) ==> 9 == 9
    # 9 == 9 = true
    # therefore
    # x = false <?> true
    # x = false or true
    # therefore "x" is true
    