"""This module provide access to prime number classes."""
from abc import ABC, abstractmethod


class AbstractPrimeNumber(ABC):
    """This abstract class used to be inherited by PrimeNumber classes."""

    @abstractmethod
    def validate_prime(self, number: int):
        pass


class PrimeNumber(AbstractPrimeNumber):
    """This class used to represent prime number."""

    def __init__(self, number: int):
        """Initialisation of the attributes of the class PrimeNumber."""

        if self.validate_prime(number):
            self.number = number

    def validate_prime(self, number: int):
        """Return True if number is prime, otherwise False."""

        if isinstance(number, int):
            for num in range(2, number):
                if not number % num:
                    break
                return True
        return False

    def __str__(self):
        return str(self.number)


class PrimeNumberNonABC:
    """This class used to represent prime number."""

    def __init__(self, number: int):
        """Initialisation of the attributes of the class PrimeNumber."""

        if self.validate_prime(number):
            self.number = number

    def validate_prime(self, number: int):
        """Return True if number is prime, otherwise False."""

        if isinstance(number, int):
            for num in range(2, number):
                if not number % num:
                    break
                return True
        return False

    def __str__(self):
        return str(self.number)


AbstractPrimeNumber.register(PrimeNumberNonABC)
