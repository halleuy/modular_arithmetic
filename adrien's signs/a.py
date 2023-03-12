from random import randint

a = 288260533169915
p = 1007621497415251 # we can check what form of prime this is

FLAG = b'crypto{????????????????????}'

# breaking down this code like a baws
def encrypt_flag(flag):
    ciphertext = [] # initialises a list to store each element of this func


    plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag]) #turns each char
    # of flag into 1s and 0s and appends 8 additional 0s behind the 
    # generated bit
    # an example of this plaintext would be 10110100101010010

    for b in plaintext: # for each DIGIT in plaintext, apply the following 
    # formulas given

        e = randint(1, p) # generates a random integer from 1 to p

        n = pow(a, e, p) # n will turn into a scary large number

        if b == '1': # if the digit is equals to 1, then it will just be equals
                     # a^e = n mod p
            ciphertext.append(n)
        else:
            n = -n % p # if the digit is equals to 0, then it will be equals to
                       # n = -n mod p or n = p-n mod p 
            ciphertext.append(n)

    return ciphertext

print(encrypt_flag(FLAG))

# in order to reverse engineer this encryption, we need to check whether element
# of ciphertext was originally a 1 or 0
# before that however, we need to solve for what e is as for each element of 
# ciphertext, it is randomised from 1 to p (sounds like F_p)

        