# implementing the tonelli-shanks algorithm to find the square
# root of quadratic residues

# check if n is a quadratic residue
def is_quadratic(n, p):
    if (pow(n, (p - 1) // 2, p) == 1):
        print(n, "is a quadratic residue")
    else:
        return False

# tonelli-shanks algorithm
def tonelli_shanks(n, p):
    # step 0.5: tonelli-shanks is optimised for primes of the form 4k + 1
    # for the primes of form 4k + 3, there is already an algorithm using legendre symbol
    # and fermat's little theorem, we will just check for that now

    if (p % 4 == 3):
        r = pow(n, (p + 1) // 4, p)

    elif (p % 4 == 1):
        # step 1: initialising Q and S such that p - 1 = Q2^S
        S = 0
        Q = p - 1
        while (Q % 2 == 0):
            S += 1
            Q //= 2

        # step 2: search for an element z in F_p which is a quadratic non-residue
        z = 1
        while (pow(z, (p - 1) // 2, p) != p - 1):
            z += 1  
        
        # step 3: initialising variables M, c, t, R
        M = S
        c = pow(z, Q, p)
        t = pow(n, Q, p)
        R = pow(n, (Q + 1) // 2, p)

        # step 4: loop d loop
        if (t == 0):
            r = 0
        elif (t == 1):
            r = R
        else:
            while (t != 1):
                i = 1
                while (pow(t, pow(2, i, p), p) != 1):
                    i += 1
                b = pow(c, pow(2, M - i - 1, p), p)
                M = i
                c = pow(b, 2, p)
                t = t * pow(b, 2, p) % p
                R = R * b % p 
            r = R

    return r

a = 8479994658316772151941616510097127087554541274812435112009425778595495359700244470400642403747058566807127814165396640215844192327900454116257979487432016769329970767046735091249898678088061634796559556704959846424131820416048436501387617211770124292793308079214153179977624440438616958575058361193975686620046439877308339989295604537867493683872778843921771307305602776398786978353866231661453376056771972069776398999013769588936194859344941268223184197231368887060609212875507518936172060702209557124430477137421847130682601666968691651447236917018634902407704797328509461854842432015009878011354022108661461024768
p = 30531851861994333252675935111487950694414332763909083514133769861350960895076504687261369815735742549428789138300843082086550059082835141454526618160634109969195486322015775943030060449557090064811940139431735209185996454739163555910726493597222646855506445602953689527405362207926990442391705014604777038685880527537489845359101552442292804398472642356609304810680731556542002301547846635101455995732584071355903010856718680732337369128498655255277003643669031694516851390505923416710601212618443109844041514942401969629158975457079026906304328749039997262960301209158175920051890620947063936347307238412281568760161


is_quadratic(a, p)
print(tonelli_shanks(a, p))