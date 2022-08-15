import math


class Fraction:
    def __init__(self, numerator, denumerator):
        self.numerator = int(numerator)
        self.denumerator = int(denumerator)

    def __add__(self, other):
        znam = self.denumerator * other.denumerator // math.gcd(self.denumerator, other.denumerator)
        chisl = znam // self.denumerator * self.numerator + znam // other.denumerator * other.numerator
        return f"{chisl}/{znam}"


    def __sub__(self, other):
        znam = self.denumerator * other.denumerator // math.gcd(self.denumerator, other.denumerator)
        chisl = znam // self.denumerator * self.numerator - znam // other.denumerator * other.numerator
        return  f"{chisl}/{znam}"


    def __mul__(self, other):
        k = math.gcd(self.numerator, other.denumerator)
        self.numerator //= k
        other.denumerator //= k
        chisl = self.numerator * other.numerator
        znam = self.denumerator * other.denumerator
        return f"{chisl}/{znam}"


    def __floordiv__(self, other):
        k = math.gcd(self.denumerator, other.denumerator)
        self.denumerator //= k
        other.denumerator //= k
        chisl = self.numerator * other.denumerator
        znam = other.numerator * self.denumerator
        return f"{chisl}/{znam}"






num = Fraction(1, 4)
num2 = Fraction(1, 4)
print(num + num2)
print(num - num2)
print(num * num2)
print(num // num2)