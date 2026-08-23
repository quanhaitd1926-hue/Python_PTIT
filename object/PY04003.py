import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplifiedFraction(self):
        gcd = math.gcd(self.numerator, self.denominator)
        return f"{int(self.numerator / gcd)}/{int(self.denominator / gcd)}"



if __name__ == '__main__':
    numerator, denominator = map(int, input().split())
    F = Fraction(numerator, denominator)
    print(F.simplifiedFraction())