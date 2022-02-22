import math
from random import random
import numpy as np

castRule = lambda x : x.replace(' ','').replace('(','').replace(')','').replace('X','')
formula = "47v=14(X/2)+24(1X)+34(2X)+4(3X)+6(5X)"
#formula = "1v=16(1X)"

bitsDeIntervalo = 8
tamIntervalo = 2 ** bitsDeIntervalo


def obtainForm():
    maximaExcursion = int(formula[:formula.index('=')].replace('v',''))
    arraySegmentRules = formula[formula.index('=') + 1:].split('+')
    arrayPrefixRules = []
    dictTamSegmento = {}
    dictTamIntervalo = {}
    segmentIteration = 0
    segmentRegrex = []
    
    for rule in arraySegmentRules:
        if rule[0] == 'X':
            prefixSegment = '1'
            segmentRegrex.append(int(prefixSegment))
            tempRule = '1'
        else:
            prefixSegment = str(rule[:rule.index('(')])
            segmentRegrex.append(int(prefixSegment))
            rule = rule[len(prefixSegment):]
            
            if '/' in rule:
                tempRule = castRule(rule)
                tempRule = eval('1' + tempRule)

            else:
                tempRule = castRule(rule)

            segmentIteration += eval(str(prefixSegment + '*' + str(tempRule)))
        
        arrayPrefixRules.append(tempRule) # Recordar las reglas de insercion TAL CUAL.

    valorDeAcopio = np.round(maximaExcursion / segmentIteration, 10) # Valor que se genera de despejar la X de la formula    

    #Funcion que toma las reglas de los segmentos que acompañan la X genera los valores limite para los segmentos no uniformes
    tempRegrex = 0
    flag = 0
    for rule in arrayPrefixRules:
        tempRegrex += int(segmentRegrex[flag])
        dictTamSegmento[str(tempRegrex)] = round(valorDeAcopio * float(rule), 10)
        flag+= 1

    #Funcion que genera los valores de los intervalos
    for key, value in dictTamSegmento.items():
        dictTamIntervalo[key] = round((value / tamIntervalo), 10)
    
    print(f"------------------------------> {sum(segmentRegrex)}")
    bitsDeSegmento = int(math.log2(sum(segmentRegrex)))

    return maximaExcursion, bitsDeSegmento, dictTamSegmento, bitsDeIntervalo, dictTamIntervalo, valorDeAcopio

# Funcion que crea segmentos e intervalos
def generateSegmentsAndIntervals(firstPosition, actualExcursion, tamArray, temporaryExcusrion):
    array = [0] if firstPosition else []

    for _ in range(0, tamArray):
        actualExcursion += temporaryExcusrion
        array.append(np.round(actualExcursion ,10))

    return array

def recursiveFun(dictTamSegmento):
    arraySegmento = []
    dictIntervalo = {}
    firstPosition = True
    actualExcursion = 0.0
    lastKey = 0
    for key, value in dictTamSegmento.items():
        tempArraySegmentos = generateSegmentsAndIntervals(firstPosition, actualExcursion, (int(key) - lastKey), value)
        arraySegmento += tempArraySegmentos
        dictIntervalo[key] = generateSegmentsAndIntervals(True, 0, tamIntervalo, (value/tamIntervalo))
        firstPosition = False
        actualExcursion = tempArraySegmentos[-1]
        lastKey = int(key)
    
    return arraySegmento, dictIntervalo