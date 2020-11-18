from math import pi
import numpy as np

 # d_list, xi_list, zi_list
def CG_calculator(fastener_details_list):
    """Calculate area of each fastener"""
    #get area for each fastener this is now correct
    A_list = []
    for i in fastener_details_list:  #goes through every item in list 
        r_fastener = i["diameter"]/2 #Changed this slightly. You can do this instead of range(len(d_list)) etc
        A_fastener = pi*(r_fastener**2)   #until here correct
        A_list.append(A_fastener)

    A_array = np.array(A_list)

    """Convert coordinates to float numbers"""
    #convert xi_list to float and put in array
    xi_listfloat = []
    for i in fastener_details_list:
        xi = float(i["coord_x"]) # Made similar change here
        xi_listfloat.append(xi)

    xi_array = np.array(xi_listfloat)

    #convert zi_list to float and put in array
    zi_listfloat = []
    for i in fastener_details_list:
        zi = float(i["coord_z"])
        zi_listfloat.append(zi)

    zi_array = np.array(zi_listfloat)

    """Multiply the area by each coordinate"""
    #get area times xi for each fastener
    Axi_array = xi_array * A_array

    #get area times xi for each fastener
    Azi_array = zi_array * A_array

    """Sum the values of each Axi, Azi and A"""
    #sum all values Axi
    Axi_sum = sum(Axi_array)

    #sum all values Azi and sum of all areas
    Azi_sum = sum(Azi_array)


    A_sum = sum(A_array)


    """Calculate cg location"""
    #get xcg value
    xcg = Axi_sum/A_sum
    print(xcg)

    #get zcg value
    zcg = Azi_sum/A_sum
    print(zcg)

    return (xcg, zcg)

TESTING_fasteners_list = [{"coord_x": 0, "coord_z": 0, "diameter": 0.02}, {"coord_x": 1, "coord_z": 1, "diameter": 0.03}, {"coord_x": 2, "coord_z": 2, "diameter": 0.04}]
print(CG_calculator(TESTING_fasteners_list))