from numpy import *
from matplotlib.pyplot import *
def initial(i):
	for e in i:
		def f(x,t):
			return sin(x)	
		a=0		#lower limit
		b=5		#upper limit
		N=1000
		h=(b-a)/N	#steps
		x=e
		
		tpoints=arange(a,b+h,h)
		xpoints=[]

		for t in tpoints:
			xpoints.append(x)
			k1=h*f(x,t)
			k2=h*f(x+0.5*k1,t+0.5*h)
			k3=h*f(x+0.5*k2,t+0.5*h)
			k4=h*f(x+k3,t+h)
			x+=(k1+2*k2+2*k3+k4)/6.0
			
		plot(tpoints, xpoints, label=r'$x_0$={0}'.format(round(e,2)))
	xlabel('t')
	ylabel('x')
	legend(loc='best')
	axvline(0, lw=1, color='black')
	axhline(0, lw=1, color='black')
	savefig('Fig_2.1.3.png')
	show()
initial(arange(-2*pi,2*pi+pi/2,pi/2))
