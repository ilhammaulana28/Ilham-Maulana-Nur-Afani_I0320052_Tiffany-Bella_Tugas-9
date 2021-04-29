print('Exercise 9.1')

import sys

Hari = ('Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', "Jumat", 'Sabtu')

def main():
    nohari = int(input('Masukkan nomor hari (1...7): '))

    if (nohari < 1) or (nohari > 7):
        print('Tidak ada hari ke-%s' % nohari)
        sys.exit(1)

    print('Hari ke-%d adalah %s' % (nohari, Hari[nohari-1]))

if __name__ == '__main__':
    main()