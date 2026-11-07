jmlrokok=int(input('masukan jumlah rokok yang terjual = '))


labarokok=1000*jmlrokok

print(f'maka keuntungan utama = {labarokok}')
bonus=0
if jmlrokok>=2000:
    total=labarokok+labarokok*(25/100)
    print(f'maka total dengan bonus 25% = {total}')
   

elif jmlrokok>=1000:
    total=labarokok+labarokok*(20/100)
    print(f'maka total dengan bonus 20% = {total}')


else:print(f'total penjualan tanpa bonus = {labarokok} ')
print('=================================\n====')

jmlrokok=int(input('masukan jumlah rokok yang terjual = '))


labarokok=1000*jmlrokok

print(f'maka keuntungan utama = {labarokok}')
bonus=0
if jmlrokok>=2000:
    total=labarokok+labarokok*(30/100)
    print(f'maka total dengan bonus 25% = {total}')
   

elif jmlrokok>=1500:
    total=labarokok+labarokok*(25/100)
    print(f'maka total dengan bonus 20% = {total}')

elif jmlrokok>=1000:
    total=labarokok+labarokok*(20/100)
    print(f'maka total dengan bonus 20% = {total}')

else:print(f'total penjualan tanpa bonus = {labarokok} ')
