def encode(sc):
    import string
    import re

    # sc = raw_input('please input:')
    l = list(sc)

    lst = []
    for word in string.lowercase:
        lst.append(word)
    lst2 = []
    for word in string.uppercase:
        lst2.append(word)

    m = []
    for i in l:
        if re.match('^[a-z]+$', i):
            num = lst.index(i)
            if num % 2 == 0:
                m.extend('0')
            elif num % 2 == 1:
                m.extend('1')
        elif re.match('^[A-Z]+$', i):
            num = lst2.index(i)
            if num % 2 == 0:
                m.extend('0')
            elif num % 2 == 1:
                m.extend('1')
        else:
            m.extend(i)
    scrit = ''.join(m)
    print scrit


encode('Hello World!')
