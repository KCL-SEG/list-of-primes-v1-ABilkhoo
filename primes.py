"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    #Ignore possibility number_of_primes < 1
    list = []
    
    i = 2
    while len(list) < number_of_primes:
        prime = True;
        for item in list:
            if i % item == 0:
                prime = False;
                break;
        
        if prime == True:
            list.append(i)
        i += 1

    return list
