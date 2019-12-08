# Strings - F String Formatting type
    # let's understand with example
        >>> model
        'Note5'
        >>> gb
        6
        >>> inr
        12999.99
        >>>
    # Syntax - f"template inside this"
    # Example - 
    >>> f"Redmi - {model}, {gb} GB RAM, INR {inr}"
    'Redmi - Note5, 6 GB RAM, INR 12999.99'

    # Advantage - You can use the operators learnt earlier here like below
        >>> f"Redmi - {model.upper()}, {gb} GB RAM, INR {inr*2}"
        'Redmi - NOTE5, 6 GB RAM, INR 25999.98'