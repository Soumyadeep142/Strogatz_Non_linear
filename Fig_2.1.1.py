from numpy import *
from matplotlib.pyplot import *

def f(x):
	return sin(x)
a=-20
b=20
N=10000
h=(b-a)/N
xpoints=arange(a,b+h,h)
x_dotpoints=f(xpoints)

plot(xpoints, x_dotpoints)
axvline(0, lw=1, color='black')
axhline(0, lw=1, color='black')
xlabel('x')
ylabel(r'$\dot x$')
savefig('Fig_2.1.1.png')
show()
