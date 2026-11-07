#ef data(a,b):
#    a+b
#   
#asil=data(2,4)
#rint(hasil)
#
#ef data(a,b):
#    return a+b
#   
#asil=data(2,4)
#rint(hasil)

#calculator part 2

def operator(x):
    match x.split(' '):
        case [x,'+',y]:
            print(int(x)+int(y))
        case [x,'-',y]:
            print(int(x)-int(y))
        case [x,'/',y]:
            print(int(x)/int(y))
        case [x,'x',y]:
            print(int(x)*int(y))
        case [x,'^',y]:
            print(int(x)**int(y))

operator('2 + 3')

def kali_kartesian(A,B):
    product=set()
    for a in A:
        for b in B:
            product.add((a,b))
    return product

def main():
    A=['a','b']
    B=[1,2]
    A_x_B=kali_kartesian(A,B)
    print(A_x_B)
    return

main()




