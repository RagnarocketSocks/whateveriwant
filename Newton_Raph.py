import time
import numpy as np
import cmath


# Newton Raphson Method

# Admittance 
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

Y_bus = np.array([[Y11, Y12, Y13, Y14],[Y21, Y22, Y23, Y24],[Y31, Y32, Y33, Y34],[Y41, Y42, Y43, Y44]])



# Admittance Mag and Angle 
def RecttoPolar(Y):
    return cmath.polar(Y)

#Y_mag = 
Y_mag= []
Y_phase = []


for i in range(4):
    for j in range(4):
        x,y = RecttoPolar(Y_bus[i][j])
        Y_mag.append(x)
        Y_phase.append(((180/np.pi)*y))
    






# Slack Bus
V_1 = 1.04 + 0.0*1j
d_1 = 0.0
#P_1 = ????
#Q_1 = ????

# Bus 2  
V_2 =  1.0 + 0.0*1j# Flat Start
d_2 = 0.0 
S_2 = 0.5 -0.2*1j

P_2 = 0.5 
Q_2 = -0.2

# Bus 3 
V_3 = 1.0 + 0.0*1j
d_3 = 0.0
S_3 = -1.0 + 0.5*1j

P_3 = -1.0
Q_3 = 0.5

# Bus 4
V_4 = 1.0 + 0.0*1j
d_4 = 0.0
S_4 = 0.3 - 0.1*1j

P_4 = 0.3
Q_4 = -0.1



V_bus = [V_1,V_2,V_3,V_4]
S_bus = [S_2,S_3,S_4]


# Output Vector 
y = [P_2,Q_2,P_3,Q_3,P_4,Q_4]

# Vector of Unknown Quantities to be solved for
x = [V_2, d_2, V_3, d_3, V_4, d_4]


# Voltage Magnitude and Phase 
V_mag= []
V_phase = []

# Real and Reactive Power
P = []
Q = []

for i in range(4):
    x,y = RecttoPolar(V_bus[i])
    V_mag.append(x)
    V_phase.append(((180/np.pi)*y))


for i in range(3):
    x,y = RecttoPolar(S_bus[i])
    P.append(x)
    Q.append(y)



#e = float(input('Enter tolerable error: '))
e = 0.0001
def concat(a, b):
    return eval(f"{a}{b}")


def multiplys(v,y_bus):
    return np.matmul(v,y_bus).round(8)

def multi_comp(v,I):
    S = v*I
    return S.round(8)


condition=True


########################### Functions for creating Jacobian Matrix ###################################
def J_1_diff(k,n):
    J1 = V_mag[2]*Y_mag[23]*V_mag[3]*np.sin(V_phase[2]-V_phase[3]-Y_phase[23])
    return J_1


J_1_diff(P[0],V_phase[2],k,n),J_1_diff(P[0],V_phase[3],k,n) k=2 n=3




def J_1_same(P,V_phase,k,n):
    if k > n:
        for i in range(1, 5):
            A_j1 += Sum(Y_mag[kn]*V_mag[n]*np.sin(V_phase[k]-V_phase[n]-Y_phase[kn]))
            J1 = -1*V[k]*sum(A_j1)
    else if k < n:
    return J_1




def J_2_diff(P,V,k,n):
    J2[k,n] = V[k]*Y[k,n]*np.cos(V_phase[k]-V_phase[n]-Y_phase[k,n])
    return J_2

def J_2_same(P,V,k,n):
    A_j2 = Sum(Y[k,n]*V[n]*np.cos(V_phase[k]-V_phase[n]-Y_phase[k,n])) from n=1 to N
    J2[k,k] = V[k]*Y[k,k]*np.cos(Y_phase[k,k])+ sum(A_j2)
    return J_2






def J_3_diff(Q,V_phase,k,n):
    J3[k,n] = -1*V[k]*Y[k,n]*V[n]*np.cos(V_phase[k]-V_phase[n]-Y_phase[k,n])
    return J_3

def J_3_same(Q,V_phase,k,n):
    A_j3 = Sum(Y[k,n]*V[n]*np.cos(V_phase[k]-V_phase[n]-Y_phase[k,n])) from n=1 to N, n!=k
    J3[k,k] = V[k]*sum(A_j3)
    return J_3





def J_4_diff(Q,V,k,n):
    J4[k,n] = V[k]*Y[k,n]*np.sin(V_phase[k]-V_phase[n]-Y_phase[k,n])
    return J_4

def J_4_same(Q,V,k,n):
    A_j4 = Sum(Y[k,n]*V[n]*np.sin(V_phase[k]-V_phase[n]-Y_phase[k,n])) from n=1 to N
    J4[k,k] = -1*V[k]*Y[k,k]*np.sin(Y_phase[k,k])+sum() 
    return J_4


##########################################################################################################


#### Iteration ####

