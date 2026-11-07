jmlrokok=int(input('masukan jumlah rokok yang terjual = '))


labarokok=1000*jmlrokok

print(f'maka keuntungan utama = {labarokok}')
bonus=0
if jmlrokok>=1000:
    bonus=+(2/10)*labarokok

print(f'bonus = {bonus} ')
print(f'total = {bonus+labarokok}')




jmlrokok=int(input('masukan jumlah rokok yang terjual = '))


labarokok=1000*jmlrokok
if jmlrokok>=1000:
    total=labarokok+(2/10)*labarokok
    print(f'maka total ditambah dengan bonus = {total}')
else:print(f'maka total tanpa bonus = {labarokok}')





