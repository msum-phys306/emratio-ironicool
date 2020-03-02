import numpy as np

def HH_field(N, I, L):
    """
    Determine magnetic field of a Helmholtz pair.

    Arguments:
    N -- the number of loops wrapped on a coil
    I --  the current through the coils, in Amps
    L --the radius of a coil, or the separation between the two sides.


    Return
    float Bfield--magnetic field strength in Teslas


    """
    mu = 4 * (1.0e-7)*np.pi # Corrected mu0
    return 8 * mu * N * I / (np.sqrt(125 )* L)

####################################################
def Lorentz_force(q, v, B):
    """
    Determine Lorentz force on a moving charge.

    Arguments:
    q -- value and sign of charge in Coulombs
    v --  array of velocity components (x, y, z)
    B --array of magnetic field components (x,y,z)


    Return
    array force--magnetic force components (x,y,z)
    """
    return np.cross(q*v, B)

# the voltage difference experience by the electron


