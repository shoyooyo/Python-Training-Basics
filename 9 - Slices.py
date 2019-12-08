#talks about slices

    # example: inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255
    # the below is a variable with the data defined
    >>> ip_info = "inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255"
    >>> ip_info
    'inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255'
    # below is example of splicing
    >>> ip_info[5:14]
    '10.0.2.15'
    >>> ip_info[5:]
    '10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255'
    >>> ip_info[:14]
    'inet 10.0.2.15'
    >>> ip_info[:]
    'inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255'
    >>> ip_info[-1]
    '5'
    >>> ip_info[-10:-1]
    '10.0.2.25'
    >>> ip_info[-10:]
    '10.0.2.255'
    >>> ip_info[:-10]
    'inet 10.0.2.15  netmask 255.255.255.0  broadcast '
    
    #to skip every 2nd character of the above string
    >>> ip_info[::2]
    'ie 0021 ntak2525250 racs 00225'

    #to get the value in reverse
    >>> ip_info[::-1]
    '552.2.0.01 tsacdaorb  0.552.552.552 ksamten  51.2.0.01 teni'