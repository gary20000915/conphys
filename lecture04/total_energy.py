"""

This program calculate the total energy from 
a set of data that include times, velocities, 
and heights.

2023.03.13
Kuo-Chuan Pan

"""

def main():
    """
    
    The main function to compute the total energy
    """
    # constants
    MASS = 1.5  # (kg)
    G    = 9.81 # (m/s^2)

    # read the data 
    data = load_data()

    # compute total energy
    tot_energies = []
    sum_etot = 0.0

    for t, v, h in zip(data["times"],data["velocities"],data["heights"]):
    
        ekin = 0.5 * MASS * v**2
        epot = MASS*G*h
        etot = ekin + epot
        sum_etot += etot

        tot_energies.append(etot)
        #print("debug: etot",etot)
    
    # calculate the averaged tot energy.
    npoints  = len(data["times"])
    etot_ave = sum_etot / npoints
    print("Answer: the averaged total energy is ", etot_ave)

    return 

def load_data():
    """
    initialize the data points
    """

    times = [0.004, 0.215, 0.417,
             0.605, 0.813, 1.003,
             1.209, 1.411, 1.602,
             1.805]
    
    velocities = [0.013, 0.679, 1.306,
                  1.920, 2.638, 3.236,
                  3.897, 4.516, 5.010,
                  5.803]
    
    heights = [2.004, 1.987, 1.988,
               1.862, 1.684, 1.573,
               1.327, 1.070, 0.768,
               0.416]

    data = {}
    data["times"] = times
    data["velocities"] = velocities
    data["heights"]= heights

    return data

if __name__=='__main__':

    # run the main function
    main()
