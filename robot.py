import numpy as np
import matplotlib.pyplot as plt
from time import sleep

#Calcula la cinemática directa
def calcFKinematics(T1, T2, T3, a1, a2, a3, a4, a5):
    R0_A1 = np.eye(3)

    RA1_1 = np.array([
                        [np.cos(T1), -np.sin(T1), 0],
                        [np.sin(T1), np.cos(T1), 0],
                        [0, 0, 1]
    ])

    rA1_1 = np.array([
                        [0, 0, 1],
                        [1, 0, 0],
                        [0, 1, 0]
    ])

    RA1_1 = np.dot(RA1_1, rA1_1)

    R1_2 = np.array([
                        [np.cos(T2), -np.sin(T2), 0],
                        [np.sin(T2), np.cos(T2), 0],
                        [0, 0, 1]
    ])

    R2_A2 = np.eye(3)

    RA2_3 = np.array([
                        [np.cos(T3), -np.sin(T3), 0],
                        [np.sin(T3), np.cos(T3), 0],
                        [0, 0, 1]
    ])

    P0_A1 = np.array([[0], [0], [a1]])
    PA1_1 = np.array([
                        [a2 * np.cos(T1)],
                        [a2 * np.sin(T1)],
                        [0]
    ])
    P1_2 = np.array([
                        [a3 * np.cos(T2)],
                        [a3 * np.sin(T2)],
                        [0]
    ])
    P2_A2 = np.array([
                        [0],
                        [0],
                        [-a4]
    ])
    PA2_3 = np.array([
                        [a5 * np.cos(T3)],
                        [a5 * np.sin(T3)],
                        [0]
    ])

    T0_A1 = np.concatenate((R0_A1, P0_A1), 1)
    T0_A1 = np.concatenate((T0_A1, [[0, 0, 0, 1]]), 0)
    TA1_1 = np.concatenate((RA1_1, PA1_1), 1)
    TA1_1 = np.concatenate((TA1_1, [[0, 0, 0, 1]]), 0)
    T1_2 = np.concatenate((R1_2, P1_2), 1)
    T1_2 = np.concatenate((T1_2, [[0, 0, 0, 1]]), 0)
    T2_A2 = np.concatenate((R2_A2, P2_A2), 1)
    T2_A2 = np.concatenate((T2_A2, [[0, 0, 0, 1]]), 0)
    TA2_3 = np.concatenate((RA2_3, PA2_3), 1)
    TA2_3 = np.concatenate((TA2_3, [[0, 0, 0, 1]]), 0)

    T0_1 = np.dot(T0_A1, TA1_1)
    T0_2 = np.dot(T0_1, T1_2)
    T0_A2 = np.dot(T0_2, T2_A2)
    T0_3 = np.dot(T0_A2, TA2_3)

    return T0_3[0][3], T0_3[1][3], T0_3[2][3], T0_A1, T0_1, T0_2, T0_A2, T0_3

#Calcula las coordenadas articulares dado un conjunto de coordenadas cartesianas del efector final
def calcIKinematics(xf, yf, zf, a1, a2, a3, a4, a5):
    #Comienza T1
    EFT = np.arctan2(yf, xf)
    #print(f'EFT:{np.rad2deg(EFT)}')
    R = np.sqrt(xf**2 + yf**2)
    #print(f'R:{R}')
    yi = np.sqrt(R**2 - (a2-a4)**2)
    #print(f'yi:{yi}')
    T1i = np.arctan2(yi, a2-a4)
    #print(f'T1i:{np.rad2deg(T1i)}')
    T1 = EFT - T1i
    #print(f'T1:{T1}')

    #Comienza T2
    a4x = a4*np.cos(T1)
    a4y = a4*np.sin(T1)
    xf2 = xf + a4x
    yf2 = yf + a4y
    Bxy = np.sqrt(xf2**2 + yf2**2 - a2**2)
    B = np.sqrt(Bxy**2 + (zf - a1)**2)
    d1 = np.around((B**2+a3**2-a5**2)/(2*a3*B), decimals=5)
    g1 = np.arctan2(np.sqrt(1 - d1**2), d1)
    b1 = np.arctan2((zf-a1), Bxy)
    T2 = b1 - g1

    #Comienza T3
    d2 = np.around((a3**2+a5**2-B**2)/(2*a3*a5), decimals=5)
    #print(f'd2:{d2}')
    g3 = np.arctan2(np.sqrt(1 - d2**2), d2)
    #print(f'g3:{g3}')
    T3 = np.radians(180) - g3
    #print(f'T3:{T3}')

    posx, posy, posz, H1, H2, H3, H4, H5 = calcFKinematics(T1, T2, T3, a1, a2, a3, a4, a5)

    print(f"Para (x={xf}, y={yf}, z={zf}), T1={np.around(np.rad2deg(T1), decimals=2)}, T2={np.around(np.rad2deg(T2), decimals=2)}, T3={np.around(np.rad2deg(T3), decimals=2)}")

    return T1, T2, T3, posx, posy, posz, H1, H2, H3, H4, H5

