# Finding the maximum of three integers.

def maximumvalue( x, y, z ):
    maximum = x

    if y > maximum:
        maximum = y

    if z > maximum:
        maximum = z

    return maximum

a = int( input( "Enter first integer: " ) )
b = int( input( "Enter second integer: " ) )
c = int( input( "Enter third integer: " ) )

# function call
print ("Maximum integer is:", maximumvalue( a, b, c ))
print ()# print new line

d = float( input( "Enter first float: " ) )
e = float( input( "Enter second float: " ) )
f = float( input( "Enter third float: " ) )
print ("Maximum float is: ", maximumvalue( d, e, f ))
print ()

g = input( "Enter first string: " )
h = input( "Enter second string: " )
i = input( "Enter third string: " )
print ("Maximum string is: ", maximumvalue( g, h, i ))