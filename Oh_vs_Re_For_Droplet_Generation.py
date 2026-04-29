import numpy as np
import matplotlib.pyplot as plt

from matplotlib.collections import PatchCollection
from matplotlib.patches import  Polygon


def Oh_vs_Re(sigma = 0.072, rho = 997, mu = 0.0010016, U_init = 4, dn = 50e-6,):
    ''' The function Oh_vs_Re() calculates and draws the position for a droplet of a 
    given liquid in the control parameter space.

    Input:
        sigma  - liquid surface tension [N/m];
        rho      - liquid density         [kg/m**3];
        mu      - dynamic viscosity      [Pa*s];
        dn       - characteristic length  [m], e.g., diameter of the nozzle orifice.
        U_init  - initial velocity of droplet.
        
    By default, the function calculates the dimensionless parameters for a water droplet.

    Output: 
        tc    - capillary time;
        U_min - minimal velocity needed for droplet formation derived from the Weber number (We);
        We    - Weber number;
        Re    - Reynolds number;
        Oh    - Ohnesorge number;
        Bo    - Bond number;
'''
    if U_init != 0:
        U_min = U_init
    else:
        U_min = np.sqrt(4*sigma/rho/dn)
    Re = U_min*rho*dn/mu
    We = U_min**2*rho*dn/sigma
    Oh = np.sqrt(We)/Re
    Bond = rho*dn**2*9.81/sigma
    tc = np.sqrt(rho*dn**3/sigma)

    print('-------------')
    print('U = {:.4f} [m/sec]'.format(U_min))
    print('tc = {:.2f} [us]'.format(tc*1e6))
    print('-------------')
    print('Re = {:.4f}'.format(Re))
    print('We = {:.4f}'.format(We))
    print('Oh = {:.4f}'.format(Oh))
    print('Z = {:.4f}'.format(1/Oh))
    print('Bond = {:.4f}'.format(Bond))
    print('-------------')
    
    
    
    fig, ax = plt.subplots()

    patches = []
    polygon = Polygon([(1,2), (200,0.01), (1,0.01), (1,2)])
    patches.append(polygon)
    
    polygon = Polygon([(200,0.01), (20,0.1),
                                   (1000,0.1), (1000,0.01)])
    patches.append(polygon)
    
    polygon = Polygon([(2,1), (1, 2.017),
                                   (1,10), (1000,10),(1000,1)])
    patches.append(polygon)
    
    polygon = Polygon([(2,1), (20, 0.1),
                                   (1000,0.1), (1000,1),(2,1)])
    patches.append(polygon)

    colors = [(1,0,0), (1,1,0), (0,0,1), (0,1,0)]
    p = PatchCollection(patches,facecolors=colors,alpha=0.5)
    
    ax.add_collection(p)
    
    ax.scatter(Re,Oh)
    ax.scatter(Re,Oh)
    plt.plot(np.array([1,200]),np.array([2,0.01]),color='r',linewidth=2)
    plt.plot(np.array([1,1000]),np.array([1,1]))
    plt.plot(np.array([1,1000]),np.array([0.1,0.1]))

    plt.ylabel('Ohnesorge Number, Oh')
    plt.xlabel('Reynolds Number, Re')
    plt.text(3,1.4,'Too viscous')
    plt.text(3,0.02,'Insufficient Energy for Drop Formation',rotation = -37)
    plt.text(40,0.7,'Region of Stable Generation')
    plt.text(90,0.05,'Satellite Droplets')
    plt.loglog()
    plt.ylim(0.01,10)
    plt.xlim(1,1000)
## Uncomment the line below to export the figure.
##    plt.savefig(r'Example.png', dpi=600)
    plt.show()

Oh_vs_Re()



