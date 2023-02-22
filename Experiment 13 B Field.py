import numpy as np
from numpy import loadtxt
import matplotlib.pyplot as plt

# Files for Varying Magnetic Field Helium Spectra
# Need to Change File Path on Each Device
# Use Kevin on PC, kdono user on laptop

#667
He6674 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\667\4.5 mm", dtype = "double")
He6675 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\667\5.5 mm", dtype = "double")
He6676 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\667\6.5 mm", dtype = "double")
He6677 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\667\7.5 mm", dtype = "double")
x1,y1 = np.transpose(He6674)
x2,y2 = np.transpose(He6675)
x3,y3 = np.transpose(He6676)
x4,y4 = np.transpose(He6677)
Plot1 = plt.plot(x1,y1, label = "4.5 mm")
Plot2 = plt.plot(x2,y2, label = "5.5 mm")
Plot3 = plt.plot(x3,y3, label = "6.5 mm")
Plot4 = plt.plot(x4,y4, label = "7.5 mm")
plt.xlabel("Pixel Number")
plt.legend()
plt.ylabel("Intensity")
plt.title("Helium 667 nm with Varying B Field")
plt.show()
#706
He7064 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\706\4.5 mm.txt", dtype = "double")
He7065 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\706\5.5 mm", dtype = "double")
He7066 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\706\6.5 mm", dtype = "double")
He7067 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\706\7.5 mm", dtype = "double")

x5,y5 = np.transpose(He7064)
x6,y6 = np.transpose(He7065)
x7,y7 = np.transpose(He7066)
x8,y8 = np.transpose(He7067)
Plot1 = plt.plot(x5,y5, label = "4.5 mm")
Plot2 = plt.plot(x6,y6, label = "5.5 mm")
Plot3 = plt.plot(x7,y7, label = "6.5 mm")
Plot4 = plt.plot(x8,y8, label = "7.5 mm")
plt.xlabel("Pixel Number")
plt.legend()
plt.ylabel("Intensity")
plt.title("Helium 706 nm with Varying B Field")
plt.show()
#728
He7284 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\728\4.5 mm.txt", dtype = "double")
He7285 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\728\5.5 mm.txt", dtype = "double")
He7286 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\728\6.5 mm.txt", dtype = "double")
He7287 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\728\7.5 mm.txt", dtype = "double")

x9,y9 = np.transpose(He7284)
x10,y10 = np.transpose(He7285)
x11,y11 = np.transpose(He7286)
x12,y12 = np.transpose(He7287)
Plot1 = plt.plot(x9,y9, label = "4.5 mm")
Plot2 = plt.plot(x10,y10, label = "5.5 mm")
Plot3 = plt.plot(x11,y11, label = "6.5 mm")
Plot4 = plt.plot(x12,y12, label = "7.5 mm")
plt.xlabel("Pixel Number")
plt.legend()
plt.ylabel("Intensity")
plt.title("Helium 728 nm with Varying B Field")
plt.show()
#1083
He10834 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\1083\4.5 mm.txt", dtype = "double")
He10835 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\1083\5.5 mm.txt", dtype = "double")
He10836 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\1083\6.5 mm.txt", dtype = "double")
He10837 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\1083\7.5 mm.txt", dtype = "double")

x13,y13 = np.transpose(He10834)
x14,y14 = np.transpose(He10835)
x15,y15 = np.transpose(He10836)
x16,y16 = np.transpose(He10837)
Plot1 = plt.plot(x13,y13, label = "4.5 mm")
Plot2 = plt.plot(x14,y14, label = "5.5 mm")
Plot3 = plt.plot(x15,y15, label = "6.5 mm")
Plot4 = plt.plot(x16,y16, label = "7.5 mm")
plt.xlabel("Pixel Number")
plt.legend()
plt.ylabel("Intensity")
plt.title("Helium 1083 nm with Varying B Field")
plt.show()