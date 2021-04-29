import array
#  exercise 9.9
a = array.array('i', [100, 200, 300, 400, 500])
print(a)
a[1] = -700
a[4] = 800
print(a)

#  exercise 9.10
#  nilai awal sebelum reverse
print(a)

a.reverse()
#  nilai setelah dibalik
print(a)