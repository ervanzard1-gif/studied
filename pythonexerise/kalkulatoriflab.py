#kalkulator sederhana
print('\n')
angka1=float(input('masukan angka 1 = '))
angka2=float(input('masukan angka 2 = '))
operator=input('masukan operator(+,-,*,/) = ')

if operator=='+':
    hasil=angka1+angka2
    print(f'{angka1} + {angka2} = {hasil}')
elif operator=='-':
    hasil=angka1-angka2
    print(f'{angka1} - {angka2} = {hasil}')
elif operator=='*':
    hasil=angka1*angka2
    print(f'{angka1} * {angka2} = {hasil}')
elif operator=='/':
    if angka1==0 and angka2==0:
        print(f'{angka1} / {angka2} = tidak tentu')
    elif angka2==0:
        print(f'{angka1} / {angka2} = tidak terdefinisi')
    else:
        hasil=angka1/angka2
        print(f'{angka1} / {angka2} = {hasil}')
else:
    print('operator yang dimasukkan salah')
print('\n')