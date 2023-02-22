import numpy as np
from numpy import loadtxt
import matplotlib.pyplot as plt

# Calibration Files for Helium at 667, 706, 728, 1083
# Need to Change File Path on Each Device
# Use Kevin on PC, kdono user on laptop
    
ArHe667 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\667\Argon and He cal", dtype = "double")
#print(ArHe667)

x,y = np.transpose(ArHe667)
Plot1 = plt.plot(x,y)
plt.xlabel("Pixel Number")
plt.ylabel("Intensity")
#plt.xlim([1770, 2600])
plt.title("Argon and Helium 667 nm")
plt.show()

ArHe706 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\706\argon and helium cal", dtype = "double")
#print(ArHe706)

x2,y2 = np.transpose(ArHe706)
Plot2 = plt.plot(x2,y2)
plt.xlabel("Pixel Number")
plt.ylabel("Intensity")
plt.title("Argon and Helium 706 nm")
plt.show()

ArHe728 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\728\argon and helium cal", dtype = "double")
#print(ArHe728)

x3,y3 = np.transpose(ArHe728)
Plot3 = plt.plot(x3,y3)
plt.xlabel("Pixel Number")
plt.ylabel("Intensity")
plt.title("Argon and Helium 728 nm")
plt.show()

XeHe1083 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\1083\xenon and He", dtype = "double")
#print(XeHe1083)

x4,y4 = np.transpose(XeHe1083)
Plot3 = plt.plot(x4,y4)
plt.xlabel("Pixel Number")
plt.ylabel("Intensity")
plt.title("Xenon and Helium 1083 nm")
plt.show()

# 

