def get_summ(one, two, delimiter = '&'):
    one = str(one)
    two = str(two)
    x = (one.upper() + delimiter + two.upper())
    print(x)
    return(x)
    
get_summ("Learn", "python" ) 

     