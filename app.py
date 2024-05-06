from interfaz import *
import numpy as np
import matplotlib.pyplot as plt
#plt.style.use('dark_background')
#Opciones seaborn-darkgrid

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

    if not ui.checkBox.isChecked():
        trajectory_points = []
    
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
    if ui.checkBox.isChecked():
        ax.plot(x_trajectory, y_trajectory, z_trajectory, linestyle='--', color='m', label='End Effector Trajectory')
    else:
        pass

    ax.set_xlim([-400, 400])
    ax.set_ylim([-400, 400])
    ax.set_zlim([0, 400])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.pause(0.02)

#Mueve el robot entre dos puntos dados
def moveRobotBetweenPoints(ax, origin, destination, a1, a2, a3, a4, a5, steps=10):
    
    x0, y0, z0 = origin
    x1, y1, z1 = destination

    total_distance = np.sqrt((x1 - x0)**2 + (y1 - y0)**2 + (z1 - z0)**2)

    for i in range(steps):
        frac = i / (steps - 1)

        xf = x0 + frac * (x1 - x0)
        yf = y0 + frac * (y1 - y0)
        zf = z0 + frac * (z1 - z0)

        T1_curr, T2_curr, T3_curr = calcIKinematics(xf, yf, zf, a1, a2, a3, a4, a5)

        angular_velocities = calcJacobian(x0, y0, z0, xf, yf, zf, a1, a2, a3, a4, a5, np.degrees(T1_curr), np.degrees(T2_curr), np.degrees(T3_curr), 1)

        T1_curr += angular_velocities[0, 0] * (total_distance / steps)
        T2_curr += angular_velocities[1, 0] * (total_distance / steps)
        T3_curr += angular_velocities[2, 0] * (total_distance / steps)

        posx, posy, posz, T0_A1, T0_1, T0_2, T0_A2, T0_3 = calcFKinematics(T1_curr, T2_curr, T3_curr, a1, a2, a3, a4, a5)
        simulate(ax, T0_A1, T0_1, T0_2, T0_A2, T0_3)

        x0, y0, z0 = xf, yf, zf

        ax.figure.canvas.draw()
        ax.figure.canvas.flush_events()

#Mueve el robot solo con la cinemática directa
def moveRobotFKinematics(ax, origin, destination, a1, a2, a3, a4, a5, steps=10):
    T1i, T2i, T3i = origin
    T1f, T2f, T3f = destination
    T1i = np.radians(T1i)
    T2i = np.radians(T2i)
    T3i = np.radians(T3i)
    T1f = np.radians(T1f)
    T2f = np.radians(T2f)
    T3f = np.radians(T3f)

    for i in range(steps):
        frac = i / (steps - 1)

        #Calcular los ángulos actuales en cada paso
        T1_curr = T1i + frac * (T1f - T1i)
        T2_curr = T2i + frac * (T2f - T2i)
        T3_curr = T3i + frac * (T3f - T3i)

        #Calcular la cinemática directa para obtener la posición actual
        _, _, _, T0_A1, T0_1, T0_2, T0_A2, T0_3 = calcFKinematics(T1_curr, T2_curr, T3_curr, a1, a2, a3, a4, a5)

        #Simular la posición actual del robot
        simulate(ax, T0_A1, T0_1, T0_2, T0_A2, T0_3)

#Lógica cuando se presiona el botón de la cinemática directa
def handleButtonPressFKinematics():

    global a1r, a2r, a3r, a4r, a5r
    global previous_T1Gr
    global previous_T2Gr
    global previous_T3Gr
    global previous_x
    global previous_y
    global previous_z

    #Obtiene los ángulos de destino ingresados por el usuario
    T1Gr = ui.doubleSpinBox_5.value()
    T2Gr = ui.doubleSpinBox_4.value()
    T3Gr = ui.doubleSpinBox_6.value()

    #Acomodo de los ángulos iniciales en una Tupla
    initial_angles = (np.radians(previous_T1Gr), np.radians(previous_T2Gr), np.radians(previous_T3Gr))

    #Longitudes de los eslabones del robot
    link_lengths = (a1r, a2r, a3r, a4r, a5r)

    #Volvemos una tupla los ángulos de destino y los convertimos a radianes
    destination_angles = (T1Gr, T2Gr, T3Gr)  # Ejemplo de ángulos destino en grados
    destination_angles = tuple(np.radians(ang) for ang in destination_angles)

    steps = 10

    for i in range(steps):
        frac = i / (steps - 1)

        #Interpolar entre ángulos iniciales y finales
        current_angles = tuple(
            initial + frac * (final - initial) 
            for initial, final in zip(initial_angles, destination_angles)
        )

        #Simulación de la cinemática directa
        x, y, z, H1r, H2r, H3r, H4r, H5r = calcFKinematics(*current_angles, *link_lengths)
        simulate(ui.ax, H1r, H2r, H3r, H4r, H5r)
        previous_x = x
        previous_y = y
        previous_z = z

        #Actualiza la GUI
        ui.ax.figure.canvas.draw()
        ui.ax.figure.canvas.flush_events()

        #Actualiza los LCD con los valores finales
        ui.lcdNumber_4.display(np.rad2deg(destination_angles[0]))
        ui.lcdNumber_5.display(np.rad2deg(destination_angles[1]))
        ui.lcdNumber_6.display(np.rad2deg(destination_angles[2]))
        xf, yf, zf, _, _, _, _, _ = calcFKinematics(destination_angles[0], destination_angles[1], destination_angles[2], a1r, a2r, a3r, a4r, a5r)
        ui.lcdNumber.display(np.round(xf, decimals = 2))
        ui.lcdNumber_2.display(np.round(yf, decimals = 2))
        ui.lcdNumber_3.display(np.round(zf, decimals = 2))
        previous_T1Gr = T1Gr
        previous_T2Gr = T2Gr
        previous_T3Gr = T3Gr

