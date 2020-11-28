from math import pi
import task48_9 as ddd


def get_MS(dim, mat, loads, distances):
    # calculating the normal stress
    D_fi = dim["d2"]  # inner diameter in m
    if D_fi < 0.005:
        D_fo = 0.007
    else:
        D_fo = 1.75 * D_fi

    r_fo = D_fo / 2
    r_fi = D_fi / 2

    F_y = ddd.get_pull_through(dim, mat, loads, distances)
    # F_y = 4  # pull-through load, newtons

    A_head_ap = pi * (r_fo ** 2 - r_fi ** 2)  # area of the fastener head on the attached parts
    if not A_head_ap > 0:
        return -1

    stress_N = F_y / A_head_ap

    # print(stress_N)

    # calculating shear stress for t1
    t1 = dim["t1"]  # m thickness of the spacecraft wall calculated in WP3
    A_t1_ap = pi * t1 * D_fi  # area of the attached parts of t1
    stress_t1_V = F_y / A_t1_ap

    # print('shear stress in t1 = ', stress_t1_V)

    # calculating shear stress for t2
    t2 = dim["t2"]  # m this value is calculated earlier
    A_t2_ap = pi * t2 * D_fi  # area of the attached parts of t2
    stress_t2_V = F_y / A_t2_ap

    # print('shear stress in t2 = ', stress_t2_V)

    # calculating shear stress for t3
    t3 = 0.004  # m calculated earlier in the report WP4
    A_t3_ap = pi * t3 * D_fi  # area of the attached parts of t3
    stress_t3_V = F_y / A_t3_ap

    # print('shear stress in t3 = ', stress_t3_V)

    # total shear stress

    # stress_v_tot = stress_t1_V + stress_t2_V + stress_t3_V

    # print('total shear stress = ', stress_V_tot)

    # Comparison to yield stress, failure if <1
    tau_yield = mat["sigma_y"]
    ratio1 = tau_yield / abs(stress_t1_V)
    ratio2 = tau_yield / abs(stress_t2_V)
    ratio3 = tau_yield / abs(stress_t3_V)
    # ratio0 = tau_yield / stress_v_tot

    # print(ratio1,ratio2,ratio3, ratio0)
    MS = min(ratio1, ratio2, ratio3) - 1

    """
  if ratio1 >=1:
    print("SAFE")
  else:
        print("FAIL")

  if ratio2 >=1:
    print("SAFE")
  else:
        print("FAIL")

  if ratio3 >=1:
    print("SAFE")
  else:
        print("FAIL")

  """

    # if ratio0 >=1:
    # print("SAFE")
    # else:
    # print("FAIL")
    return MS
