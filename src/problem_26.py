from decimal import getcontext
from decimal import *

def get_digits(denominator):
    getcontext().prec = 100
    remainder = Decimal(1)/ Decimal(denominator)
    digits = []
    for i in range(1,101):
        remainder *= 10
        current = int(remainder%10)
        digits.append(current)

    return digits

def find_recurring_cycle(digits):
    for i in range(1, len(digits)):
        current = digits[i]
