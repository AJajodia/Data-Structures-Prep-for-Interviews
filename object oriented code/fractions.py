# gcd function
def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return abs(n)


# fraction class with str, +, *, =, eq methods

class Fraction:

    def __init__(self, top, bottom):
        if top % 1 == 0 and bottom % 1 == 0:
            if bottom < 0:
                top = -top
                bottom = -bottom
            self.num = top
            self.den = bottom
        else:
            raise ValueError

    def __str__(self):
        if self.num != 0:
            return str(self.num) + "/" + str(self.den)
        else:
            return "0"

    def __repr__(self):
        if self.num != 0:
            return str(self.num) + "/" + str(self.den)
        else:
            return "0"

    def __add__(self, other):
        newnum = (self.num * other.den) + (self.den * other.num)
        newden = self.den * other.den
        if newnum != 0:
            return Fraction(newnum//gcd(newden, newnum), newden//gcd(newnum, newden))
        else:
            return Fraction(0, 0)
        # final = Fraction(newnum, newden)
        # for i in range(1, newden + 1):
        #     if newnum % i == 0 and newden % i == 0:
        #         final = Fraction(int(newnum/i), int(newden/i))
        # return final

    def __iadd__(self, other):
        self.num = (self.num * other.den) + (self.den * other.num)
        self.den = self.den * other.den
        if self.num != 0:
            return Fraction(self.num // gcd(self.den, self.num), self.den // gcd(self.num, self.den))
        else:
            return Fraction(0, 0)

    def __radd__(self, other):
        other = Fraction(other, 1)
        newnum = (self.num * other.den) + (self.den * other.num)
        newden = self.den * other.den
        if newnum != 0:
            return Fraction(newnum // gcd(newden, newnum), newden // gcd(newnum, newden))
        else:
            return Fraction(0, 0)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        return Fraction(newnum//gcd(newden, newnum), newden//gcd(newnum, newden))

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        if newnum != 0:
            return Fraction(newnum // gcd(newden, newnum), newden // gcd(newnum, newden))
        else:
            return Fraction(0, 0)

    def __sub__(self, other):
        return self + Fraction(-other.num, other.den)

    def __eq__(self, other):
        return self.num/self.den == other.num/other.den

    def __gt__(self, other):
        return self.num/self.den > other.num/other.den

    def __lt__(self, other):
        return self.num/self.den < other.num/other.den

    def __le__(self, other):
        return self.num/self.den <= other.num/other.den

    def __ge__(self, other):
        return self.num/self.den >= other.num/other.den

    def __ne__(self, other):
        return self.num/self.den != other.num/other.den

    def show(self):
        print(self.num, "/", self.den)


f1 = Fraction(1, 8)
f2 = Fraction(1, 8)

print(str(f1))
