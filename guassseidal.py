
import numpy as np


# Gauss Seidel Iteration

# Defining equations to be solved
# in diagonally dominant form


# Admittance Matrix 
Y11 = 3-9*1j
Y12 = -2+6*1j
Y13 = -1+3*1j
Y14 = 0
Y21 = Y12
Y22 = 3.666-11*1j
Y23 = -0.666+2*1j
Y24 = -1+3*1j
Y31 = Y13
Y32 = Y23
Y33 = 3.666-11*1j
Y34 = -2+6*1j
Y41 = Y14
Y42 = Y24
Y43 = Y34
Y44 = 3-9*1j


# Bus Apparent Power
# S_1 = doesnt matter
S_2 = 0.5-0.2*1j
S_3 = -1+0.5*1j
S_4 = 0.3-0.1*1j

# Starting Voltages
V1_0 = 1.04
V2_0 = 1
V3_0 = 1
V4_0 = 1

# Start Counter
count = 1

Y_bus = np.array([[Y11, Y12, Y13, Y14],[Y21, Y22, Y23, Y24],[Y31, Y32, Y33, Y34],[Y41, Y42, Y43, Y44]])
V_bus = np.array([V1_0, V2_0, V3_0, V4_0])
S_bus = np.array([S_2, S_3, S_4])
# I_bus = np.matmul(Y_bus,V_bus)

# e = float(input('Enter tolerable error: '))




# print(np.matmul(Y_bus[0],V_bus))

def multiplys(v,y_bus):
    return np.matmul(v,y_bus)

def multi_comp(v,I):
    S = v*I
    return S

while True:
    I1_1 = multiplys(V_bus,Y_bus[0])
    I2_1 = multiplys(V_bus,Y_bus[1])
    I3_1 = multiplys(V_bus,Y_bus[2])
    I4_1 = multiplys(V_bus,Y_bus[3])
    

    S_1_calc = multi_comp(V_bus[0],I1_1)
    S_2_calc = multi_comp(V_bus[1],I2_1)
    S_3_calc = multi_comp(V_bus[2],I3_1)
    S_4_calc = multi_comp(V_bus[3],I4_1)


    d_y2 = abs(S_2-S_2_calc)
    d_y3 = abs(S_3-S_3_calc)
    d_y4 = abs(S_4-S_4_calc)

    count +=1
    





# # def multiplys(v,y_bus):
# #     return np.matmul(y_bus,v)

# # while True:
# #      V1_1 = multiplys(V_bus,Y_bus[0:])
#      V2_1 = multiplys(V_bus,Y_bus[1:])
#      V3_1 = multiplys(V_bus,Y_bus[2:])
#      V4_1 = multiplys(V_bus,Y_bus[3:])

#     #  print(f"================================= \n\n {V1_1}\n\n=====================================")
     
#     #  print('%d\t%0.4f\t%0.4f\t%0.4f\t%0.4f\n' %(count, V1_1,V2_1,V3_1,V4_1))

#      e1 = abs(V_bus[0]-V1_1)
#      e2 = abs(V_bus[1]-V2_1)
#      e3 = abs(V_bus[2]-V3_1)
#      e4 = abs(V_bus[3]-V4_1)
    
#      count += 1
#      V_bus[0] = V1_1
#      V_bus[1] = V2_1
#      V_bus[2] = V3_1
#      V_bus[3] = V4_1

#      condition = e1>e and e2>e and e3>e and e4>e

# print('\nSolution: V1=%0.3f, V2=%0.3f, V3=%0.3f, and V4=%0.3f\n'% (V_bus[0],V_bus[1],V_bus[2],V_bus[3]))