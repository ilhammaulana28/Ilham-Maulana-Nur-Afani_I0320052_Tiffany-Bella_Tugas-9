import array
li = [10, 20, 30, 40, 50]
c = array.array('i')
c.fromlist(li)
a = type(c)
print(a)
for nilai in c:
    print('%d' % nilai, end=',')
