# for p = 29, a = 11, a^2 = 5 mod 29
# 5 is a quadratic residue of mod 29, and is also the square root of 11
# to generalise: for prime p and integer a within F_p,
# a^2 = x mod p, x is a quadratic residue of mod p and a is the square root of x

def residue(a, p):
    residue = []
    for i in range(1, p):
        r = (i ** 2) % p
        residue.append(r)

    if a in residue:
        return(str(a) + " is a quadratic residue mod " + str(p))
    else:
        return(str(a) + " is a non-quadratic residue mod " + str(p))

ints = [14, 6, 11]
for i in range(len(ints)):
    print(residue(ints[i], 29))

def residue_square_root(x, p):
    for i in range(1, p):
        y = (i ** 2) % p
        if (y == x):
            return i, p - i

print(residue_square_root(6, 29))
