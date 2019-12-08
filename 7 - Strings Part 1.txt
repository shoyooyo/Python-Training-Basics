# Strings - Operators & Formatting Types
    # the below are various operators used
        # "=" //used for adding a data into a variable
            Example:
                >>> a = "ajaz"
                >>> b = "ahmed"
        # "+" //used for concatinating two or more strings
            Example:
                >>> a + b
                'ajazahmed'
                >>> a+b
                'ajazahmed'
        # "*" //used for multiplying any given string types
            Example:
                >>> a*3
                'ajazajazajaz'
                >>> b*3
                'ahmedahmedahmed'
        # "in" //used for searching if a character is part of a string
            Example:
                >>> "e" in a
                False
                >>> "e" in b
                True
        # "not in" ////used for searching if a character is not part of a string
            Example:
                >>> "e" not in a
                True
    # the below are various string formatting's used
        # lets take an example and understand
        # the below is a string example
        # "Redmi - 8PRO, 6 GB RAM, INR 12999.99"
        # "Redmi - %s, %d GB RAM, INR %f" % ("8PRO", 6, 12999.99)
        # where 
            # %s > placeholder for a string
            # %d > placeholder for a number
            # %f > placeholder for a floating point
            # % > acts as a mapping between strings and data in the paranthesis
        Example:
            >>> "Redmi - %s, %d GB RAM, INR %f" % ("8PRO", 6, 12999.99)
            'Redmi - 8PRO, 6 GB RAM, INR 12999.990000'
            >>> "Redmi - %s, %d GB RAM, INR %f" % ("10PRO", 8, 22999.99)
            'Redmi - 10PRO, 8 GB RAM, INR 22999.990000'
            # to control the decimal value of %f use the below (either .1, .2 or . so on etc)
            >>> "Redmi - %s, %d GB RAM, INR %.2f" % ("8PRO", 6, 12999.99)
            'Redmi - 8PRO, 6 GB RAM, INR 12999.99'
            >>> "Redmi - %s, %d GB RAM, INR %.3f" % ("8PRO", 6, 12999.99)
            'Redmi - 8PRO, 6 GB RAM, INR 12999.990'
            
            #The above can be mapped via curly braces also
            >>> "Redmi - {}, {} GB RAM, INR {}" .format ("8PRO", 6, 12999.99)
            'Redmi - 8PRO, 6 GB RAM, INR 12999.99'
            
            # why its recommended to use the above is because of the power of indexing
            # with {} we can print the value in the parathsis multiple times or switch the position
            # switching position example
                #Example: The below is our base template
                    "Redmi - {}, {} GB RAM, INR {}" .format ("8PRO", 6, 12999.99)
                    #Now let's assume you want to print 6 in different place, like below
                    "Redmi - {0}, {1} GB RAM, INR {1}" .format ("8PRO", 6, 12999.99)
                    'Redmi - 8PRO, 6 GB RAM, INR 6'
                    #Print in multiple places
                    >>> "Redmi - {1}, {2} GB RAM, INR {1}" .format ("8PRO", 6, 12999.99)
                    'Redmi - 6, 12999.99 GB RAM, INR 6'


