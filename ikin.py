#Creo que solo falta validar su espacio de trabajo, wow, solo falta eso.
import numpy as np

def calcJacobian(v, x0, y0, z0, x1, y1, z1, a1, a2, a3, a4):
    vx = (v*(x1 - x0)/(np.sqrt((x1 - x0)**2 + (y1 - y0)**2 + (z1 - z0)**2)))
    vy = (v*(y1 - y0)/(np.sqrt((x1 - x0)**2 + (y1 - y0)**2 + (z1 - z0)**2)))
    vz = (v*(z1 - z0)/(np.sqrt((x1 - x0)**2 + (y1 - y0)**2 + (z1 - z0)**2)))

    velocities = np.array([
                            [vx],
                            [vy],
                            [vz]
    ])

    T1 = 0
    T2 = 0
    T3 = 0

    T1 = np.radians(T1)
    T2 = np.radians(T2)
    T3 = np.radians(T3)

    #Posiciones d0_3
    a1_4 = -a4*np.sin(T1)*np.cos(T2)*np.cos(T3) + a4*np.sin(T1)*np.sin(T2)*np.sin(T3) + a2*np.cos(T1) - a3*np.sin(T1)*np.cos(T2)
    a2_4 = a4*np.cos(T1)*np.cos(T2)*np.cos(T3) - a4*np.cos(T1)*np.sin(T2)*np.sin(T3) + a3*np.cos(T1)*np.cos(T2) + a2*np.sin(T1)
    a3_4 = a4*np.sin(T2)*np.cos(T3) + a4*np.cos(T2)*np.sin(T3) + a3*np.sin(T2) + a1

    #Posiciones d0_2
    b1_4 = -a3*np.sin(T1)*np.cos(T2) + a2*np.cos(T1)
    b2_4 = a3*np.cos(T1)*np.cos(T2) + a2*np.sin(T1)
    b3_4 = a3*np.sin(T2) + a1

    #Posiciones d0_1
    c1_4 = a2*np.cos(T1)
    c2_4 = a2*np.sin(T1)
    c3_4 = a1

    #Para e11
    e1_1 = np.array([
                        [-a2_4],
                        [a1_4],
                        [0]
    ])

    #Para e12

    lam1_1 = a1_4 - c1_4
    lam2_1 = a2_4 - c2_4
    lam3_1 = a3_4 - c3_4

    e1_2 = np.array([
                        [lam3_1*np.sin(T1)],
                        [-lam3_1*np.cos(T1)],
                        [lam2_1*np.cos(T1) - lam1_1*np.sin(T1)]
    ])

    #Para e1_3
    lam1_1_2 = a1_4 - b1_4
    lam2_1_2 = a2_4 - b2_4
    lam3_1_2 = a3_4 - b3_4

    e1_3 = np.array([
                        [lam3_1_2*np.sin(T1)],
                        [-lam3_1_2*np.cos(T1)],
                        [lam2_1_2*np.cos(T1) - lam1_1_2*np.sin(T1)]
    ])

    vect1 = np.array([
                        [0],
                        [0],
                        [1]
    ])

    vect2 = np.array([
                        [np.cos(T1)],
                        [np.sin(T1)],
                        [0]
    ])

    J = np.hstack([e1_1, e1_2, e1_3, vect1, vect2, vect2])
    J = np.array([
                    [J[0][0], J[0][1], J[0][2]],
                    [J[1][0], J[1][1], J[1][2]],
                    [J[2][0], J[2][1], J[2][2]]
    ])

    print("Jacobiana: ")
    print(J)

    J_pinv = np.linalg.pinv(J)
    print("Pseudoinversa de la Jacobiana:")
    print(J_pinv)

    angularv = np.dot(J_pinv, velocities)

    print(angularv)

    return angularv[0][0], angularv[1][0], angularv[2][0]

