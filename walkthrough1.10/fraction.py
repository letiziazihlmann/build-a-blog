#has-a
    #numerator
    #denominator
#can-do
    #addition(fraction) output:fraction
    #multiplication(fraction) output:
    #reciprocal output: fraction
    #simplify output:fraction

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    def add(self, operand):
        commonDenom = self.denominator * operand.denominator
        newNumerator1 = self.numerator * operand.denominator
        newNumerator2 = operand.numerator * self.denominator
        finalNumerator = newNumerator1 + newNumerator2
        answer = Fraction(finalNumerator, commonDenom)
        return answer

    def multiply(self, operand):
        return Fraction(self.numerator*operand.numerator, self.denominator*operand.denominator)

    def reciprocal(self):
        return Fraction(self.denominator, self.numerator)

frac1 = Fraction(2,3)
frac2 = Fraction(1,4)
print(frac1.multiply(frac2))
print(frac1.add(frac2))
print(frac1.reciprocal())
