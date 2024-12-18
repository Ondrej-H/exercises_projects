from random import randrange

def tell_shape(num):
    if num == 0:
        shape = "triangle"
    elif num == 1:
        shape = "square"
    else:
        shape = "circlet"       # circlet nebo roundlet znamená kolečko
    return shape


num = randrange(3)
print(tell_shape(num))