from math import gcd
class Frac:
    """ Fractional class. A Frac is a pair of integers num, den(with den!=0) whose gcd is 1."""

    def __init__(self, n, d):# 类的构造函数
        """ Construct a Frac from integers n and d.
            Need error message if d =0!"""
        assert d != 0, "The denumeritor should not be 0!"
        hcf = gcd(n, d)
        self.num, self.den = n/hcf, d/hcf

    def __str__(self):
        """ Generate a string representation of a Frac. """
        if self.den == 1:
            return "%d" % (self.num)
        else:
            return "%d/%d" % (self.num, self.den)

    def __mul__(self, another):
        """ Multiply 2 Fracs to produce a Frac. """
        return self.num*another.num / (self.den*another.den)

    def __add__(self, another):
        """ Add 2 Fracs to produce a Frac. """
        return Frac(int(self.num*another.den+self.den*another.num), int(self.den*another.den))

    def __div__(self, another):
        """ Divide a Fracs to produce a new Frac. """
        return Frac(int(self.num*another.den), int(self.den*another.num))

    def __sub__(self, another):
        """ Sub a Fracs to produce a new Frac. """
        return Frac(int(self.num*another.den-self.den*another.num), int(self.den*another.den))
    def to_real(self):
        """ Return floating point value of Frac. """
        return float(self.num/float(self.den))

if __name__ == "__main__":
        a = Frac(3,7)
        b = Frac(24, 56)
        print("a.num = ",  a.num)
        print(", a.den =  ", a.den)
        print(a)
        print(b)
        print("floating point value of a is ", a.to_real())
        print("product = ", a*b)
        print("Sum = ", a+b)
        print("Sub = ", a - b)
        print(Frac(24, 1))
        print("Div = ", a.__div__(b))
        print("Div = ", a.__div__(b))
        #Frac(24, 0)
