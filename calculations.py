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

#Líneas punteadas para apoyo dimensional
xhelp1 = [T0_1[0, 3], T0_1[0, 3]]
yhelp1 = [T0_1[1, 3], T0_1[1, 3]]
zhelp1 = [0, T0_1[2, 3]]

xhelp2 = [T0_2[0, 3], T0_2[0, 3]]
yhelp2 = [T0_2[1, 3], T0_2[1, 3]]
zhelp2 = [0, T0_2[2, 3]]

xhelp3 = [T0_3[0, 3], T0_3[0, 3]]
yhelp3 = [T0_3[1, 3], T0_3[1, 3]]
zhelp3 = [0, T0_3[2, 3]]

xhelp4 = [T0_1[0, 3], T0_3[0, 3]]
yhelp4 = [T0_1[1, 3], T0_3[1, 3]]
zhelp4 = [T0_1[2, 3], T0_3[2, 3]]

#Línea entre codo y articulación 3
xhelp5 = [T0_A1[0, 3], T0_3[0, 3]]
yhelp5 = [T0_A1[1, 3], T0_3[1, 3]]
zhelp5 = [T0_A1[2, 3], T0_3[2, 3]]

xhelp6 = [0, T0_1[0, 3]]
yhelp6 = [0, T0_1[1, 3]]
zhelp6 = [0, 0]

xhelp7 = [T0_1[0, 3], T0_2[0, 3]]
yhelp7 = [T0_1[1, 3], T0_2[1, 3]]
zhelp7 = [0, 0]

xhelp8 = [T0_2[0, 3], T0_3[0, 3]]
yhelp8 = [T0_2[1, 3], T0_3[1, 3]]
zhelp8 = [0, 0]

xhelp9 = [0, 0, T0_3[0, 3]]
yhelp9 = [0, 0, T0_3[1, 3]]
zhelp9 = [0, 0, T0_3[2, 3]]

xhelp10 = [T0_1[0, 3], T0_3[0,3]]
yhelp10 = [T0_1[1, 3], T0_3[1,3]]
zhelp10 = [T0_1[2, 3], 1]

xhelp11 = [0, T0_3[0,3]]
yhelp11 = [0, T0_3[1,3]]
zhelp11 = [0, 0]

xhelp12 = [0, T0_3[0,3]]
yhelp12 = [0, T0_3[1,3]]
zhelp12 = [0, 0]

#Graficar
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#Grafica cada eslabón con parámetros especiales para cada uno
ax.plot(0, 0, 0, marker='o', color='r')
ax.plot(x_link1, y_link1, z_link1, marker='', color='r')
ax.plot(x_link2, y_link2, z_link2, marker='o', color='g')
ax.plot(x_link3, y_link3, z_link3, marker='o', color='b')

#Grafica todas las rectas de apoyo para dimensionar el mecanismo
ax.plot(xhelp1, yhelp1, zhelp1, marker='', color='black', linestyle='dashed')
ax.plot(xhelp2, yhelp2, zhelp2, marker='', color='black', linestyle='dashed')
ax.plot(xhelp3, yhelp3, zhelp3, marker='', color='black', linestyle='dashed')
ax.plot(xhelp4, yhelp4, zhelp4, marker='', color='black', linestyle='dashed') #Línea sigma
ax.plot(xhelp5, yhelp5, zhelp5, marker='', color='black', linestyle='dashed')
ax.plot(xhelp6, yhelp6, zhelp6, marker='', color='black', linestyle='dashed')
ax.plot(xhelp11, yhelp11, zhelp11, marker='', color='black', linestyle='dashed')

line_length = np.linalg.norm([xhelp4[-1] - xhelp4[0], yhelp4[-1] - yhelp4[0], zhelp4[-1] - zhelp4[0]])
print("Longitud de sigma", line_length)
line_length2 = np.linalg.norm([xhelp5[-1] - xhelp5[0], yhelp5[-1] - yhelp5[0], zhelp5[-1] - zhelp5[0]])
print("Longitud de h1", line_length2)

#Establecer límites para los ejes x, y, y z
ax.set_xlim([-1, 2])
ax.set_ylim([-1, 2])
ax.set_zlim([-1, 2])

#Etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

"""
#Proyección xy:
# Coordenadas para eslabones
x_link1 = [0, T0_A1[0, 3], T0_1[0, 3]]
y_link1 = [0, T0_A1[1, 3], T0_1[1, 3]]
z_link1 = [0, T0_A1[2, 3], T0_1[2, 3]]

x_link2 = [T0_1[0, 3], T0_2[0, 3]]
y_link2 = [T0_1[1, 3], T0_2[1, 3]]
z_link2 = [T0_1[2, 3], T0_2[2, 3]]

x_link3 = [T0_2[0, 3], T0_3[0, 3]]
y_link3 = [T0_2[1, 3], T0_3[1, 3]]
z_link3 = [T0_2[2, 3], T0_3[2, 3]]

# Graficar
fig = plt.figure()
ax = fig.add_subplot()

# Grafica cada eslabón con parámetros especiales para cada uno
ax.plot(x_link1, y_link1, marker='', color='r')
ax.plot(x_link2, y_link2, marker='o', color='g')
ax.plot(x_link3, y_link3, marker='o', color='b')

# Establecer límites para los ejes x, y
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])

# Etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')

plt.show()
"""