#Retorna las velocidades angulares para generar una tayectoria lineal
def calcJacobian(x0, y0, z0, xf, yf, zf, a1, a2, a3, a4, a5, T1, T2, T3, v):
    velocities = np.array([
                            [(v*(xf - x0))/(np.sqrt((xf - x0)**2 + (yf - y0)**2 + (zf + z0)**2))],
                            [(v*(yf - y0))/(np.sqrt((xf - x0)**2 + (yf - y0)**2 + (zf + z0)**2))],
                            [(v*(zf - z0))/(np.sqrt((xf - x0)**2 + (yf - y0)**2 + (zf + z0)**2))]
    ])

    T1 = np.radians(T1)
    T2 = np.radians(T2)
    T3 = np.radians(T3)

    R0_A1 = np.eye(3)
    RA1_1 = np.array([
                        [np.cos(T1), -np.sin(T1), 0],
                        [np.sin(T1), np.cos(T1), 0],
                        [0, 0, 1]
    ])
    RA1_1 = np.dot(RA1_1, np.array([
                        [0, 0, 1],
                        [1, 0, 0],
                        [0, 1, 0]
    ]))

    R1_2 = np.array([
                        [np.cos(T2), -np.sin(T2), 0],
                        [np.sin(T2), np.cos(T2), 0],
                        [0, 0, 1]
    ])

    R2_A2 = np.eye(3)

    R0_1 = np.dot(R0_A1, RA1_1)
    R0_2 = np.dot(R0_1, R1_2)
    R0_A2 = np.dot(R0_2, R2_A2)

    #d0_3
    a1_4 = -a5*np.sin(T1)*np.cos(T2)*np.cos(T3) + a5*np.sin(T1)*np.sin(T2)*np.sin(T3) - a4*np.cos(T1) - a3*np.sin(T1)*np.cos(T2) + a2*np.cos(T1)
    a2_4 = a5*np.cos(T1)*np.cos(T2)*np.cos(T3) - a5*np.cos(T1)*np.sin(T2)*np.sin(T3) - a4*np.sin(T1) + a3*np.cos(T1)*np.cos(T2) + a2*np.sin(T1)
    a3_4 = a5*np.sin(T2)*np.cos(T3) + a5*np.cos(T2)*np.sin(T3) + a3*np.sin(T2) + a1

    #d0_2 si no funciona probar con coeficientes de T0_A2
    #b1_4 = -a3*np.sin(T1)*np.cos(T2) + a2*np.cos(T1)
    #b2_4 = a3*np.cos(T1)*np.cos(T2) + a2*np.sin(T1)
    #b3_4 = a3*np.sin(T2) + a1
    b1_4 = -a4*np.cos(T1) - a3*np.sin(T1)*np.cos(T2) + a2*np.cos(T1)
    b2_4 = -a4*np.sin(T1) + a3*np.cos(T1)*np.cos(T2) + a2*np.sin(T1)
    b3_4 = a3*np.sin(T2) + a1

    #d0_1
    c1_4 = a2*np.cos(T1)
    c2_4 = a2*np.sin(T1)
    c3_4 = a1

    e1_1 = np.array([
                        [-a2_4],
                        [a1_4],
                        [0]
    ])

    lam1_1 = a1_4 - c1_4
    lam2_1 = a2_4 - c2_4
    lam3_1 = a3_4 - c3_4

    e1_2 = np.array([
                        [lam3_1*np.sin(T1)],
                        [-lam3_1*np.cos(T1)],
                        [lam2_1*np.cos(T1) - lam1_1*np.sin(T1)]
    ])

    lam1_1_2 = a1_4 - b1_4
    lam2_1_2 = a2_4 - b2_4
    lam3_1_2 = a3_4 - b3_4

    e1_3 = np.array([
                        [lam3_1_2*np.sin(T1)],
                        [-lam3_1_2*np.cos(T1)],
                        [lam2_1_2*np.cos(T1) - lam1_1_2*np.sin(T1)]
    ])

    e2_1 = np.array([
                        [0],
                        [0],
                        [1]
    ])
    e2_2 = np.dot(R0_1, e2_1)
    e2_3 = np.dot(R0_A2, e2_1)

    J = np.hstack([np.concatenate((e1_1, e2_1), 0), np.concatenate((e1_2, e2_2), 0), np.concatenate((e1_3, e2_3), 0)])
    J = J[:3, :3]

    J_pinv = np.linalg.pinv(J)
    angular = np.dot(J_pinv, velocities)

    return angular

