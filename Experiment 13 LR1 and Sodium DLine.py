import numpy as np
from numpy import loadtxt
import matplotlib.pyplot as plt
import scipy.signal as scipy
from scipy.signal import find_peaks 

# Files for Room Light, Helium, Cold/Hot Sodium, as well as the Sodium D-Line
# Need to Change File Path on Each Device
# Use Kevin on PC, kdono user on laptop
    
RoomL = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\Room Light Spectra.txt", dtype = "double")
#print(RoomL)

x,y = np.transpose(RoomL)
Plot1 = plt.plot(x,y)
plt.xlabel("Wavelength (nm)")
plt.ylabel("Intensity")
#plt.xlim([1770, 2600])
plt.title("Room Light Spectra")
plt.show()

Helium = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\Helium Spectra.txt", dtype = "double")
#print(Helium)

x2,y2 = np.transpose(Helium)
Plot2 = plt.plot(x2,y2)
plt.xlabel("Wavelength (nm)")
plt.ylabel("Intensity")
plt.title("Helium Spectra")
plt.show()

NAcold = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\Sodium Spectra.txt", dtype = "double")
#print(NAcold)

x3,y3 = np.transpose(NAcold)
Plot3 = plt.plot(x3,y3)
plt.xlabel("Wavelength (nm)")
plt.ylabel("Intensity")
plt.title("Sodium Spectra")
plt.show()

NAhot = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\hot sodium spectra.txt", dtype = "double")
#print(NAhot)

x4,y4 = np.transpose(NAhot)
Plot3 = plt.plot(x4,y4)
plt.xlabel("Wavelength (nm)")
plt.ylabel("Intensity")
plt.title("Sodium Hot Spectra")
plt.show()

#Finding Peaks in the Room Light, He, Na, and HOT Na
#Returns the NUMBER of the x coord (wavelength) rather than its value, so need to search within raw data

RoomPeak = find_peaks(y, height = 450.0)
print(RoomPeak)
HePeak = find_peaks(y2, height = 1200.0 )
print(HePeak)
NaCPeak = find_peaks(y3, height = 650.0)
print(NaCPeak)
NaHPeak = find_peaks(y4, height = 500.0)
print(NaHPeak)

#Sodium D1 and D2
NAD1 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\Sodium 589 no magnetic field", dtype = "double")

xNA,yNA = np.transpose(NAD1)
Plot3 = plt.plot(xNA,yNA)
plt.xlabel("Pixel Number")
plt.ylabel("Intensity")
plt.title("Sodium D-Line No Field")
plt.show()

NAD2 = loadtxt(r"C:\Users\Kevin\OneDrive - Northeastern University\Senior Spring LAST SEM\CAPSTONE\Lab 3\Audrey and Kevin\Sodium 589 magnetic field", dtype = "double")

xNA2,yNA2 = np.transpose(NAD2)
Plot3 = plt.plot(xNA2,yNA2)
plt.xlabel("Pixel Number")
plt.ylabel("Intensity")
plt.title("Sodium D-Line Magnetic Field")
plt.show()

#Messing with calculating FWHM of two Sodium D line graphs. Did it manually instead!!
NAnoBP, NApeakval = find_peaks(yNA, height = 20000.0)
NABP, NApeakvalB = find_peaks(yNA2, height = 20000.0)
#FWHMnoB = scipy.peak_widths(yNA, NAnoBP, rel_height = 0.5)
#FWHMB = scipy.peak_widths(yNA2, NABP, rel_height = 0.5)

