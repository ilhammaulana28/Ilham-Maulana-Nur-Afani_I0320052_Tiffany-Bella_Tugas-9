import sys

kamus = {'one': 'satu',
         'two': 'dua',
         'three': 'tiga',
         'four': 'empat',
         'five': 'lima',
         'six': 'enam',
         'seven': 'tujuh',
         'eight': 'delapan',
         'nine':'sembilan',
         'ten': 'sepuluh'}


def main ():
    kata = input('Masukkan kata dalam bahasa inggris: ')

    if not  (kata in kamus.keys()):
        print("'%s' tidak dapat ditemukan dalam kamus ini" % kata)
        sys.exit(1)

    print('Arti kata "%s" adalah "%s"' % (kata, kamus[kata]))


if __name__ == '__main__':
    main()