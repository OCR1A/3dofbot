import numpy as np
import matplotlib.pyplot as plt
from time import sleep

#Eslabones
a1 = 1
a2 = 1
a3 = 1
a4 = 1

#Coordenadas
xf = -1.72429919
yf = 0.97005457 #Se rompe arriba de 90°
zf = 0.29289322 #Se rompe arriba de 180°
shud = 0 #Codo arriba, codo abajo, 0: codo abajo, 1: codo arriba

#Un mar de variables
s = np.sqrt(xf**2+yf**2-a2**2+(zf-a2)**2)
sxy = np.sqrt(xf**2+yf**2-a2**2)
h1 = np.sqrt(xf**2+yf**2+(zf-a2)**2)
e2 = np.arctan(a2/sxy)
psi2 = np.arctan(xf/yf)
psi1 = e2-psi2
u1 = np.radians(90) - psi1
Ix = sxy*np.cos(u1)
Iy = sxy*np.sin(u1)
x1 = 0
y1 = 0
circ = np.sqrt(x1**2 + y1**2)
cdr = 0

#Encunetra la diferencia de catetos que resuelve la circunferencia trazada por a2 y (xf, yf)
while circ != a1:
    if cdr == 0:
        x1 = xf + Ix
        y1 = yf - Iy
        print("1")
    elif cdr == 1:
        x1 = xf - Ix
        y1 = yf + Iy
        print("2")
    elif cdr == 2:
        x1 = xf + Ix
        y1 = yf + Iy
        print("3")
    elif cdr == 3:
        x1 = xf - Ix
        y1 = yf - Iy
        print("4")
        
    circ = np.around((np.sqrt(x1**2 + y1**2)), decimals=7)
    #print(f"circ: {circ}")
    cdr = cdr + 1

#Comienza T1        
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
T1 = np.abs(np.radians(90) - phi1 - phi2)
if x1 > 0 and y1 > 0:
    T1 = np.arctan((yf-Iy)/(xf+Ix))
    print("Primer cuadrante")
elif x1 < 0 and y1 > 0:
    T1 = np.abs(np.radians(90) - phi1 - phi2)
    print("Segundo cuadrante")
elif x1 < 0 and y1 < 0:
    T1 = np.abs(np.radians(90) - phi1 - phi2)
    print("Tercer cuadrante")
elif x1 > 0 and y1 < 0:
    T1 = np.abs(np.radians(90) - phi1 - phi2)
    print("Cuarto cuadrante")

#Vectores unitarios del marco de referencia original
x0 = np.array([[1], [0], [0]])
y0 = np.array([[0], [-1], [0]])
z0 = np.array([[0], [0], [1]])

#Rotación del marco {1}
R0_1 = np.array([
    [np.cos(T1), -np.sin(T1), 0],
    [np.sin(T1), np.cos(T1), 0],
    [0, 0, 1]
])

#Posición del marco {1}
P0_1 = np.array([
                [a2*np.cos(T1)],
                [a2*np.sin(T1)],
                [a1]
])

#Rotación del marco {1}
x1 = np.dot(R0_1, x0)
y1 = np.dot(R0_1, y0)
z1 = np.dot(R0_1, z0)

#Redondeo
umbral = 1e-10
x1[np.abs(x1) < umbral] = 0
y1[np.abs(y1) < umbral] = 0
z1[np.abs(z1) < umbral] = 0
print(f"x1: {x1[0][0]}")
print(f"y1: {y1[0][0]}")
print(f"z1: {z1[0][0]}")

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

#Condicionales respecto al marco {1}
if x1[0][0] >= 0 and y1[0][0] >= 0:
    if shud == 0:
        T2 = b1 - g1             
    elif shud == 1:
        T2 = b1 + g1
elif y1[0][0] < 0:
    if shud == 0:
        T2 = np.radians(180) - b1      
    elif shud == 1:
        T2 = -np.radians(180) + b1
else:
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

print(f"T1: {np.rad2deg(T1)}")
print(f"T2: {np.rad2deg(T2)}")
print(f"T3: {np.rad2deg(T3)}")