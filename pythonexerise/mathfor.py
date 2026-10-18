import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3

jagorenang={'evan','kai','sofia','gaby'}
jagobola={'evan','kai'}
jagonyanyi={'kai','sofia','gaby'}

plt.figure('marcel suka betit')
venn3([jagobola,jagonyanyi,jagorenang],set_labels=('jago bola',' jago nyanyi','jago renang'))
plt.show()