import sympy
x = sympy.Symbol('x')
f = x**2 + 1

print(f.subs(x,1))

import sympy
x, y = sympy.symbols('x y')
print(sympy.solve(2*x + 6 - y))


x = sympy.symbols('x')
f = x**2
g = x + 3
print('f(g(x)) =', sympy.compose(f,g))    
# (f o g)(x) atau f(g(x))
print('g(f(x)) =', sympy.compose(g,f))    
