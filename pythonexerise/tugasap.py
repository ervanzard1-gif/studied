#nama=input('masukan nama anda = ')
#umur=int(input('masukan umur anda = '))
#datajenisk=['pria','wanita']
#print('1-pria dan 2-wanita')
#jenisk=int(input('masukan kode jenis kelamin anda = '))
#jkelamin=datajenisk[jenisk-1]    
#print('\n')
#print(f'''nama anda = {nama}
#umur anda = {umur}
#jenis kelamin anda = {jkelamin}''')
#
#if umur<=12 and jkelamin=='pria':
#    print(f'{nama} anda seorang {jkelamin} yang masih kecil')
#elif umur<=18 and jkelamin=='pria':
#    print(f'{nama} anda seorang {jkelamin} remaja')
#elif umur>18 and jkelamin=='pria':
#    print(f'{nama} anda seorang {jkelamin} dewasa')
#
#elif umur<=10 and jkelamin=='wanita':
#    print(f'{nama} anda seorang {jkelamin} yang masih kecil')
#elif umur<=16 and jkelamin=='wanita':
#    print(f'{nama} anda seorang {jkelamin} remaja')
#elif umur>16 and jkelamin=='wanita':
#    print(f'{nama} anda seorang {jkelamin} dewasa')
#print('\n')
#

#2
#nama=input('masukan nama mahasiswa = ')
#npm=input('masukan NPM = ')
#kelas=input('masukan kelas = ')
#print('\n')
#print(f'nama mahasiswa = {nama}')
#print(f'NPM mahasiswa = {npm}')
#print(f'kelas mahasiswa = {kelas}')
#
#if npm[2]=='4' and npm[0]=='1' and len(npm)==8:
#    print('program studi = Teknik Elektro')
#elif npm[2]=='4' and npm[0]=='2' and len(npm)==8:
#    print('program studi = Teknik Mesin')
#
#elif npm[2]=='4' and npm[0]=='3' and len(npm)==8:
#    print('program studi = Teknik Industri')
#
#elif npm[2]=='4' and npm[0]=='4' and len(npm)==8:
#    print('program studi = Agroteknologi')
#
#elif npm[2]=='4' and npm[0]=='5' and len(npm)==8:
#    print('program studi = Informatika')
#else:print('ada kesalahan di NPM')
#print('\n')
#


#3
barang=int(input('banyaknya barang yang dibeli = '))
if barang<100:
    hargatotal=barang*10000
    print(f'haraga yang harus dibayar untuk {barang} buah adalah Rp.{hargatotal}')
elif 100<=barang<150:
    hargatotal=barang*9500
    print(f'haraga yang harus dibayar untuk {barang} buah adalah Rp.{hargatotal}')
elif barang>=150:
    hargatotal=barang*9000
    print(f'haraga yang harus dibayar untuk {barang} buah adalah Rp.{hargatotal}')
print('\n')