#Función para simular el robot obtenido tanto por el algoritmo directo como el inverso
def simulate(T0_A1, T0_1, T0_2, T0_A2, T0_3, name):
    #Coordenadas para eslabones
    x_link1 = [0, T0_A1[0, 3], T0_1[0, 3]]
    y_link1 = [0, T0_A1[1, 3], T0_1[1, 3]]
    z_link1 = [0, T0_A1[2, 3], T0_1[2, 3]]

    x_link2 = [T0_1[0, 3], T0_2[0, 3]]
    y_link2 = [T0_1[1, 3], T0_2[1, 3]]
    z_link2 = [T0_1[2, 3], T0_2[2, 3]]

    x_link3 = [T0_2[0, 3], T0_A2[0, 3]]
    y_link3 = [T0_2[1, 3], T0_A2[1, 3]]
    z_link3 = [T0_2[2, 3], T0_A2[2, 3]]

    x_link4 = [T0_A2[0, 3], T0_3[0, 3]]
    y_link4 = [T0_A2[1, 3], T0_3[1, 3]]
    z_link4 = [T0_A2[2, 3], T0_3[2, 3]]

    #Graficar
    fig = plt.figure(name)
    ax = fig.add_subplot(111, projection='3d')

    #Grafica cada eslabón con parámetros especiales para cada uno
    ax.plot(0, 0, 0, marker='o', color='r')
    ax.plot(x_link1, y_link1, z_link1, marker='', color='r')
    ax.plot(x_link2, y_link2, z_link2, marker='o', color='g')
    ax.plot(x_link3, y_link3, z_link3, marker='', color='b')
    ax.plot(x_link4, y_link4, z_link4, marker='', color='b')

    #Coordenadas mínimas y máximas en cada eje
    x_coords = x_link1 + x_link2 + x_link3 + x_link4
    y_coords = y_link1 + y_link2 + y_link3 + y_link4
    z_coords = z_link1 + z_link2 + z_link3 + z_link4

    #Establecer límites para los ejes x, y, y z
    ax.set_xlim(-400, 400)
    ax.set_ylim(-400, 400)
    ax.set_zlim(0, 400)

    #Etiquetas de los ejes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

