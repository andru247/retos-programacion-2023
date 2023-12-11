entry = input('Lenguaje Natral a Lenguaje Hacker: ')
leet = {'a' : '4',
        'b' : 'IB',
        'c' : '[',
        'd' : ')',
        'e' : '3',
        'f' : '|=',
        'g' : '&',
        'h' : '#',
        'i' : '1',
        'j' : ',_|',
        'k' : '>|',
        'l' : '1',
        'm' : "/\/\ ", # Quitar espacio
        'n' : '^/',
        'o' : '0',
        'p' : '|*',
        'q' : '(_,)',
        'r' : 'I2',
        's' : '5',
        't' : '7',
        'u' : '(_)',
        'v' : '\/',
        'w' : '\/\/',
        'x' : '><',
        'y' : 'j',
        'z' : '2'
        }
new_str = ''

for i in entry:
    if i.lower() in leet:
        new_str += leet[i.lower()]
    else:
        new_str += i

print(new_str)
