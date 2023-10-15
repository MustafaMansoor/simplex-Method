import numpy as np
coffeArray = [3, 5]
sizeOfCoffeArray = len(coffeArray)
numOfCons = 3

Coffbasic = [0] * numOfCons

rightsidevalues = [4, 12, 18]
calculatedValue = 0

nonbasicvalues = [[0] * sizeOfCoffeArray for _ in range(numOfCons)]

nonbasicvalues[0][0] = 1
nonbasicvalues[0][1] = 0
nonbasicvalues[1][0] = 0
nonbasicvalues[1][1] = 2
nonbasicvalues[2][0] = 3
nonbasicvalues[2][1] = 2

basicvalues = [[1 if i == j else 0 for j in range(numOfCons)] for i in range(numOfCons)]





def getmaxCoffIndex(coffeArray):
    return coffeArray.index(max(coffeArray))


def calratiotest(nonbasicvalues, rightsidevalues, ReplacingIndexFromNonBasic):
    ratios = []

    for i in range(len(nonbasicvalues)):
        if nonbasicvalues[i][ReplacingIndexFromNonBasic] > 0:
            ratio = rightsidevalues[i] / nonbasicvalues[i][ReplacingIndexFromNonBasic]
            ratios.append(ratio)
        else:
            ratios.append(float("inf"))
    min_ratio = ratios.index(min(ratios))
    return min_ratio



ReplacingIndexFromNonBasic=getmaxCoffIndex(coffeArray)
ReplacingIndexFromBasic=calratiotest(nonbasicvalues,rightsidevalues,ReplacingIndexFromNonBasic)

def replaceColumnInBasicValues(basicvalues, nonbasicvalues, replacingIndexFromNonBasic, replacingIndexFromBasic):
    # Convert the input lists to NumPy arrays
    basicvalues = np.array(basicvalues)
    nonbasicvalues = np.array(nonbasicvalues)

    if len(nonbasicvalues) != len(basicvalues):
        raise ValueError("Both matrices must have the same number of rows for replacement.")
    
    basicvalues[:, replacingIndexFromBasic] = nonbasicvalues[:, replacingIndexFromNonBasic]
    return basicvalues

basicvalues=replaceColumnInBasicValues(basicvalues, nonbasicvalues, ReplacingIndexFromNonBasic, ReplacingIndexFromBasic)

basicvalues=np.linalg.inv(basicvalues)


def Binverseb(basicvalues,rightsidevalues):
    return np.dot(basicvalues,rightsidevalues)


def calculateCB(Coffbasic,coffeArray,ReplacingIndexFromBasic,ReplacingIndexFromNonBasic):
     Coffbasic[ReplacingIndexFromBasic]=coffeArray[ReplacingIndexFromNonBasic]
     return Coffbasic
Coffbasic=calculateCB(Coffbasic,coffeArray,ReplacingIndexFromBasic,ReplacingIndexFromNonBasic)



def calculateCBinverseB(basicvalues,Coffbasic):
    return np.dot(Coffbasic,basicvalues)

def calculateCBinverseBintob():
    return np.dot(calculateCB(Coffbasic,coffeArray,ReplacingIndexFromBasic,ReplacingIndexFromNonBasic),Binverseb(basicvalues,rightsidevalues))

calculatedValue=calculateCBinverseBintob()

print(calculatedValue)

def calBinverseA(basicvalues,nonbasicvalues):
    return np.dot(basicvalues,nonbasicvalues)

def calCBintoBinverseAminusC():
    return np.dot(calculateCB(Coffbasic,coffeArray,ReplacingIndexFromBasic,ReplacingIndexFromNonBasic),calBinverseA(basicvalues,nonbasicvalues))-coffeArray

       
print(calCBintoBinverseAminusC())