#Lógica cuando se presiona el botón de trayectorias lineales
def handleButtonPressLinearPath():

    global a1r, a2r, a3r, a4r, a5r
    global previous_x
    global previous_y
    global previous_z
    global previous_T1Gr
    global previous_T2Gr
    global previous_T3Gr

    #Recuperar las coordenadas de origen y destino desde la interfaz de usuario
    x0 = previous_x
    y0 = previous_y
    z0 = previous_z
    xf = ui.doubleSpinBox.value()
    yf = ui.doubleSpinBox_2.value()
    zf = ui.doubleSpinBox_3.value()

    #Coordenadas del punto de origen
    origin = (x0, y0, z0)
    #Coordenadas del punto de destino
    destination = (xf, yf, zf)

    #Longitudes de los eslabones del robot, que podrían estar definidas globalmente o recuperadas de la GUI
    link_lengths = (a1r, a2r, a3r, a4r, a5r)
    
    #Llamar a la función moveRobotBetweenPoints con los parámetros adecuados
    moveRobotBetweenPoints(ui.ax, origin, destination, *link_lengths, 10)

    # Actualizar la GUI con los últimos valores y la simulación
    ui.ax.figure.canvas.draw()
    ui.ax.figure.canvas.flush_events()
    previous_x = xf
    previous_y = yf
    previous_z = zf
    ui.lcdNumber.display(np.round(xf, decimals = 2))
    ui.lcdNumber_2.display(np.round(yf, decimals = 2))
    ui.lcdNumber_3.display(np.round(zf, decimals = 2))
    previous_T1Gr, previous_T2Gr, previous_T3Gr = calcIKinematics(xf, yf, zf, a1r, a2r, a3r, a4r, a5r)
    previous_T1Gr = np.rad2deg(previous_T1Gr)
    previous_T2Gr = np.rad2deg(previous_T2Gr)
    previous_T3Gr = np.rad2deg(previous_T3Gr)
    ui.lcdNumber_4.display(previous_T1Gr)
    ui.lcdNumber_5.display(previous_T2Gr)
    ui.lcdNumber_6.display(previous_T3Gr)

#Función para manejar la lógica de la checkbox1
def handleCheckBox1(state):
    pass

#Variables globales
trajectory_points = []
previous_T1Gr = 0
previous_T2Gr = 0
previous_T3Gr = 0
previous_x = 45.5
previous_y = 385.25
previous_z = 133.2

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    #Tamaño de los eslabones en mm
    a1r = 133.2
    a2r = 69
    a3r = 285.25
    a4r = 23.5
    a5r = 100

    #Ángulos en grados
    T1Gr = ui.doubleSpinBox.value()
    T2Gr = ui.doubleSpinBox_2.value()
    T3Gr = ui.doubleSpinBox_3.value()

    #Ángulos en radianes
    T1r = np.radians(T1Gr)
    T2r = np.radians(T2Gr)
    T3r = np.radians(T3Gr) 

    ui.pushButton_9.pressed.connect(handleButtonPressFKinematics)
    ui.pushButton_10.pressed.connect(handleButtonPressLinearPath)
    ui.checkBox.stateChanged.connect(handleCheckBox1)

    #Simulación de la cinemática directa
    x, y, z, H1r, H2r, H3r, H4r, H5r = calcFKinematics(T1r, T2r, T3r, a1r, a2r, a3r, a4r, a5r)
    simulate(ui.ax, H1r, H2r, H3r, H4r, H5r)
    ui.lcdNumber.display(np.round(x, decimals = 2))
    ui.lcdNumber_2.display(np.round(y, decimals = 2))
    ui.lcdNumber_3.display(np.round(z, decimals = 2))
    
    sys.exit(app.exec_())