def calcFkinematics(a1f, a2f, a3f, a4f, T1f, T2f, T3f):

    #Posiciones calculadas a mano
    a1f4 = (-a4f*np.sin(T1f)*np.cos(T2f)*np.cos(T3f)+a4f*np.sin(T1f)*np.sin(T2f)*np.sin(T3f)+a2f*np.cos(T1f)-a3f*np.sin(T1f)*np.cos(T2f))
    a2f4 = (a4f*np.cos(T1f)*np.cos(T2f)*np.cos(T3f)-a4f*np.cos(T1f)*np.sin(T2f)*np.sin(T3f)+a3f*np.cos(T1f)*np.cos(T2f)+a2f*np.sin(T1f))
    a3f4 = (a4f*np.sin(T2f)*np.cos(T3f)+a4f*np.cos(T2f)*np.sin(T3f)+a3f*np.sin(T2f)+a1f)
    print(a2f4)
    print(a3f4)

    return a1f4, a2f4, a3f4

#Eslabones
a1 = 1
a2 = 1
a3 = 1
a4 = 1

#Coordenadas, no puede calcularlas bien cuando el efector final se posa sobre algun eje
#Revisar cinemática cuando T3G debería ser mayor a 90
#Revisar cuando xf = 1, yf = 1, zf = 2 y shud = 1
#xf = 1, yf = 1, zf = 2 funciona solo cuando shud = 0   
#Revisar cuando xf = 2, yf = 1, zf = 1, debería ser th1 = 90, th2 = 180, th3 = 0
#Revisar cuando TH2 = 90 grados
xf = 0.034904812874567016
yf = 1
zf = 2.9996953903127825
shud = 0      #Codo arriba, codo abajo, 0: codo abajo, 1: codo arriba

#Comienza T1
s = np.sqrt(xf**2+yf**2-a2**2+(zf-a2)**2)
sxy = np.sqrt(xf**2+yf**2-a2**2)
h1 = np.sqrt(xf**2+yf**2+(zf-a2)**2)
if xf != 0 and yf != 0:
    phi1 = np.arctan(yf/xf)
elif xf == 0:
    phi1 = np.arcsin(yf/h1)
elif yf == 0:
    phi1 = np.arccos(xf/h1)
if a2 != 0 and sxy != 0:
    phi2 = np.arctan(a2/sxy)
elif sxy == 0:
    phi2 = np.arcsin(a2/h1)
if xf >= 0 and yf >= 0:
    T1 = np.abs(np.radians(90) - phi1 - phi2)
elif  xf < 0 and yf >= 0:
    T1 = np.abs(np.radians(90) + phi1 + phi2)
elif xf < 0 and yf < 0:
    T1 = np.abs(np.radians(90) + phi1 + phi2) 
elif xf >= 0 and yf < 0:
    T1 = np.radians(180) + np.abs(np.radians(90) + phi1 + phi2)

#Comienza T2
d1 = np.around((s**2+a3**2-a4**2)/(2*a3*s), decimals=5)
if -1 <= d1 <= 1:
    g1 = np.arccos(d1)
if sxy != 0 and (zf-a1) != 0:
    b1 = np.arctan((zf-a1)/sxy)
elif sxy == 0:
    b1 = np.arcsin((zf-a1)/s)
elif (zf-a1) == 0:
    b1 = np.arccos(sxy/s)
if shud == 0:
    T2 = b1 - g1
elif shud == 1:
    T2 = b1 + g1

#Comienza T3
d2 = np.around((a3**2+a4**2-s**2)/(2*a3*a4), decimals=5)
if -1 <= d2 <= 1:
    g3 = np.arccos(d2)
if shud == 0:
    T3 = np.radians(180) - g3
elif shud == 1:
    T3 = (np.radians(180) - g3) * -1

print(f"Para (x={xf}, y={yf}, z={zf}), T1={np.around(np.rad2deg(T1), decimals=2)}, T2={np.around(np.rad2deg(T2), decimals=2)}, T3={np.around(np.rad2deg(T3), decimals=2)}")

#wx, wy, wz = calcJacobian(1, 1, 2, 1, 1, 1, 2)
#print(wx)
#print(wy)
#print(wz)