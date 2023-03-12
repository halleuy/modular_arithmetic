# by fermat's little theorem:
# 3 ^ (13 - 1) = 1 mod 13
# 3 ^ 12 = 1 mod 13
# 3 * 3^11 = 1 mod 13 => d = 3^11

# F_p is defined as the field {0, 1, 2, ..., p-1} i.e. range(p)
def invert(a, p):
    if (a == 0):
        return 0
    for i in range(p):
        if ((a * i) % p == 1):
            return i

print(invert(3,13))

# alternate solution making use of the blurb on top
def invert2(a, p):
    if (a == 0):
        return 0
    d = (a ** (p - 2)) % p
    return d

print(invert2(3,13))