def PrimeNumber(NumberToCheck):
    for i in range(2,NumberToCheck):
        if(NumberToCheck%i == 0):
            return False
        return True