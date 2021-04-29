import array
b = array.array('c')
b.fromstring("Python")
for karakter in b:
    print('%c' % karakter, end='')
