import numpy as np
from math import pi

#cg calculator
#Constants

#def calculate_cg():    
#input the fastener details
d_list = [1,2,1,4,6,4]
xi_list = [0,2,4,5,0,2]
zi_list = [0,2,2,4,1,3]

#detailslist = [2, 4, 6, 2]
#detials_fastener = input(detailslist)

"""Calculate area of each fastener"""
#get area for each fastener this is now correct
A_list = []
for i in d_list:  #goes through every item in list 
    r_fastener = i/2 #Changed this slightly. You can do this instead of range(len(d_list)) etc
    A_fastener = pi*(r_fastener**2)   #until here correct
    A_list.append(A_fastener)

A_array = np.array(A_list)

"""Convert coordinates to float numbers"""
#convert xi_list to float and put in array
xi_listfloat = []
for i in xi_list:
    xi = float(i) # Made similar change here
    xi_listfloat.append(xi)

xi_array = np.array(xi_listfloat)

#convert zi_list to float and put in array
zi_listfloat = []
for i in zi_list:
    zi = float(i)
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

"""until here correct""" # Looks correct and makes sense to me -Kristian

"""Bearing stress calculator"""

""" Constants and inputs"""
D2 = 2
t2 = 1
F_inplane_x = 20
F_inplane_z = 10
F_inplane_my = 10
stress_allowable = 20

""" Vectorize the forces [x,y,z]"""
F_inx = np.array([F_inplane_x , 0, 0])
F_inmy = np.array([0, F_inplane_my, 0])
F_inz = np.array([0, 0, F_inplane_z])


""" Calculate Pi"""
Pi = F_inx + F_inz + F_inmy
print(Pi)

Pix = Pi[0]
Piy = Pi[1]
Piz = Pi[2]
print(Pix, Piy, Piz)
#find magnitude of Pi and the bearing stress
Pi = (Pix**2+Piy**2+Piz**2)**(1/2)
B_stress = Pi/(D2*t2)


print("The bearing stress is:", B_stress, "\nThe max allowable stress is:", stress_allowable, "\n")
 #Check if bearing stress does not exceed allowable stress
if B_stress < stress_allowable:
    print("No failure due to bearing stress\nTry to save weight by reducing t2 or removing fasteners")

elif B_stress == stress_allowable:
    print("Bearing stress is equal to allowable stress")

elif B_stress > stress_allowable:
    print("Failure occurs due to bearing stress please change one of the following geometries:")
    print("D2\nt2\nnumber of fasteners, note w might change due to this")

else:
    print("Failed to compute")


# from math import sin, cos, atan2


# def read_excel(): #Working on this one -Saviër


# For this function, I would like the forces F_x and F_z to have coordinates that I can use
# CG should be coordinates as (x, z)
def calculate_equivalent_FM(forces_and_moments_dictionary, CG_coordinates): # Working on this one -Kristian
    #The forces in the x- and z-directions will just be the forces
    return { "F_cgx": forces_and_moments_dictionary["F_x"], "F_cgz": forces_and_moments_dictionary["F_z"], "M_cgy": forces_and_moments_dictionary["F_x"] * (forces_and_moments_dictionary["coord_z"] - CG_coordinates(1))  - forces_and_moments_dictionary["F_z"] * (forces_and_moments_dictionary["coord_x"] - CG_coordinates(0))}


def in_plane_force(cg_forces_and_moments_dictionary, number_of_fasteners): # Working on this one -Kristian
    return { "F_in_plane_x": cg_forces_and_moments_dictionary["F_x"] / number_of_fasteners, "F_in_plane_z": cg_forces_and_moments_dictionary["F_z"] / number_of_fasteners}


# def in_plane_moment(M_cgy, all_fastener_details_list, CG_coordinates, current_fastener_number): # Working on this one -Kristian
#     fastener_radius = ((all_fastener_details_list[current_fastener_number]["coord_x"] - CG_coordinates[0]) ** 2 + (fastener_details_dictionary["coord_z"] - CG_coordinates[1]) ** 2) ** 0.5


