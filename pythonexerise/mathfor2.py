def kali_kartesian(A,B):
    product={}
    for a in A:
        for b in B:
            product.add((a,b))
    return product

def main():
    X={1,2,3}
    Y={'a','b','c'}
    X_x_Y=kali_kartesian(X,Y)
    print('X x Y = ',X_x_Y)

main()