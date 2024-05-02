import numpy as np
import matplotlib.pyplot as plt
from time import sleep

#Calcula la posición del efector final dado un conjunto de coordenadas articulares
def calcFKinematics(T1, T2, T3, a1, a2, a3, a4):

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

    print(np.round(T0_3, decimals = 2))

    return T0_3[0][3], T0_3[1][3], T0_3[2][3], T0_A1, T0_1, T0_2, T0_3

#Calcula las coordenadas articulares dado un conjunto de coordenadas cartesianas del efector final
def calcIKinematics(xf, yf, zf, a1, a2, a3, a4):

    #Actualmente la cinemática es incapaz de predecir T2 cuando T2 = 180° yT3 = 180°

    #Comienza T1
    s = np.sqrt(xf**2+yf**2-a2**2+(zf-a2)**2)
    sxy = np.sqrt(xf**2+yf**2-a2**2)
    s2 = xf**2 + yf**2 - a2**2 + (zf - a2)**2
    sxy2 = xf**2 + yf**2 - a2**2
    if s2 < 0 or sxy2 < 0:
        xf = xf + 0.0000000000001
        yf = yf + 0.0000000000001
        zf = zf + 0.0000000000001
        s = np.sqrt(xf**2+yf**2-a2**2+(zf-a2)**2)
        sxy = np.sqrt(xf**2+yf**2-a2**2)
    EFT = np.arctan2(yf, xf)
    R = np.sqrt(xf**2 + yf**2)
    yi = np.sqrt(R**2 - a2**2)
    T1i = np.arctan2(yi, a2)
    T1 = EFT - T1i

    #Comienza T2
    d1 = np.around((s**2+a3**2-a4**2)/(2*a3*s), decimals=5)
    #g1 = np.arccos(d1)
    g1 = np.arctan2(np.sqrt(1 - d1**2), d1)
    #print(f"g1: {g1}")
    b1 = np.arctan2((zf-a1), sxy)
    print(f"Gamma 1: {np.rad2deg(g1)}")
    print(f"Betha 1: {np.rad2deg(b1)}")
    T2 = b1 - g1

    #Comienza T3
    d2 = np.around((a3**2+a4**2-s**2)/(2*a3*a4), decimals=5)
    #g3 = np.arccos(d2)
    g3 = np.arctan2(np.sqrt(1 - d2**2), d2)
    T3 = np.radians(180) - g3
    #print(f"T3 sin redondeo: {np.rad2deg(T3)}")
    #if np.isclose(T3, np.radians(180), atol=1e-8): # "atol" es la tolerancia absoluta
    #T3 = np.radians(179.9)

    #Calculamos la cinemática directa para simular y contrastar las coordenadas articulares obtenidas con la cinemática inversa y la cinemática directa
    posx, posy, posz, H1, H2, H3, H4 = calcFKinematics(T1, T2, T3, a1, a2, a3, a4)

    print(f"Para (x={xf}, y={yf}, z={zf}), T1={np.around(np.rad2deg(T1), decimals=2)}, T2={np.around(np.rad2deg(T2), decimals=2)}, T3={np.around(np.rad2deg(T3), decimals=2)}")

    return T1, T2, T3, posx, posy, posz, H1, H2, H3, H4

#Simula la configuración de eslabones del robot
def simulate(ax, T0_A1, T0_1, T0_2, T0_3):
    #Colectar las coordenadas para los enlaces del robot
    x_link1 = [0, T0_A1[0, 3], T0_1[0, 3]]
    y_link1 = [0, T0_A1[1, 3], T0_1[1, 3]]
    z_link1 = [0, T0_A1[2, 3], T0_1[2, 3]]

    x_link2 = [T0_1[0, 3], T0_2[0, 3]]
    y_link2 = [T0_1[1, 3], T0_2[1, 3]]
    z_link2 = [T0_1[2, 3], T0_2[2, 3]]

    x_link3 = [T0_2[0, 3], T0_3[0, 3]]
    y_link3 = [T0_2[1, 3], T0_3[1, 3]]
    z_link3 = [T0_2[2, 3], T0_3[2, 3]]

    #Limpiar la visualización antes de agregar nuevas líneas
    ax.cla()

    #Dibujar cada eslabón del robot
    ax.plot(0, 0, 0, marker='o', color='r')
    ax.plot(x_link1, y_link1, z_link1, marker='', color='r')
    ax.plot(x_link2, y_link2, z_link2, marker='o', color='g')
    ax.plot(x_link3, y_link3, z_link3, marker='o', color='b')

    #Establecer límites y etiquetas para los ejes
    ax.set_xlim([-1, 2])
    ax.set_ylim([-1, 2])
    ax.set_zlim([-1, 2])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.pause(0.05)

#Desplaza el robot entre un punto A y uno B
def move_robot_between_points(origin, destination, a1, a2, a3, a4, steps=100):
    #Desempaquetamos las coordenadas del origen y el destino
    x0, y0, z0 = origin
    x1, y1, z1 = destination

    #Calculamos los ángulos articulares iniciales y finales
    T1i, T2i, T3i, posx0, posy0, posz0, H1_0, H2_0, H3_0, H4_0 = calcIKinematics(x0, y0, z0, a1, a2, a3, a4)
    T1f, T2f, T3f, posx1, posy1, posz1, H1_1, H2_1, H3_1, H4_1 = calcIKinematics(x1, y1, z1, a1, a2, a3, a4)

    #Inicializamos la ventana de simulación
    fig = plt.figure("Inverse Kinematics Simulation")
    ax = fig.add_subplot(111, projection='3d')

    #Interpolamos entre los ángulos iniciales y finales
    for i in range(steps):
        T1_curr = T1i + i * (T1f - T1i) / (steps - 1)
        T2_curr = T2i + i * (T2f - T2i) / (steps - 1)
        T3_curr = T3i + i * (T3f - T3i) / (steps - 1)

        posx, posy, posz, T0_A1, T0_1, T0_2, T0_3 = calcFKinematics(T1_curr, T2_curr, T3_curr, a1, a2, a3, a4)

        simulate(ax, T0_A1, T0_1, T0_2, T0_3)

    plt.show()

if __name__ == '__main__':
    #Longitudes de los segmentos del robot
    a1r, a2r, a3r, a4r = 1, 1, 1, 1

    #Coordenadas de origen y destino
    origin = (-1.41, 1, 2.41)
    #destination = (1.8460004078225585, 0.9999999999999999, 1.0805981184150308)
    #destination = (1, 7.07106781e-01, 2.70710678e+00)
    destination = (-0.41, -1, 2.79)

    #Simulamos el movimiento entre los puntos
    move_robot_between_points(origin, destination, a1r, a2r, a3r, a4r)