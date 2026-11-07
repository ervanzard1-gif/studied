tahun=int(input('masukan tahun = '))
if tahun%400==0:
    print(f'{tahun} merupakan tahun kabisat')
elif tahun%100==0:
    print(f'{tahun} bukan merupakan tahun kabisat')
elif tahun%4==0:
    print(f'{tahun} merupakan tahun kabisat')
elif tahun&4!=0:
    print(f'{tahun} bukan merupakan tahun kabisat')



tahun=int(input('masukan tahun = '))
if tahun%400==0 or (tahun%4==0 and tahun%100!=0):
    print()
