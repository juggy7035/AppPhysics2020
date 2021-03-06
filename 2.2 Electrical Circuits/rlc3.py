from matplotlib.pyplot import plot, show, xlabel, ylabel, legend, grid, ylim, title, savefig, figure
from numpy import linspace, arctan, pi, sqrt


def gain(omega, r):
    l = 1e-3
    c = 1e-6
    I = 1j
    return abs(c*l*omega**2*r/(c*l*omega**2*r + (I*c*l*omega**2 + c*omega*r - I)*(I*c*l*omega**2*r + l*omega - I*r)))

def power1(omega, r):
    l = 1e-3
    c = 1e-6
    I = 1j
    return abs(c*omega*(I*c*l*omega**2*r + l*omega - I*r)/(c*l*omega**2*r + (I*c*l*omega**2 + c*omega*r - I)*(I*c*l*omega**2*r + l*omega - I*r)))**2*0.5*r


def power2(omega, r):
    l = 1e-3
    c = 1e-6
    I = 1j
    return abs((c*l*omega**2*r/(c*l*omega**2*r + (I*c*l*omega**2 + c*omega*r - I)*(I*c*l*omega**2*r + l*omega - I*r))))**2/(2*r)

omega = linspace(10000, 80000, 1000)
plot(omega/1000, gain(omega, 50), 'k-', label='R=50 $\Omega$')
plot(omega/1000, gain(omega, 100), 'r-', label='R=100 $\Omega$')
plot(omega/1000, gain(omega, 500), 'g-', label='R=500 $\Omega$')
plot(omega/1000, gain(omega, 1000), 'b-', label='R=1000 $\Omega$')


xlabel('$\omega$ (kHz)')
ylabel('V$_o$($\omega$)/V$_i$')
grid()
legend()
savefig('gain.jpg', dpi=500)
show()


rval = linspace(1, 2000, 2)
for Resistance in rval:
    print(Resistance)
    plot(omega/1000, power1(omega, Resistance)*2*Resistance, 'k-', label='resistor 1')
    plot(omega/1000, power2(omega, Resistance)*2*Resistance, 'r-', label='resistor 2')
    xlabel('$\omega$ (kHz)')
    ylabel('P($\omega$)/P$_0$')
    grid()
    legend()
    title(str(round(Resistance,2)) +" $\Omega$")
    savefig(str(int(Resistance)), dpi=500, format='jpg')
    show()