#Retorna las velocidades angulares para generar una tayectoria lineal
def calcJacobian(x0, y0, z0, xf, yf, zf, a1, a2, a3, a4, T1, T2, T3):
    velocities = np.array([
                            [(xf - x0)],
                            [(yf - y0)],
                            [(zf - z0)]
    ])

    T1 = np.radians(T1)
    T2 = np.radians(T2)
    T3 = np.radians(T3)

    R0_A1 = np.eye(3)
    RA1_1 = np.array([
                        [np.cos(T1), -np.sin(T1), 0],
                        [np.sin(T1), np.cos(T1), 0],
                        [0, 0, 1]
    ])
    RA1_1 = np.dot(RA1_1, np.array([
                        [0, 0, 1],
                        [1, 0, 0],
                        [0, 1, 0]
    ]))

    R1_2 = np.array([
                        [np.cos(T2), -np.sin(T2), 0],
                        [np.sin(T2), np.cos(T2), 0],
                        [0, 0, 1]
    ])

    R2_A2 = np.eye(3)

    R0_1 = np.dot(R0_A1, RA1_1)
    R0_2 = np.dot(R0_1, R1_2)

    a1_4 = -a4*np.sin(T1)*np.cos(T2)*np.cos(T3) + a4*np.sin(T1)*np.sin(T2)*np.sin(T3) + a2*np.cos(T1) - a3*np.sin(T1)*np.cos(T2)
    a2_4 = a4*np.cos(T1)*np.cos(T2)*np.cos(T3) - a4*np.cos(T1)*np.sin(T2)*np.sin(T3) + a3*np.cos(T1)*np.cos(T2) + a2*np.sin(T1)
    a3_4 = a4*np.sin(T2)*np.cos(T3) + a4*np.cos(T2)*np.sin(T3) + a3*np.sin(T2) + a1

    b1_4 = -a3*np.sin(T1)*np.cos(T2) + a2*np.cos(T1)
    b2_4 = a3*np.cos(T1)*np.cos(T2) + a2*np.sin(T1)
    b3_4 = a3*np.sin(T2) + a1

    c1_4 = a2*np.cos(T1)
    c2_4 = a2*np.sin(T1)
    c3_4 = a1

    e1_1 = np.array([
                        [-a2_4],
                        [a1_4],
                        [0]
    ])

    lam1_1 = a1_4 - c1_4
    lam2_1 = a2_4 - c2_4
    lam3_1 = a3_4 - c3_4

    e1_2 = np.array([
                        [lam3_1*np.sin(T1)],
                        [-lam3_1*np.cos(T1)],
                        [lam2_1*np.cos(T1) - lam1_1*np.sin(T1)]
    ])

    lam1_1_2 = a1_4 - b1_4
    lam2_1_2 = a2_4 - b2_4
    lam3_1_2 = a3_4 - b3_4

    e1_3 = np.array([
                        [lam3_1_2*np.sin(T1)],
                        [-lam3_1_2*np.cos(T1)],
                        [lam2_1_2*np.cos(T1) - lam1_1_2*np.sin(T1)]
    ])

    e2_1 = np.array([
                        [0],
                        [0],
                        [1]
    ])
    e2_2 = np.dot(R0_1, e2_1)
    e2_3 = np.dot(R0_2, e2_1)

    J = np.hstack([np.concatenate((e1_1, e2_1), 0), np.concatenate((e1_2, e2_2), 0), np.concatenate((e1_3, e2_3), 0)])
    J = J[:3, :3]

    J_pinv = np.linalg.pinv(J)
    angular = np.dot(J_pinv, velocities)

    return angular

#Tamaño de los eslabones en mm
a1r = 133.2
a2r = 69
a3r = 285.25
a4r = 23.5
a5r = 100

#Ángulos en grados
T1Gr = 0
T2Gr = 87
T3Gr = 64

#Ángulos en radianes
T1r = np.radians(T1Gr)
T2r = np.radians(T2Gr)
T3r = np.radians(T3Gr)

#Simulación de la cinemática directa
x, y, z, H1r, H2r, H3r, H4r, H5r = calcFKinematics(T1r, T2r, T3r, a1r, a2r, a3r, a4r, a5r)
simulate(H1r, H2r, H3r, H4r, H5r, "Forward kinematics simulation")
print("Coordenadas calculadas por la cinemática directa: ")
print(f"xf: {x}")
print(f"yf: {y}")
print(f"zf: {z}")

#Comprobación de la cinemática inversa
T1i, T2i, T3i, xi, yi, zi, H1i, H2i, H3i, H4i, H5i = calcIKinematics(H5r[0][3], H5r[1][3], H5r[2][3], a1r, a2r, a3r, a4r, a5r)
simulate(H1i, H2i, H3i, H4i, H5i, "Inverse kinematics simulation")