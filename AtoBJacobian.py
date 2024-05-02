import numpy as np
import matplotlib.pyplot as plt

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
    R = np.sqrt(xf**2 + yf**2)
    yi = np.sqrt(R**2 - (a2-a4)**2)
    T1i = np.arctan2(yi, a2-a4)
    T1 = EFT - T1i

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
    g3 = np.arctan2(np.sqrt(1 - d2**2), d2)
    T3 = np.radians(180) - g3

    posx, posy, posz, H1, H2, H3, H4, H5 = calcFKinematics(T1, T2, T3, a1, a2, a3, a4, a5)

    return T1, T2, T3

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

#Simula la trayectoria del robot
def simulate(ax, T0_A1, T0_1, T0_2, T0_A2, T0_3):
    global trajectory_points
    
    trajectory_points.append((T0_3[0, 3], T0_3[1, 3], T0_3[2, 3]))

    x_trajectory = [pt[0] for pt in trajectory_points]
    y_trajectory = [pt[1] for pt in trajectory_points]
    z_trajectory = [pt[2] for pt in trajectory_points]

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

    ax.cla()
    ax.plot(0, 0, 0, marker='o', color='r')
    ax.plot(x_link1, y_link1, z_link1, marker='', color='r')
    ax.plot(x_link2, y_link2, z_link2, marker='o', color='g')
    ax.plot(x_link3, y_link3, z_link3, marker='', color='b')
    ax.plot(x_link4, y_link4, z_link4, marker='', color='b')
    ax.plot(x_trajectory, y_trajectory, z_trajectory, linestyle='--', color='m', label='End Effector Trajectory')

    ax.set_xlim([-400, 400])
    ax.set_ylim([-400, 400])
    ax.set_zlim([0, 400])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.pause(0.01)

#Mueve el robot entre dos puntos dados
def moveRobotBetweenPoints(origin, destination, a1, a2, a3, a4, a5, steps=10):

    x0, y0, z0 = origin
    x1, y1, z1 = destination

    fig = plt.figure("Inverse Kinematics Simulation")
    ax = fig.add_subplot(111, projection='3d')

    total_distance = np.sqrt((x1 - x0)**2 + (y1 - y0)**2 + (z1 - z0)**2)

    for i in range(steps):
        frac = i / (steps - 1)

        xf = x0 + frac * (x1 - x0)
        yf = y0 + frac * (y1 - y0)
        zf = z0 + frac * (z1 - z0)

        T1_curr, T2_curr, T3_curr = calcIKinematics(xf, yf, zf, a1, a2, a3, a4, a5)

        angular_velocities = calcJacobian(x0, y0, z0, xf, yf, zf, a1, a2, a3, a4, a5, np.degrees(T1_curr), np.degrees(T2_curr), np.degrees(T3_curr), 10)

        T1_curr += angular_velocities[0, 0] * (total_distance / steps)
        T2_curr += angular_velocities[1, 0] * (total_distance / steps)
        T3_curr += angular_velocities[2, 0] * (total_distance / steps)

        posx, posy, posz, T0_A1, T0_1, T0_2, T0_A2, T0_3 = calcFKinematics(T1_curr, T2_curr, T3_curr, a1, a2, a3, a4, a5)
        simulate(ax, T0_A1, T0_1, T0_2, T0_A2, T0_3)

        x0, y0, z0 = xf, yf, zf
   
trajectory_points = []

if __name__ == '__main__':

    #Tamaño de los eslabones en mm
    a1r = 133.2
    a2r = 69
    a3r = 285.25
    a4r = 23.5
    a5r = 100

    #destination = (3.8525, 0.4549999999999997, 1.3320000000000005)
    #Ejemplo 1:
    #origin = (288.1577386897249, 223.81102160174908, 1.4367397837861162)
    #destination = (-160.45164145601214, 224.79835854398794, 405.61288745211743)
    #Ejemplo 2:
    origin1 = (45.5, 301.7022093334627, 133.2)
    destination1 = (45.5, 301.7022093334627, 334.9022093334627)
    destination2 = (-130, 301.7022093334627, 334.9022093334627)
    destination3 = (-130, 301.7022093334627, 133.2)
    destination4 = (45.5, 301.7022093334627, 133.2)

    moveRobotBetweenPoints(origin1, destination1, a1r, a2r, a3r, a4r, a5r)
    moveRobotBetweenPoints(destination1, destination2, a1r, a2r, a3r, a4r, a5r)
    moveRobotBetweenPoints(destination2, destination3, a1r, a2r, a3r, a4r, a5r)
    moveRobotBetweenPoints(destination3, destination4, a1r, a2r, a3r, a4r, a5r)

    plt.show()