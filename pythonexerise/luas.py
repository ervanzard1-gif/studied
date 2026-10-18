#program menghitung luas

dataprogram=['persegi panjang','segitiga','persegi','lingkaran']

datakode=int(input('masukan kode data bangun ruang yang ingin dihitung = '))
datadituju=dataprogram[datakode-1]

if datadituju=='persegi panjang':
    panjang=int(input('masukan data panjang = '))
    lebar=int(input('masukan data lebar = '))
    hasil= panjang*lebar
    print('hasil luas persegi panjang = ',hasil)

elif datadituju=='segitiga':
    alas=int(input('masukan data alas = '))
    tinggi=int(input('masukan data tinggi = '))
    hasil=(alas*tinggi)/2
    print('hasil luas segitiga = ',hasil)

elif datadituju=='persegi':
    sisi=int(input('masukan panjang sisi = '))
    hasil=sisi**2
    print('hasil luas persegi = ',hasil)

elif datadituju=='lingkaran':
    jari2=int('masukan jari jari = ')
    hasil=(22/7)*(jari2**2)
    print('hasil luas lingkaran = ',hasil)


    