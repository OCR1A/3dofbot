import numpy as np
import matplotlib.pyplot as plt

#Calcula las coordenadas del efector final dado un conjunto de coordenadas articulares
def calcFKinematics(a1, a2, a3, T1, T2, d1):
    
    #Matrices de transformación homogenea
    T0_1 = np.array([
                        [np.cos(T1), -np.sin(T1), 0, 0],
                        [np.sin(T1), np.cos(T1), 0, 0],
                        [0, 0, 1, d1],
                        [0, 0, 0, 1]
    ])

    T1_2 = np.array([
                        [1, 0, 0, 0],
                        [0, 1, 0, a1],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]
    ])

    T2_A1 = np.array([
                        [1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 1, a2],
                        [0, 0, 0, 1]
    ])

    TA1_3 = np.array([
                        [np.cos(T2), -np.sin(T2), 0, -a3*np.sin(T2)],
                        [np.sin(T2), np.cos(T2), 0, a3*np.cos(T2)],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]
    ])

    T0_2 = np.dot(T0_1, T1_2)
    T0_A1 = np.dot(T0_2, T2_A1)
    T2_3 = np.dot(T2_A1, TA1_3)
    T0_3 = np.dot(T0_2, T2_3)

    print("Cinemática directa del Scara computada: ")
    print(T0_3)

    return T0_3[0][3], T0_3[1][3], T0_3[2][3], T0_1, T0_2, T0_A1, T0_3

#Calcula las coordenadas articulares dadas unas coordenadas del efector final
def calcIKinematics(xf, yf, zf, a1, a2, a3, d1):
    
    #Calculo de d1
    d1 = zf - a2
    
    #Calculo de T1
    EFT = -1*np.arctan2(xf, yf)
    EF = np.sqrt(xf**2 + yf**2)
    e1 = (EF**2 + a1**2 - a3**2)/(2*EF*a1)
    g1 = np.arctan2(np.sqrt(1 - e1**2), e1)
    T1 = EFT - g1

    #Calculo de T2
    xi = 0
    yi = a1 + a3
    if EF != np.sqrt(xi**2 + yi**2):
        e2 = (a1**2+a3**2-xf**2-yf**2)/(2*a1*a3)
        g2 = np.arctan2(np.sqrt(1-e2**2),e2)
        T2 = np.radians(180) - g2
    else: 
        T2 = 0

    x, y, z, T0_1, T0_2, T0_A1, T0_3 = calcFKinematics(a1, a2, a3, T1, T2, d1)

    return T1, T2, d1, T0_1, T0_2, T0_A1, T0_3

#Dibuja el mecanismo dadas las matrices de transformación homogenea
def draw(T0_1, T0_2, T0_A1, T0_3, name):
    
    #Simulación del robot utilizando matplotlib
    x_link1 = [0, T0_1[0, 3]]
    y_link1 = [0, T0_1[1, 3]]
    z_link1 = [0, T0_1[2, 3]]

    x_link2 = [T0_1[0, 3], T0_2[0, 3]]
    y_link2 = [T0_1[1, 3], T0_2[1, 3]]
    z_link2 = [T0_1[2, 3], T0_2[2, 3]]

    x_link3 = [T0_2[0, 3], T0_A1[0, 3]]
    y_link3 = [T0_2[1, 3], T0_A1[1, 3]]
    z_link3 = [T0_2[2, 3], T0_A1[2, 3]]

    x_link4 = [T0_A1[0, 3], T0_3[0, 3]]
    y_link4 = [T0_A1[1, 3], T0_3[1, 3]]
    z_link4 = [T0_A1[2, 3], T0_3[2, 3]]

    #Graficar
    fig = plt.figure(name)
    ax = fig.add_subplot(111, projection='3d')

    #Grafica cada eslabón con parámetros especiales para cada uno
    ax.plot(0, 0, 0, marker='o', color='r')
    ax.plot(x_link1, y_link1, z_link1, marker='', color='r')
    ax.plot(x_link2, y_link2, z_link2, marker='', color='g')
    ax.plot(x_link3, y_link3, z_link3, marker='', color='g')
    ax.plot(x_link4, y_link4, z_link4, marker='o', color='b')

    #Establecer límites para los ejes x, y, y z
    ax.set_xlim([-400, 400])
    ax.set_ylim([-400, 400])
    ax.set_zlim([0, 400])

    #Etiquetas de los ejes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

#Tamaños de eslabones
a1r = 285.25
a2r = 50
a3r = 133.2

#Ángulos en grados y valor del prismático
T1r = -90
T2r = -47.23
d1r = 100

#Conversión de los ángulos a radianes
T1r = np.radians(T1r)
T2r = np.radians(T2r)

#Simulación de la cinemática directa
xfr, yfr, zfr, H0_1r, H0_2r, H0_A1r, H0_3r = calcFKinematics(a1r, a2r, a3r, T1r, T2r, d1r)
draw(H0_1r, H0_2r, H0_A1r, H0_3r, "Forward kinematics")

#Simulación de cinemática inversa
T1i, T2i, d1i, H1i, H2i, H3i, H4i = calcIKinematics(H0_3r[0][3], H0_3r[1][3], H0_3r[2][3], a1r, a2r, a3r, d1r)
draw(H1i, H2i, H3i, H4i, "Inverse kinematics")
print(f"Theta1 calculado por la inversa: {np.rad2deg(T1i)}")
print(f"Theta2 calculado por la inversa: {np.rad2deg(T2i)}")
print(f"D1 calculado por la inversa: {d1i}")