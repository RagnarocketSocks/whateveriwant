
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
PQ_bus = np.array([PQ_2, PQ_3, PQ_4])
# I_bus = np.matmul(Y_bus,V_bus)

# e = float(input('Enter tolerable error: '))
e = 0.0001




# print(np.matmul(Y_bus[0],V_bus))

def multiplys(v,y_bus):
    return np.matmul(v,y_bus)

def multi_comp(v,I):
    S = v*I
    return S

condition=True
new_bus_v = []
for_loop_array = [1]
for i in a:
    
    
    I1_1 = multiplys(V_bus[i],Y_bus[0])
    I2_1 = multiplys(V_bus[i],Y_bus[1])
    I3_1 = multiplys(V_bus[i],Y_bus[2])
    I4_1 = multiplys(V_bus[i],Y_bus[3])
    

    PQ_1_calc = multi_comp(V_bus[i],np.conj(I1_1))
    PQ_2_calc = multi_comp(V_bus[i],np.conj(I2_1))
    PQ_3_calc = multi_comp(V_bus[i],np.conj(I3_1))
    PQ_4_calc = multi_comp(V_bus[i],np.conj(I4_1))


    d_y2 = abs(PQ_2-PQ_2_calc)
    d_y3 = abs(PQ_3-PQ_3_calc)
    d_y4 = abs(PQ_4-PQ_4_calc)
    
    count +=1

    condition = d_y2>e and d_y3>e and d_y4>e


    #print(condition)
   
    
    V2_new = (1/Y22)*((PQ_2_calc/(np.conj(V_bus[1])))-Y21*V_bus[0]+Y23*V_bus[2]+Y24*V_bus[3])
    V3_new = (1/Y33)*((PQ_3_calc/(np.conj(V_bus[2])))-Y31*V_bus[0]+Y32*V_bus[1]+Y34*V_bus[3])
    V4_new = (1/Y44)*((PQ_4_calc/(np.conj(V_bus[3])))-Y41*V_bus[0]+Y42*V_bus[1]+Y43*V_bus[2])
    #print(V2_new.round(8))

    # V2_new.append(new_bus_v)
    new_bus_v = []
    new_bus_v.append(V2_new.round(2))
    print(new_bus_v)
    
    


    # V_bus[1]==V2_new
    # print(f"\nV_bus[1] \t {V_bus[1]}\t ======= \t {V2_new} \n")
    # V_bus[2] = V3_new
    # V_bus[3] = V4_new

    


    
print('\nSolution: V1=%0.3f, V2=%0.3f, V3=%0.3f, and V4=%0.3f\n'% (V_bus[0],V_bus[1],V_bus[2],V_bus[3]))

#=====================