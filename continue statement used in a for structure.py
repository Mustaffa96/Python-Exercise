# Fig. 3.26: fig03_26.py
# Using the continue statement in a for/in structure.

for x in range( 1, 11 ):

    if x == 5:
        continue

    print (x),

print ("\nUsed continue to skip printing the value 5")