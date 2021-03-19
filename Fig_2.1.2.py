from numpy import *
from matplotlib.pyplot import *

def f(x,t):
	return sin(x)
	
a=0		#lower limit
b=8		#upper limit
N=1000
h=(b-a)/N	#steps
x=pi/4		#initial conditions

tpoints=arange(a,b+h,h)
xpoints=[]

for t in tpoints:
	xpoints.append(x)
	k1=h*f(x,t)
	k2=h*f(x+0.5*k1,t+0.5*h)
	k3=h*f(x+0.5*k2,t+0.5*h)
	k4=h*f(x+k3,t+h)
	x+=(k1+2*k2+2*k3+k4)/6.0
	

plot(tpoints, xpoints, color='red')
xlabel('t')
ylabel('x')
axhline(1.57, color='black', lw=1.5, ls='--')
axhline(3.14, color='black', lw=1.5, ls='--')
axvline(0, lw=1)
axhline(0, lw=1)
savefig('Fig_2.1.2.png')
show()

