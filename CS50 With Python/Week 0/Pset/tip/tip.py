def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Using the split function split the string into two parts ["$","50.00"] 
    # of a list and take the 1 index of the list(eg. $50.00)
    # then convert the string into a float (50.0)
    
    d = d.split("$")
    d = float(d[1])
    return d

    """ 
    # with the replace function we can do the same thing
    d_n = d_n.replace("$", "")
    return float(d_n)
    
    """


def percent_to_float(p):
    # using the split function split the string into two parts ["15","%"] 
    # of a list and take the 0 index of the list (eg. 15%)
    # then convert the string into a float (eg. 15) then divide to get the actual amount out of 100 (15% of 100%)
    p = p.split("%")
    p = float(p[0])

    p /= 100
    return p

    """ 
    # with the replace function we can do the same thing
    p_n = p_n.replace("%", "")
    return float(p_n)
    
    """



main()