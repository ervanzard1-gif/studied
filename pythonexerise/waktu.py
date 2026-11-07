datadetik=int(input('masukan jumlah detik = '))

jam=datadetik//3600
menit=(datadetik%3600)//60
detik=(datadetik%3600)%60

print(f'{jam} jam, {menit} menit, {detik} detik')