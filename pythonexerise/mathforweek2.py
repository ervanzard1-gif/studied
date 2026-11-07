#A={1,2,3,4}
#B={2,4,8,9,15,16}
#R={(a,b)for a in A for b in B if b%a==0}
#print(R)
#
#

def is_reflexive(R,A):
    for a in A:
        if (a,a) not in R:
            return False
    return True

def main():
    A={1,2,3,4}
    R={(1,1),(2,2),(3,3)}
    BreflexA=is_reflexive(R,A)
    print(BreflexA)
main()