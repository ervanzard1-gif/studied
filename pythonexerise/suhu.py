celcius=float(input('masukan suhu dalam celcius = '))

fahrenheit=(celcius*9/5)+32
kelvin=celcius+273.15
reamur=4/5*celcius

print(f'celcius = {celcius:.2f} celcius')
print(f'fahrenheit = {fahrenheit:.2f} fahrenheit')
print(f'kelvin = {kelvin:.2f} kelvin')
print(f'reamur = {reamur:.2f} reamur')

print(f'{celcius:.2f} celcius = {fahrenheit:.2f} fahrenheit = {kelvin:.2f} kelvin = {reamur:.2f} reamur')