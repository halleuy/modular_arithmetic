# for the system of linear congruences where a_i are arbitrary
# integers and n_i, n_j are pairwise coprime integers
# x = a_1 mod n_1
# x = a_2 mod n_2
# ...
# x = a_n mod n_n
# there is a uninue solution x = a mod N where N = n_1 * ... * n_n

# chinese remainder theorem
a1 = [2, 3, 5]
n1 = [5, 11, 17]

def crt(a, n):
    N = 1
    for i in range(len(n)):
        N *= n[i]
    # print(N)
    
    y = []
    for i in range(len(n)):
        y.append(N // n[i])
    # print(y)

    z = []
    for i in range(len(y)):
        z.append(pow(y[i], n[i] - 2, n[i]))
    # print(z)

    x = []
    for i in range(len(y)):
        x.append(a[i] * y[i] * z[i])
    sol = sum(x) % N
    print(sol)

crt(a1, n1)