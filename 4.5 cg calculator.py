import numpy as np

#cg calculator
#Constants
pi = 3.14

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
for i in range(len(d_list)):  #goes through every item in list
    r_fastener = d_list[i]/2
    A_fastener = pi*(r_fastener**2)   #until here correct
    A_list.append(A_fastener)

A_array = np.array(A_list)

"""Convert coordinates to float numbers"""
#convert xi_list to float and put in array
xi_listfloat = []
for i in range(len(xi_list)):
    xi = float(xi_list[i])
    xi_listfloat.append(xi)

xi_array = np.array(xi_listfloat)

#convert zi_list to float and put in array
zi_listfloat = []
for i in range(len(zi_list)):
    zi = float(zi_list[i])
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

"""until here correct"""

