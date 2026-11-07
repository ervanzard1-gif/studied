print('\n')
saldof=int(input('masukan saldo awal = '))
sukubt=int(input('masukan suku bunga per tahun = '))
lamasimpan=int(input('masukan lama simpanan = '))

print('\n')
periode=1
judul=(f'| {"Tahun":^8s} | {"Saldo Awal":^12s} | {"Bunga/Tahun":^12s} | {"Pajak":^10s} | {"Saldo Akhir":^12s} |')
print(judul)
print(len(judul)*"-")
while periode<=lamasimpan:
    bunga=saldof*sukubt/100
    saldosp=saldof+bunga
    if saldosp>7500000:
        pajak=bunga*20/100
        saldoakhir=saldosp-pajak

    else:
        pajak=0
        saldoakhir=saldosp
    print(f'| {periode:^8d} | {saldof:^12,.0f} | {bunga:^12,.0f} | {pajak:^10,.0f} | {saldoakhir:^12,.0f} |')

    periode+=1
    saldof=saldoakhir
print('\n')


  