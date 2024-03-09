import sys
import fractions
a,b=map(int,sys.stdin.readline().rstrip().split())


re=fractions.Fraction(b-a,b)

print(re.numerator,re.denominator)