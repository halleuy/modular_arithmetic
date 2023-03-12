# euclidean algorithm
# a = bq + r with r = a % b, r replacing b and b replacing a

def gcd(a, b):
    if (a < b):
        a, b = b, a
    while (b > 0):
        a, b = b, a % b
    return(a)
    
print(gcd(66528, 52920))