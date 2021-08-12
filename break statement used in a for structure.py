# Fig. 3.24: fig03_24.py
# Using the break statement in a for structure.

for x in range( 1, 11 ):

    if x == 5:
        break

    print (x),

print ("\nBroke out of loop at x =", x)