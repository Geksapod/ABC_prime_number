import abc_prime_number as pn

if __name__ == "__main__":

    try:
        number_1 = pn.PrimeNumber(5)
        print(number_1)

        number_2 = pn.PrimeNumberNonABC(4)
        print(isinstance(number_2, pn.AbstractPrimeNumber))
        print(number_2)
    except AttributeError:
        pass
