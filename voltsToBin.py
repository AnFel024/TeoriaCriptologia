import pandas as pd
import buildSegmentsAndIntervals as bsi

maximaExcursion = 0

bitDeSigno = 1
bitsDeSegmento = 1
bitsDeIntervalo = 3
valorDeAcopio = 0.0
dictTamSegmento = {}
dictTamIntervalo = {}

maximaExcursion, bitsDeSegmento, dictTamSegmento, dictTamIntervalo, valorDeAcopio = bsi.obtainForm()
bitsCodificacion = bitDeSigno + bitsDeIntervalo + bitsDeSegmento
arraySegmento, dictIntervalo  = bsi.recursiveFun(dictTamSegmento)

df_segmentos = pd.DataFrame(arraySegmento).T
df_blanco = pd.DataFrame([" "]).T
df_intervalos = pd.DataFrame(dictIntervalo).T
df_info = pd.DataFrame(["valorDeAcopio", valorDeAcopio, "Max Excursion", maximaExcursion]).T

df = pd.concat([df_segmentos, df_blanco, df_intervalos, df_blanco, df_info], sort= False)
df.to_excel(excel_writer = "./codificador_prueba.xlsx")

chain = "-1.25,-2.9375,-2.75,-2.0625,-0.5,-2.0625,-0.5,-3.5,-2.9375,-2.25,-2.9375,-3.375,-0.6875,-0.5,-2.3125,-3.375,-3.5,-2.9375,-0.5,-2.3125,-3.375,-0.5,-3.625,-2.875,-2.0625,-0.5,-3.0,-3.25,-3.625,-2.3125,-2.125,-2.5625,-2.875,-2.5,2.0625,-0.5,-3.375,-2.9375,-2.125,-3.25,-2.3125,-0.5,-2.5,-2.3125,-3.25,-3.25,-2.9375,-3.25,-2.3125,-3.375,-0.5,-2.25,-2.3125,-0.5,-2.9375,-3.5,-3.25,-2.9375,0.8125,-2.4375,-3.25,2.0625,-2.375,-2.5625,-2.0625,-0.5,-3.125,-2.9375,-2.25,-2.5625,-2.375,-2.5625,-2.6875,-2.0625,-2.25,-2.9375,-4.25,-0.71875"

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

def searchInArray(valueToSearhc, minPosition):
    if valueToSearhc >= arraySegmento[minPosition] and valueToSearhc < arraySegmento[minPosition + 1]:
        return minPosition
    
    return searchInArray(valueToSearhc, minPosition + 1)

def searchInMeta(requestValue : float):
    tempKey= 0.0
    lastValue = 0.0
    presentValue = 0.0
    for key, value in dictTamSegmento.items():
        floatKey = float(key)
        result = (floatKey - tempKey) * value
        presentValue += result

        if requestValue == 0:
            return 0, key
        
        elif requestValue >= lastValue and requestValue < presentValue:
            response = searchInArray(requestValue, int(tempKey))
            return response, key

        elif requestValue == 5.0:
            return len(arraySegmento) - 2, key

        lastValue = presentValue
        tempKey = floatKey

# Funcion que itera sobre los voltajes
def makeChain(arrayChain):
    volBinChain = ""
    arrayBins = []

    for volt in arrayChain:
        volBinChain = getBitSigno(volt)
        volt = abs(volt)

        intSegmento, keyIntervals = searchInMeta(volt)
        tempBinSegment = convertIntToBin(intSegmento)
        binSegment = putZerosBefore(tempBinSegment, bitsDeSegmento)

        volInterval = volt - arraySegmento[intSegmento] # Restamos el tamaño del segmento por el voltaje y obtenemos el intervalo
        intInterval = int(abs(volInterval) / dictTamIntervalo[keyIntervals]) # Dividimos el voltaje restante entre el tamaño del intervalo
     
        tempBinInterval = convertIntToBin(intInterval)
        binInterval = putZerosBefore(tempBinInterval, bitsDeIntervalo)

        if arrayOrder[1] == "Segmento":
            volBinChain += (str(binSegment) + str(binInterval))
        elif arrayOrder[1] == "Intervalo":
            volBinChain += (str(binInterval) + str(binSegment))

        arrayBins.append(volBinChain)
        
    #arrayBins[-1] = dropZerosAfter(arrayBins[-1])

    return arrayBins


def good_bye_world():
    arrayVolts = chain.split(",")
    arrayChain = [float(value) for value in arrayVolts]

    response = str.join(" ", makeChain(arrayChain))

    #return response + " | " + responseAS + " | " + responseAI

    return response
