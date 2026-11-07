def xor(p,q):
    return (p or q) and not (p and q)

def implikasi(p,q):
    return not p or q   

def biimplikasi(p,q):
    return (p and q) or ( not p and not q)