from laspy.file import File
import numpy as np
import os

def LasToCsv(lasFileName, shift = True):
    lasFile = File(lasFileName, mode='r')
    X = lasFile.X
    Y = lasFile.Y
    Z = lasFile.Z
    if shift:
        X = X - min(X)
        Y = Y - min(Y)
        Z = Z - min(Z)
    I = lasFile.intensity
    index = np.arange(X.shape[0])
    data = np.stack((X,Y,Z,I,index),axis=1)
    np.savetxt(lasFileName+".csv", data, fmt="%.3f,%.3f,%.3f,%d,%d")


##put this .py file and .las files into same directory
##LasToCsv(f, False) for not to shift
for f in os.listdir(os.getcwd()):
    if f.endswith(".las"):
        print("current: " + f)
        LasToCsv(f)


## single file
# lasFileName = "place/of/the/las/file.las"
# LasToCsv(lasFileName)

