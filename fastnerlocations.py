from dimensions import *

""" Fastener coordinates"""
e1 = 1.5*D2_fromcg
e2 = 1.5*D2_fromcg

#take bottom right as 0 point
#fasteners x z coordinates on righthandside of the lug
fastcordx_1 = e2
fastcordz_1 = e1

fastcordx_2 = e2
fastcordz_2 = w-e1

fastcordx_3 = w-e2
fastcordz_3 = e1

fastcordx_4 = w-e2
fastcordz_4 = w-e1

#fasteners x z location on left handside of the lug
fastcordx_5 = w+h+t1+t1+e2
fastcordz_5 = e1

fastcordx_6 = w+h+t1+t1+e2
fastcordz_6 = w-e1

fastcordx_7 = w+h+t1+t1+w-e2
fastcordz_7 = e1

fastcordx_8 = w+h+t1+t1+w-e2
fastcordz_8 = w-e1

