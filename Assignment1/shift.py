import random
from encryption_scheme import alphabet

c = 'e11wft9}t4q0hdjntg8x7it6'

random.seed(2107)

shifts = []

for i in range(len(c)):
    shifts.append(random.randint(0, len(alphabet)))

def decrypt(c):
    acc = []
    for i in range(len(c)):
        new_index = (alphabet.index(c[i]) - shifts[i]) % len(alphabet)
        acc.append(alphabet[new_index])
    return ''.join(acc)

print (decrypt(c))
