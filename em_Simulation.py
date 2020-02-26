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
    mu = 4 * np.pi
    return 8 * mu * N * I / (125 * L)

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

V_i = -60
V_f = -135
dV = V_f - V_i

q = -1.6e-19
m = 9.1e-31

# the electron speed assuming that it is at rest to begin with
e_speed = np.sqrt(2 * q * dV / m)
print(e_speed)
c = 2.99e8
print(e_speed/c)

# gives the magnitude but not the direction of the B field
Bmag = HH_field(300, 4, 0.2)
# setting the coordinates to align with what's in my notebook
B_field = np.array([Bmag, 0, 0])

# the lists below will contain the history of the position components
e_x = [0]
e_y = [0]
e_z = [0]

e_vel = np.array([0, 0, e_speed])
e_mom = m * e_vel
e_pos = np.array([0, 0, 0])

t = 0
dt = 1e-17

while e_pos[2] >= 0:
    
    e_force = Lorentz_force(q, e_vel, B_field)
    e_mom = e_mom + e_force * dt
    e_vel = e_mom / m
    e_pos = e_pos + e_vel * dt
    
    # below are 
    e_x.append(e_pos[0])
    e_y.append(e_pos[1])
    e_z.append(e_pos[2])
    
    t += dt

# below is the history of the position components as arrays
x_array = np.array(e_x)
y_array = np.array(e_y)
z_array = np.array(e_z)