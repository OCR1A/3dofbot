#Creo que solo falta validar su espacio de trabajo, wow, solo falta eso.
import numpy as np

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
xf = -1
yf = 7.07106781e-01
zf = 2.70710678e+00  
shud = 0       #Codo arriba, codo abajo, 0: codo abajo, 1: codo arriba

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