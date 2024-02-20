import numpy as np
import matplotlib.pyplot as plt

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
R0_A1 = np.array([  
                    [1,0,0],
                    [0,1,0],
                    [0,0,1]
])

rA1_1 =  np.array([
                    [0,0,1],
                    [1,0,0],
                    [0,1,0]
])

RA1_1 = np.array([
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

RA1_1 = np.dot(RA1_1, rA1_1)

#Vectores de posición
P0_A1 = np.array([
                    [0],
                    [0],
                    [a1]
])

PA1_1 = np.array([
                [a2*np.cos(T1)],
                [a2*np.sin(T1)],
                [0]
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
T0_A1 = np.concatenate((R0_A1, P0_A1), 1)
T0_A1 = np.concatenate((T0_A1, [[0,0,0,1]]), 0)
TA1_1 = np.concatenate((RA1_1, PA1_1), 1)
TA1_1 = np.concatenate((TA1_1, [[0,0,0,1]]), 0)
T1_2 = np.concatenate((R1_2, P1_2), 1)
T1_2 = np.concatenate((T1_2, [[0,0,0,1]]), 0)
T2_3 = np.concatenate((R2_3, P2_3), 1)
T2_3 = np.concatenate((T2_3, [[0,0,0,1]]), 0)

T0_1 = np.dot(T0_A1, TA1_1)
T0_2 = np.dot(T0_1, T1_2)
T0_3 = np.dot(T0_2, T2_3)

#Cinemática directa
print(T0_3)

#Coordenadas para eslabones
x_link1 = [0, T0_A1[0, 3], T0_1[0, 3]]
y_link1 = [0, T0_A1[1, 3], T0_1[1, 3]]
z_link1 = [0, T0_A1[2, 3], T0_1[2, 3]]

x_link2 = [T0_1[0, 3], T0_2[0, 3]]
y_link2 = [T0_1[1, 3], T0_2[1, 3]]
z_link2 = [T0_1[2, 3], T0_2[2, 3]]

x_link3 = [T0_2[0, 3], T0_3[0, 3]]
y_link3 = [T0_2[1, 3], T0_3[1, 3]]
z_link3 = [T0_2[2, 3], T0_3[2, 3]]

#Graficar
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#Grafica cada eslabón con parámetros especiales para cada uno
ax.plot(0, 0, 0, marker='o', color='r')
ax.plot(x_link1, y_link1, z_link1, marker='', color='r')
ax.plot(x_link2, y_link2, z_link2, marker='o', color='g')
ax.plot(x_link3, y_link3, z_link3, marker='o', color='b')

#Establecer límites para los ejes x, y, y z
ax.set_xlim([-1, 2])
ax.set_ylim([-1, 2])
ax.set_zlim([-1, 2])

#Etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
