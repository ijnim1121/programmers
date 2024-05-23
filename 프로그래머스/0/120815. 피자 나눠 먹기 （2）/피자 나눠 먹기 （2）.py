import math

def solution(n):
    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b)
    lcm = lcm(n, 6)
    pizza = lcm//6
    return pizza