import array
def sort(a):
    i = 0
    while i < len(a) - 1:
        j = len(a) - 1
        while j >= i + 1:
            if a[j] < a[j-1]:
                temp = a[j]
                a[j] = a[j-1]
                a[j-1] = temp
            j -= 1
        i += 1

def main():
    a = array.array('i', [50, 10, 30, 40, 20])
    print('Sebelum diurutkan: ')
    for nilai in a:
        print('%d' % nilai, end=' ')
    print('\n')
    #  mengurutkan array
    sort(a)
    print('Setelah diurutkan: ')
    for nilai in a:
        print('%d' % nilai, end=' ')
if __name__ == '__main__':
    main()