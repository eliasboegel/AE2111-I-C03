from math import pi
# F_tot is the total applied force to the fastener pattern 
# centre of gravity to the F_tot original location
# x_n is the fastener number (i.e fastener 2 -> x_n=2)

# Input for radial distance for fastener cg to ith fastener
# d is the distance between the attachment point and the fastener cg

def get_pull_through(dim,mat,loads,distances):
  Fy = loads["Fy"] # from other file
  Mx = loads["Mx"] # from other file
  rho_out = distances[1]
  rho_in = distances[0]

  n_f_total = 8
  F_pi = Fy/n_f_total

  diameter_hole = dim["d2"] #mm
  radius_hole = diameter_hole /2
  Ai= pi * radius_hole**2 #area of the fastener cross section

  #find sum of inner fasteners: Ai * ri^2
  n_f_in = 4 #n_f_in is the number of inner fasteners
  rho_in = int(rho_in) #radial distance to the fastener cg of the inner fasteners
  Sum_Ai_rho2_in = 0
  #Arho2_in = Ai * rho_in**2  might not be necessary
  for k in range(n_f_in):
    Sum_Ai_rho2_in = Sum_Ai_rho2_in + Ai * rho_in**2

  #find sum of the outer fasteners: Ai * ri^2
  n_f_out = 4 #n_f_out is the number of outer fasteners
  #rho_out = int(rho_out) #radial distance to the fastener cg of the inner fasteners
  Sum_Ai_rho2_out = 0
  # Arho2_out = Ai * rho_out**2  might not be necessary
  for h in range(n_f_out):
    Sum_Ai_rho2_out = Sum_Ai_rho2_out + Ai * rho_out**2


  #find total sum of the fasteners
  totSum_Ai_rho2 = Sum_Ai_rho2_out + Sum_Ai_rho2_in


  # Fp_Mx for outer lower fasteners
  A = Mx * Ai * rho_out
  B = totSum_Ai_rho2
  Fp_Mx_outerlower = (A/B)
  F_pullthrough_outerlower = Fp_Mx_outerlower + F_pi
  #print('pull-through load of the outer lower fasteners =', F_pullthrough_outerlower)


  # Fp_Mx for inner lower fasteners
  C = Mx * Ai * rho_in
  D = totSum_Ai_rho2
  Fp_Mx_innerlower = (C/D)
  F_pullthrough_innerlower = Fp_Mx_innerlower + F_pi
  #print('pull-through load of the inner lower fasteners =', F_pullthrough_innerlower)


  # Fp_Mx for outer upper fasteners
  A = -Mx * Ai * rho_out
  B = totSum_Ai_rho2
  Fp_Mx_outerupper = (A/B)
  F_pullthrough_outerupper = Fp_Mx_outerupper + F_pi
  #print('pull-through load of the outer upper fasteners =', F_pullthrough_outerupper)


  # Fp_Mx for inner upper fasteners
  C = -Mx * Ai * rho_in
  D = totSum_Ai_rho2
  Fp_Mx_innerupper = (C/D)
  F_pullthrough_innerupper = Fp_Mx_innerupper + F_pi
  #print('pull-through load of the inner upper fasteners =',F_pullthrough_innerupper)

  return max(F_pullthrough_outerlower, F_pullthrough_innerlower, F_pullthrough_outerupper, F_pullthrough_innerupper)

