import time
import numpy as np
import cmath

# Gauss Seidel Iteration


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
PQ_1 = 1
PQ_2 = 0.5-0.2*1j
PQ_3 = -1+0.5*1j
PQ_4 = 0.3-0.1*1j

# Starting Voltages
V1_0 = 1.04
V2_0 = 1
V3_0 = 1
V4_0 = 1

# Start Counter
count = 1

Y_bus = np.array([[Y11, Y12, Y13, Y14],[Y21, Y22, Y23, Y24],[Y31, Y32, Y33, Y34],[Y41, Y42, Y43, Y44]])
V_bus = np.array([V1_0, V2_0, V3_0, V4_0])
V_bus_old = np.array([0, 0, 0, 0])
PQ_bus = np.array([PQ_1,PQ_2, PQ_3, PQ_4])

e = float(input('Enter tolerable error: '))


def multiplys(v,y_bus):
    return np.matmul(v,y_bus).round(8)

def multi_comp(v,I):
    S = v*I
    return S.round(8)

def RecttoPolar(V):
    return cmath.polar(V)


counter = 0
condition=True

while condition:
 
    I1_1 = multiplys(V_bus,Y_bus[0])
    I2_1 = multiplys(V_bus,Y_bus[1])
    I3_1 = multiplys(V_bus,Y_bus[2])
    I4_1 = multiplys(V_bus,Y_bus[3])
    

    PQ_1_calc = multi_comp(V_bus[0],np.conj(I1_1))
    PQ_2_calc = multi_comp(V_bus[1],np.conj(I2_1))
    PQ_3_calc = multi_comp(V_bus[2],np.conj(I3_1))
    PQ_4_calc = multi_comp(V_bus[3],np.conj(I4_1))


    d_y1 = abs(V_bus[0]-V_bus_old[0])
    d_y2 = abs(V_bus[1]-V_bus_old[1])
    d_y3 = abs(V_bus[2]-V_bus_old[2])
    d_y4 = abs(V_bus[3]-V_bus_old[3])
   
    

    condition = (d_y1>e) and (d_y2>e) and (d_y3>e) and (d_y4>e)
      
    V1_new = V1_0
    V2_new = ((1/Y22)*((PQ_2_calc/(np.conj(V_bus[1])))-(Y21*V_bus[0]+Y23*V_bus[2]+Y24*V_bus[3]))).round(2)
    V3_new = ((1/Y33)*((PQ_3_calc/(np.conj(V_bus[2])))-(Y31*V_bus[0]+Y32*V_bus[1]+Y34*V_bus[3]))).round(2)
    V4_new = ((1/Y44)*((PQ_4_calc/(np.conj(V_bus[3])))-(Y41*V_bus[0]+Y42*V_bus[1]+Y43*V_bus[2]))).round(2)
    
    V_bus_old = V_bus
   
    V_bus = []

    V_bus.append(V1_new)
    V_bus.append(V2_new)
    V_bus.append(V3_new)
    V_bus.append(V4_new)

    count +=1



V_bus_new = []
for i in range(4):
    V_bus_new.append(RecttoPolar(V_bus[i]))
    

print(f'\nSolution: V1={V_bus_new[0]}, V2={V_bus_new[1]}, V3={V_bus_new[2]}, and V4={V_bus_new[3]}\n' )

# =====================
