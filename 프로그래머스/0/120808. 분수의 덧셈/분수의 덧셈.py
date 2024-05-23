def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solution(numer1, denom1, numer2, denom2):
    numer = (numer1 * denom2) + (numer2 * denom1)
    denom = denom1 * denom2
    
    common_divisor = gcd(numer, denom)
    
    reduced_numerator = numer // common_divisor
    reduced_denominator = denom // common_divisor
        
    answer = [reduced_numerator, reduced_denominator]
    return answer
