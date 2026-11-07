namabulan=['januari','februari','maret','april','mei','juni','juli','agustus','september','oktober','november','desember']
pilihanbulan=int(input('masukan nomor bulan = '))

if pilihanbulan>12:
    print('salah')
elif 1<=pilihanbulan<=12:  
    print(f'nama bulan = {namabulan[pilihanbulan-1]}')