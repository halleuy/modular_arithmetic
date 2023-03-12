# extended euclidean algorithm
# finding the inverse modulo of 2 numbers

def x_gcd(a,b):

    if (a == 0):
        return b, 0, 1
    
    gcd, x1, y1 = x_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return(gcd, x, y)

g, u, v = x_gcd(26513, 32321)

print(u, v)
    
