p = 845529816183328832288826827978944092433
g = 419182772165909068703324756801961881648
ga = 803331951724823196054726562340183173391
gb = 382083902245594277300548430928765321436

# From calculator
a = 3499166536901693766286466928751407646
b = 2764982533026574259926634274221654820

# Fast modular exponentiation
def f(x,e,m):
    X = x
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E = E >> 1
        else:
            Y = (X * Y) % m
            E = E - 1
    return Y

# Sanity check
na = f(g, a, p)
nb = f(g, b, p)

print(na, na == ga, nb, nb ==gb)

# Shared key
s = f(g, a*b, p)
print(s)