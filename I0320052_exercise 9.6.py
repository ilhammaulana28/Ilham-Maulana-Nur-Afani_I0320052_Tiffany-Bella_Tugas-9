import array
a = array.array('i')
a.append(50)
a.append(-20)
a.append(30)
a.insert(1, 40)
for nilai in a:
    print('%d' % nilai, end=',')
print('')
i = 0
while i < len(a):
    print('%d' % a[i], end=',')
    i += 1
print('')
check = a.index(30)
print(check)