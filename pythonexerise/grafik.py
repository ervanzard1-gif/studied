import numpy as np
import matplotlib.pyplot as plt
# Definisi fungsi f
def f(x):
  return 2*x+1
x = np.linspace(-10, 10)    
y = f(x)
plt.figure()
plt.plot(x, y, label='f(x)')
plt.title('Grafik Fungsi f(x) = x^2')    
plt.xlabel('x')    

# Subset dari domain untuk cakupan sumbu x grafik
# Judul grafik
# Label sumbu x
plt.ylabel('f(x)') # Label sumbu y
plt.show()