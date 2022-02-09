import buildSegmentsAndIntervals as bsi

maximaExcursion = 0

bitDeSigno = 1
bitsDeSegmento = 1
bitsDeIntervalo = 3
valorDeAcopio = 0.0
dictTamSegmento = {}
dictTamIntervalo = {}

formula = "5v=4(X/2)+4(1X)+4(2X)+4(3X)"
#formula = "1v=16(1X)"

tamIntervalo = 2 ** bitsDeIntervalo
maximaExcursion, bitsDeSegmento, dictTamSegmento, dictTamIntervalo, valorDeAcopio = bsi.obtainForm(formula, tamIntervalo)
tamSegmento = 2 ** bitsDeSegmento
bitsCodificacion = bitDeSigno + bitsDeIntervalo + bitsDeSegmento
arraySegmento, dictIntervalo  = bsi.recursiveFun(dictTamSegmento, tamIntervalo)

chain = "-0.5048076923076923"

arrayOrder = ["Signo", "Segmento", "Intervalo"]

# Funcion que rellena los zeros faltantes en la ultima posicion
def putZerosBefore(chain, bits):
    zeros = ""
    for _ in range(len(chain), bits):
        zeros += "0"
    zeros += chain
    
    return zeros

# Funcion que borra los zeros de la ultima posicion
# Esto para limpiar la codificacion
def dropZerosAfter(chain):
    return chain[:chain.rfind('1')+1]

getBitSigno = lambda x: "0" if (str(x)[0] == "-") else "1"
convertIntToBin = lambda x: format(x, 'b')

# Funcion que itera sobre los voltajes
def makeChain(arrayChain):
    volBinChain = ""
    arrayBins = []

    for volt in arrayChain:
        volBinChain = getBitSigno(volt)
        intSegment = int(abs(volt) / dictTamSegmento) # Dividimos el voltaje entre el tamaño del segmento
        tempBinSegment = convertIntToBin(intSegment)
        binSegment = putZerosBefore(tempBinSegment, bitsDeSegmento)

        volInterval = abs(volt) - arraySegmento[intSegment] # Restamos el tamaño del segmento por el voltaje y obtenemos el intervalo
        intInterval = int(abs(volInterval) / dictTamSegmento) # Dividimos el voltaje restante entre el tamaño del intervalo
        tempBinInterval = convertIntToBin(intInterval)
        binInterval = putZerosBefore(tempBinInterval, bitsDeIntervalo)

        if arrayOrder[1] == "Segmento":
            volBinChain += (str(binSegment) + str(binInterval))
        elif arrayOrder[1] == "Intervalo":
            volBinChain += (str(binInterval) + str(binSegment))

        arrayBins.append(volBinChain)
        
    arrayBins[-1] = dropZerosAfter(arrayBins[-1])

    return arrayBins


def good_bye_world():
    arrayVolts = chain.split(",")
    arrayChain = [float(value) for value in arrayVolts]

    response = str.join(" ", makeChain(arrayChain))

    #return response + " | " + responseAS + " | " + responseAI

    return response


# Funcion que crea segmentos e intervalos
def generateSegmentsAndIntervals(tamArray, temporaryExcusrion):
    array = [0]
    actualExcursion = 0.0

    for _ in range(0, tamArray):
        actualExcursion += temporaryExcusrion
        array.append(actualExcursion)
        # Buscar lib para crear excel

    return array
