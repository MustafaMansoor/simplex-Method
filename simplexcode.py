import numpy as np
coffevariables = [3, 5]
coffeArray = coffevariables
tempcoffeArray = [-coff for coff in coffevariables]
sizeOfCoffeArray = len(coffeArray)
numOfCons = 3

Coffbasic = [0] * numOfCons


SmallbValues = [4, 12, 18]

rightsidevalues = SmallbValues
calculatedValue = 0

AmetrixValues = [[0] * sizeOfCoffeArray for _ in range(numOfCons)]

AmetrixValues[0][0] = 1
AmetrixValues[0][1] = 0
AmetrixValues[1][0] = 0
AmetrixValues[1][1] = 2
AmetrixValues[2][0] = 3
AmetrixValues[2][1] = 2

nonbasicvalues=AmetrixValues

CapitalBValues = [[1 if i == j else 0 for j in range(numOfCons)] for i in range(numOfCons)]


basicvalues=CapitalBValues

while any(coff < 0 for coff in tempcoffeArray):

    def getmaxCoffIndex(coffeArray):
        return coffeArray.index(max(coffeArray))


    def calratiotest(nonbasicvalues, SmallbValues, ReplacingIndexFromNonBasic):
        ratios = []

        for i in range(len(nonbasicvalues)):
            if nonbasicvalues[i][ReplacingIndexFromNonBasic] > 0:
                ratio = SmallbValues[i] / nonbasicvalues[i][ReplacingIndexFromNonBasic]
                ratios.append(ratio)
            else:
                ratios.append(float("inf"))
        min_ratio = ratios.index(min(ratios))
        return min_ratio



    ReplacingIndexFromNonBasic=getmaxCoffIndex(coffeArray)
    print("ReplacingIndexFromNonBasic")
    print(ReplacingIndexFromNonBasic)
    ReplacingIndexFromBasic=calratiotest(nonbasicvalues,SmallbValues,ReplacingIndexFromNonBasic)
    print("ReplacingIndexFromNonBasic")
    print(ReplacingIndexFromBasic)
    def replaceColumnInBasicValues(basicvalues, nonbasicvalues, replacingIndexFromNonBasic, replacingIndexFromBasic):
        # Convert the input lists to NumPy arrays
        basicvalues = np.array(basicvalues)
        nonbasicvalues = np.array(nonbasicvalues)

        if len(nonbasicvalues) != len(basicvalues):
            raise ValueError("Both matrices must have the same number of rows for replacement.")
        
        basicvalues[:, replacingIndexFromBasic] = nonbasicvalues[:, replacingIndexFromNonBasic]
        return basicvalues

    basicvalues=replaceColumnInBasicValues(basicvalues, nonbasicvalues, ReplacingIndexFromNonBasic, ReplacingIndexFromBasic)

    print("basicvalues")
    print(basicvalues)

    inversebasicvalues=np.linalg.inv(basicvalues)
    
    print("inversebasicvalues")
    print(inversebasicvalues)

    def Binverseb(inversebasicvalues,rightsidevalues):
        return np.dot(inversebasicvalues,rightsidevalues)

    
    SmallbValues=Binverseb(inversebasicvalues,rightsidevalues)
    print("SmallbValues")
    print(SmallbValues)
    def calculateCB(Coffbasic,coffeArray,ReplacingIndexFromBasic,ReplacingIndexFromNonBasic):
        Coffbasic[ReplacingIndexFromBasic]=coffeArray[ReplacingIndexFromNonBasic]
        return Coffbasic
    Coffbasic=calculateCB(Coffbasic,coffeArray,ReplacingIndexFromBasic,ReplacingIndexFromNonBasic)

    print("Coffbasic")
    print(Coffbasic)


    def calculateCBinverseB(SmallbValues,Coffbasic):
        return np.dot(Coffbasic,SmallbValues)

    def calculateCBinverseBintob():
        return np.dot(Coffbasic,SmallbValues)

    calculatedValue=calculateCBinverseBintob()

    print("calculatedValue")
    print(calculatedValue)

    def calBinverseA(inversebasicvalues,nonbasicvalues):
        return np.dot(inversebasicvalues,nonbasicvalues)

    def calCBintoBinverseAminusC():
        return np.dot(calculateCB(Coffbasic,coffeArray,ReplacingIndexFromBasic,ReplacingIndexFromNonBasic),calBinverseA(inversebasicvalues,nonbasicvalues))-coffevariables

        
    tempcoffeArray=calCBintoBinverseAminusC()
    
    coffeArray = [abs(value) for value in tempcoffeArray]

    print("coffeArray")
    print(coffeArray)

    print("tempcoffeArray")
    print(tempcoffeArray)
    print()