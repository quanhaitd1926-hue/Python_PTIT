import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def sumTwoFraction(self, q):
        lcm = math.lcm(self.denominator, q.denominator)
        self.numerator *= lcm / self.denominator
        q.numerator *= lcm / q.denominator
        tmp = Fraction(self.numerator + q.numerator, lcm)
        gcd = math.gcd(int(tmp.numerator), int(tmp.denominator))
        return f"{int(tmp.numerator / gcd)}/{int(tmp.denominator / gcd)}"

if __name__ == '__main__':
    numerator1, denominator1, numerator2, denominator2 = map(int, input().split())
    p = Fraction(numerator1, denominator1)
    q = Fraction(numerator2, denominator2)
    print(p.sumTwoFraction(q))