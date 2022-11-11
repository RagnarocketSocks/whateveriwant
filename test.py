import numpy as np


Y_mag = ([1, 2, 3, 4, 5],[1,2,3,4,5],[1,2,3,4,5])
Y_phase = ([1, 2, 3, 4, 5],[1,2,3,4,5],[1,2,3,4,5])
V_mag = [1, 2, 3, 4, 5]
V_phase = [1,2,3,4,5]



def J_10_diff(k,n):
    J1 = V_mag[2]*Y_mag[1:2]*V_mag[3]*np.sin(V_phase[2]-V_phase[3]-Y_phase[1:2])
    return J_10

def J_1_diff(k,n):
    J1 = V_mag[k]*Y_mag[k-1:n-1]*V_mag[n]*np.sin(V_phase[k]-V_phase[n]-Y_phase[k-1:n-1])
    return J_1


J = J_1_diff(2,3) #k,n
J1 = J_10_diff(2,3)

# J_1_diff(P[0],V_phase[3],k,n) k=2 n=3





# def J_1_same(k,n):
#     A_j1 = 0

#     for i in range(1,5):
#         for j in range(1,5):
#             A_j1 += Y_mag[i:j]*V_mag[j]*np.sin(V_phase[i]-V_phase[j]-Y_phase[i:j])
#             time.sleep(3)
#     J1 = -1*V_mag[k]*A_j1
#     return J_1



# J = J_1_same(1,1)

print(J)
print(J_10)