#Abbas 18.09.25 1415

import string, random
from random import shuffle

def luoSalasana(): 

    random_source = string.ascii_letters + string.digits + string.punctuation

    password    =   random.choice(string.ascii_uppercase)
    password    +=  random.choice(string.ascii_uppercase)
    password    +=  random.choice(string.digits)
    password    +=  random.choice(string.punctuation)

    for i in range (8):
        password += random.choice(random_source)

    passowrd_list = list(password)
    random.shuffle(passowrd_list)
    salasana = ''.join(passowrd_list)
    return salasana

print('Slasana on: ', luoSalasana())