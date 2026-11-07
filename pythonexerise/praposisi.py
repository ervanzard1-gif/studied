x=True
print(not x)

print(f'|  p  |  -p  |')
for p in [True, False]:
    negp=not p
    print(f'| {p} | {negp} |')


print(f'|  p  |  q  |  p n q  |')
for p in [True, False]:
    for q in [True, False]:
        konj=p and q
        print(f'| {p} | {q} | {konj} |')

print(f'|  p  |  q  |  p v q  |')
for p in [True, False]:
    for q in [True, False]:
        disj=p or q
        print(f'| {p} | {q} | {disj} |')


def xor(p,q):
    return (p or q) and not (p and q)

print(f'|  p  |  q  |  p xor q  |')
for p in [True, False]:
    for q in [True, False]:
        hasil=xor(p,q)
        print(f'| {p} | {q} | {hasil} |')


def implikasi(p,q):
    return not p or q

print(f'|  p  |  q  |  p -> q  |')
for p in [True, False]:
    for q in [True, False]:
        hasil=implikasi(p,q)
        print(f'| {p} | {q} | {hasil} |')

def biimplikasi(p,q):
    return (p and q) or ( not p and not q)

print(f'|  p  |  q  |  p <-> q  |')
for p in [True, False]:
    for q in [True, False]:
        hasil=biimplikasi(p,q)
        print(f'| {p} | {q} | {hasil} |')


#ekuivalensi
import logika

kondisi=True
print(f'|  p  |  q  |  p-->q  |  -p v q  |')
for p in [True, False]:
    for q in [True,False]:
        hasil1=logika.implikasi(p,q)
        hasil2=not p or q
        if hasil1!=hasil2:
            kondisi=False

print(f'Kondisi ekuivalensi: {kondisi}')    