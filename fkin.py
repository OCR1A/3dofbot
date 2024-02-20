import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Eslabones
a1 = 1
a2 = 1
a3 = 1
a4 = 1

#Ángulos en grados
T1G = 45
T2G = 45
T3G = 45

#Ángulos en radianes
T1 = np.radians(T1G)
T2 = np.radians(T2G)
T3 = np.radians(T3G)

#Matrices de rotación
r0_1 =  np.array([
                    [0,0,1],
                    [1,0,0],
                    [0,1,0]
])

R0_1 = np.array([
                    [np.cos(T1), -np.sin(T1), 0],
                    [np.sin(T1), np.cos(T1), 0],
                    [0, 0, 1]
])

R1_2 = np.array([
                    [np.cos(T2), -np.sin(T2), 0],
                    [np.sin(T2), np.cos(T2), 0],
                    [0, 0, 1]
])

R2_3 = np.array([
                    [np.cos(T3), -np.sin(T3), 0],
                    [np.sin(T3), np.cos(T3), 0],
                    [0, 0, 1]
])

R0_1 = np.dot(R0_1, r0_1)

#Vectores de posición
P0_1 = np.array([
                [a2*np.cos(T1)],
                [a2*np.sin(T1)],
                [a1]
])

P1_2 = np.array([
                [a3*np.cos(T2)],
                [a3*np.sin(T2)],
                [0]
])

P2_3 = np.array([
                [a4*np.cos(T3)],
                [a4*np.sin(T3)],
                [0]
])

#Matrices de transformación homogenea
T0_1 = np.concatenate((R0_1, P0_1), 1)
T0_1 = np.concatenate((T0_1, [[0,0,0,1]]), 0)
T1_2 = np.concatenate((R1_2, P1_2), 1)
T1_2 = np.concatenate((T1_2, [[0,0,0,1]]), 0)
T2_3 = np.concatenate((R2_3, P2_3), 1)
T2_3 = np.concatenate((T2_3, [[0,0,0,1]]), 0)

T0_2 = np.dot(T0_1, T1_2)
T0_3 = np.dot(T0_2, T2_3)

epsilon = 1*(10**-10)
T0_3 = np.where(np.abs(T0_3)<epsilon, 0, T0_3)

#Cinemática directa calculada a mano
a11 = -np.sin(T1)*np.cos(T2)*np.cos(T3)+np.sin(T1)*np.sin(T2)*np.sin(T3)
a12 = np.sin(T1)*np.cos(T2)*np.sin(T3)+np.sin(T1)*np.sin(T2)*np.cos(T3)
a13 = np.cos(T1)
a14 = -a4*np.sin(T1)*np.cos(T2)*np.cos(T3)+a4*np.sin(T1)*np.sin(T2)*np.sin(T3)+a2*np.cos(T1)-a3*np.sin(T1)*np.cos(T2)
a21 = np.cos(T1)*np.cos(T2)*np.cos(T3)-np.cos(T1)*np.sin(T2)*np.sin(T3)
a22 = -np.cos(T1)*np.cos(T2)*np.sin(T3)-np.cos(T1)*np.sin(T2)*np.cos(T3)
a23 = np.sin(T1)
a24 = a4*np.cos(T1)*np.cos(T2)*np.cos(T3)-a4*np.cos(T1)*np.sin(T2)*np.sin(T3)+a3*np.cos(T1)*np.cos(T2)+a2*np.sin(T1)
a31 = np.sin(T2)*np.cos(T3)+np.cos(T2)*np.sin(T3)
a32 = -np.sin(T2)*np.sin(T3)+np.cos(T2)*np.cos(T3)
a33 = 0
a34 = a4*np.sin(T2)*np.cos(T3)+a4*np.cos(T2)*np.sin(T3)+a3*np.sin(T2)+a1
a41 = 0
a42 = 0
a43 = 0
a44 = 1

T0_3C = np.array([
                    [a11, a12, a13, a14],
                    [a21, a22, a23, a24],
                    [a31, a32, a33, a34],
                    [a41, a42, a43, a44]
])

print("Cinemática directa computada:")
print(T0_3)
print("Cinemática directa a mano:")
print(T0_3C)