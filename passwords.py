import random

chars = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

print( "           " )
print( "           " )
print( "╔═══╗╔══╗╔══╗╔══╗╔╗╔╗╔╗╔══╗╔═══╗╔══╗─╔══╗" )        
print( "║╔═╗║║╔╗║║╔═╝║╔═╝║║║║║║║╔╗║║╔═╗║║╔╗╚╗║╔═╝" )
print( "║╚═╝║║╚╝║║╚═╗║╚═╗║║║║║║║║║║║╚═╝║║║╚╗║║╚═╗" )
print( "║╔══╝║╔╗║╚═╗║╚═╗║║║║║║║║║║║║╔╗╔╝║║─║║╚═╗║" )
print( "║║───║║║║╔═╝║╔═╝║║╚╝╚╝║║╚╝║║║║║─║╚═╝║╔═╝║" )
print( "╚╝───╚╝╚╝╚══╝╚══╝╚═╝╚═╝╚══╝╚╝╚╝─╚═══╝╚══╝" )
print( "           " )
print( "           " )

number = int( input( "amount: " + "\n" ) )
lenght = int( input( "lenght: " + "\n" ) )
for x in range( number ):
    password = ""
    for i in range( lenght ):
        password += random.choice( chars )
    print( password )

    file = open( "pass.txt", "a" )
    file.write( "\n" + password )
    file.close()
