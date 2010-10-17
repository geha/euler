from decimal import getcontext
import problem_26
from decimal import *
dig = problem_26.get_digits(7)

print (dig)
getcontext().prec = 100
tmp = Decimal(1) / Decimal(7)
print (len(dig))
