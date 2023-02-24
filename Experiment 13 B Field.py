import numpy as np
from numpy import loadtxt
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Files for Varying Magnetic Field Helium Spectra
# Need to Change File Path on Each Device

#667
He6674 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\667\4.5 mm", dtype = "double")
He6675 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\667\5.5 mm", dtype = "double")
He6676 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\667\6.5 mm", dtype = "double")
He6677 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\667\7.5 mm", dtype = "double")
x1,y1 = np.transpose(He6674)
x2,y2 = np.transpose(He6675)
x3,y3 = np.transpose(He6676)
x4,y4 = np.transpose(He6677)
Plot1 = plt.plot(x1,y1, label = "2.07 T")
Plot2 = plt.plot(x2,y2, label = "1.80 T")
Plot3 = plt.plot(x3,y3, label = "1.57 T")
Plot4 = plt.plot(x4,y4, label = "1.39 T")
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
Plot1 = plt.plot(x5,y5, label = "2.07 T")
Plot2 = plt.plot(x6,y6, label = "1.80 T")
Plot3 = plt.plot(x7,y7, label = "1.57 T")
Plot4 = plt.plot(x8,y8, label = "1.39 T")
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
Plot1 = plt.plot(x9,y9, label = "2.07 T")
Plot2 = plt.plot(x10,y10, label = "1.80 T")
Plot3 = plt.plot(x11,y11, label = "1.57 T")
Plot4 = plt.plot(x12,y12, label = "1.39 T")
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
Plot1 = plt.plot(x13,y13, label = "2.07 T")
Plot2 = plt.plot(x14,y14, label = "1.80 T")
Plot3 = plt.plot(x15,y15, label = "1.57 T")
Plot4 = plt.plot(x16,y16, label = "1.39 T")
plt.xlabel("Pixel Number")
plt.legend()
plt.ylabel("Intensity")
plt.title("Helium 1083 nm with Varying B Field")
plt.show()


# Plotting delta lambda as a function of B with error bars
B = [2.07 , 1.80 , 1.57 , 1.39]
Berr = [0.005, 0.005, 0.005, 0.005]
LAM667 = [84.7, 72.072, 64.064, 55.44]
err667 = [10.20, 10.20, 10.20, 10.20]
LAM706 = [113.245, 102.95, 95.98, 85.91]
err706 = [10.20, 10.20, 10.20, 10.20]
LAM728 = [87.696, 80.272, 70.064, 64.496]
err728 = [10.20, 10.20, 10.20, 10.20]
LAM1083 = [363.792, 309.52, 284.928, 262.88]
err1083 = [10.20, 10.20, 10.20, 10.20]

Plot5 = plt.errorbar(B,LAM667, xerr=Berr,yerr=err667, label = "667 nm", linestyle = '')
Plot6 = plt.errorbar(B,LAM706, xerr=Berr, yerr=err667, label = "706 nm", linestyle = '')
Plot7 = plt.errorbar(B,LAM728, xerr=Berr, yerr=err667, label = "728 nm", linestyle = '')
Plot8 = plt.errorbar(B,LAM1083, xerr=Berr, yerr=err667, label = "1083 nm", linestyle = '')

#Linear Fits for four sets of data
coef667 = np.polyfit(B, LAM667, 1)
f667 = np.poly1d(coef667)
Lin1 = plt.plot(B, f667(B), '--b')
#706
coef706 = np.polyfit(B, LAM706, 1)
f706 = np.poly1d(coef706)
Lin1 = plt.plot(B, f706(B), '--y')
#728
coef728 = np.polyfit(B, LAM728, 1)
f728 = np.poly1d(coef728)
Lin1 = plt.plot(B, f728(B), '--g')
#1083
coef1083 = np.polyfit(B, LAM1083, 1)
f1083 = np.poly1d(coef1083)
Lin1 = plt.plot(B, f1083(B), '--r')
#Plot labels
plt.xlabel("B Field (T)")
plt.legend()
plt.ylabel(r"$\Delta \lambda$ (pm)")
plt.title(r"B Field v. $\Delta \lambda$")
plt.show()

#Linear Fit Analysis
LA667 =linregress(B,LAM667)
LA706 =linregress(B,LAM706)
LA728 =linregress(B,LAM728)
LA1083 =linregress(B,LAM1083)

#Plotting delta lambda as a function of lambda squared with error bars for delta lamdba. Based on B value!
#Divide by 1000 to match nm to nm
#Did all B values but only really need 2.07 T bc its BMAX

LAM207 = [84.7/1000, 113.245/1000, 87.696/1000, 363.792/1000]
LAM18 = [72.072/1000, 102.95/1000, 80.272/1000, 309.52/1000]
LAM157 = [64.064/1000, 95.98/1000, 70.064/1000,284.928/1000]
LAM139 = [55.44/1000, 85.91/1000, 64.496/1000, 262.88/1000]
LSQ = [667.81517*667.81517, 706.57086*706.57086, 728.135*728.135, 1082.90911*1082.90911]
newerr667 = [10.20/1000, 10.20/1000, 10.20/1000, 10.20/1000]
Plot1 = plt.errorbar(LSQ,LAM207, yerr=newerr667, label = r"Exp. $\Delta\lambda$ at B = 2.07 T ", linestyle = '')
#Plot1 = plt.errorbar(LSQ,LAM18, yerr=newerr667, label = r"Exp. $\Delta\lambda$ at B = 1.80 T ", linestyle = '')
#Plot1 = plt.errorbar(LSQ,LAM157, yerr=newerr667, label = r"Exp. $\Delta\lambda$ at B = 1.57 T ", linestyle = '')
#Plot1 = plt.errorbar(LSQ,LAM139, yerr=newerr667, label = r"Exp. $\Delta\lambda$ at B = 1.39 T ", linestyle = '')

#Linear Fits for four sets of data, now based on B value
coef207 = np.polyfit(LSQ, LAM207, 1)
f207 = np.poly1d(coef207)
L207 = plt.plot(LSQ, f207(LSQ), '--b')
#180
coef18 = np.polyfit(LSQ, LAM18, 1)
f18 = np.poly1d(coef18)
#L18 = plt.plot(LSQ, f18(LSQ), '--y')
#157
coef157 = np.polyfit(LSQ, LAM157, 1)
f157 = np.poly1d(coef157)
#L157 = plt.plot(LSQ, f157(LSQ), '--g')
#139
coef139 = np.polyfit(LSQ, LAM139, 1)
f139 = np.poly1d(coef139)
#L139 = plt.plot(LSQ, f139(LSQ), '--r')

plt.xlabel(r"$\lambda^2\ (nm)^2$")
plt.legend()
plt.ylabel(r"$\Delta \lambda$ (nm)")
plt.title(r"$\lambda^2\ v.\ \Delta \lambda$")
plt.show()

#Linear Fit Analysis
LA207 =linregress(LSQ,LAM207)
LA18 =linregress(LSQ,LAM18)
LA157 =linregress(LSQ,LAM157)
LA139 =linregress(LSQ,LAM139)