while condition:
    
    
    I1_1 = multiplys(V_bus,Y_bus[0])
    I2_1 = multiplys(V_bus,Y_bus[1])
    I3_1 = multiplys(V_bus,Y_bus[2])
    I4_1 = multiplys(V_bus,Y_bus[3])
    

    S_1_calc = multi_comp(V_bus[0],np.conj(I1_1))
    S_2_calc = multi_comp(V_bus[1],np.conj(I2_1))
    S_3_calc = multi_comp(V_bus[2],np.conj(I3_1))
    S_4_calc = multi_comp(V_bus[3],np.conj(I4_1))

    S_bus_calc = [S_2_calc,S_3_calc,S_4_calc]
    P_calc = []
    Q_calc =[]

    for i in range(3):
    x,y = RecttoPolar(S_bus_calc[i])
    P_calc.append(x)
    Q_calc.append(y)


    d_y2 = abs(P[0]-P_calc[0])
    d_y3 = abs(P[1]-P_calc[1])
    d_y4 = abs(P[2]-P_calc[2])
   
    

    condition = (d_y2>e) and (d_y3>e) and (d_y4>e)



    Jacobian_Matrix = ([J_1_same(P[0],V_phase[1],2,2),J_1_diff(P[0],V_phase[2],k,n),J_1_diff(P[0],V_phase[3],k,n),J_2_same(P[0],V_mag[1],2,2),J_2_diff(P[0],V_mag[2],k,n),J_2_diff(P[0],V_mag[3],k,n)],..
    [J_1_diff(P[1],V_phase[1],k,n),J_1_same(P[1],V_phase[2],3,3),J_1_diff(P[1],V_phase[3],k,n),J_2_diff(P[1],V_mag[1],k,n),J_2_same(P[1],V_mag[2]3,3),J_2_diff(P[1],V_mag[3],k,n)],..
    [J_1_diff(P[2],V_phase[1],k,n),J_1_diff(P[2],V_phase[2],k,n),J_1_same(P[2],V_phase[3],4,4),J_2_diff(P[2],V_mag[1],k,n),J_2_diff(P[2],V_mag[2],k,n),J_2_same(P[2],V_mag[3],4,4)],..
    [J_3_same(Q[0],V_phase[1],2,2),J_3_diff(Q[0],V_phase[2],k,n),J_3_diff(Q[0],V_phase[3],k,n),J_4_same(Q[0],V_mag[1],2,2),J_4_diff(Q[0],V_mag[2],k,n),J_4_diff(Q[0],V_mag[3],k,n)],..
    [J_3_diff(Q[1],V_phase[1],k,n),J_3_same(Q[1],V_phase[2],3,3),J_3_diff(Q[1],V_phase[3],k,n),J_4_diff(Q[1],V_mag[1],k,n),J_4_same(Q[1],V_mag[2],3,3),J_4_diff(Q[1],V_mag[3],k,n)],..
    [J_3_diff(Q[2],V_phase[1],k,n),J_3_diff(Q[2],V_phase[2],k,n),J_3_same(Q[2],V_phase[3],4,4),J_4_diff(Q[2],V_mag[1],k,n),J_4_diff(Q[2],V_mag[2],k,n),J_4_same(Q[2],V_mag[3],4,4)])
    































    #print(condition)
    #print(e)
   
    V1_new = V_1
    V2_new = ((1/Y22)*((PQ_2_calc/(np.conj(V_bus[1])))-(Y21*V_bus[0]+Y23*V_bus[2]+Y24*V_bus[3]))).round(2)
    V3_new = ((1/Y33)*((PQ_3_calc/(np.conj(V_bus[2])))-(Y31*V_bus[0]+Y32*V_bus[1]+Y34*V_bus[3]))).round(2)
    V4_new = ((1/Y44)*((PQ_4_calc/(np.conj(V_bus[3])))-(Y41*V_bus[0]+Y42*V_bus[1]+Y43*V_bus[2]))).round(2)
    


    V_bus_old = V_bus
   
    V_bus = []

    V_bus.append(V1_new)
    V_bus.append(V2_new)
    V_bus.append(V3_new)
    V_bus.append(V4_new)


    # print("v bus\t",V_bus)
    # print("dy2\t\n",d_y2)
    # print("dy3\t\n",d_y3)
    # print("dy4\t\n",d_y4)
    
    
    
    
    count +=1

















# # # Jacobian Matrix Formulas
# # # n != k
# # J1[kn] = V[k]*Y[kn]*V[n]*np.sin(V_phase[k]-V_phase[n]-Y_phase[kn])

# # J2[kn] = V[k]*Y[kn]*np.cos(V_phase[k]-V_phase[n]-Y_phase[kn])

# # J3[kn] = -1*V[k]*Y[kn]*V[n]*np.cos(V_phase[k]-V_phase[n]-Y_phase[kn])

# # J4[kn] = V[k]*Y[kn]*np.sin(V_phase[k]-V_phase[n]-Y_phase[kn])

# # # n = k
# # A_j1 = Sum(Y[kn]*V[n]*np.sin(V_phase[k]-V_phase[n]-Y_phase[kn])) from n=1 to N, n!=k
# # J1[kk] = -1*V[k]*sum(A_j1)

# # A_j2 = Sum(Y[kn]*V[n]*np.cos(V_phase[k]-V_phase[n]-Y_phase[kn])) from n=1 to N
# # J2[kk] = V[k]*Y[kk]*np.cos(Y_phase[kk])+ sum(A_j2)

# # A_j3 = Sum(Y[kn]*V[n]*np.cos(V_phase[k]-V_phase[n]-Y_phase[kn])) from n=1 to N, n!=k
# # J3[kk] = V[k]*sum(A_j3)

# A_j4 = Sum(Y[kn]*V[n]*np.sin(V_phase[k]-V_phase[n]-Y_phase[kn])) from n=1 to N
# J4[kk] = -1*V[k]*Y[kk]*np.sin(Y_phase[kk])+sum() 
