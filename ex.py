# Examples used to test the main symbolic fuzzer function
import math

def check_triangle(a: int, b: int, c: int) -> int:
    if a == b:
        if a == c:
            if b == c:
                return "Equilateral"
            else:
                return "Isosceles"
        else:
            return "Isosceles"
    else:
        if b != c:
            if a == c:
                return "Isosceles"
            else:
                return "Scalene"
        else:
            return "Isosceles"



def abs_value(x: float) -> float:
    if x < 0:
        v: float = -x
    else:
        v: float = x
    return v


def gcd(a: int, b: int) -> int:
    if a < b:
        c: int = a
        a = b
        b = c

    while b != 0:
        c: int = a
        a = b
        b = c % b
    return a


def detect_triangle (a: int, b: int, c: int) :
    if a + b > c:
        return True

    if c + a > b:
        return True
        
    if b + c > a:
        return True

    else:
        return False

def sum(*args):
    temp_sum = 0
    for value in args:
        temp_sum += value
    return temp_sum