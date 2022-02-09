import math

castRule = lambda x : x.replace(' ','').replace('(','').replace(')','').replace('X','')

def obtainForm(formula, tamIntervalo):
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
            rule = rule.replace(str(prefixSegment),'')
            if '/' in rule:
                tempRule = castRule(rule)
                tempRule = eval('1' + tempRule)

            else:
                tempRule = castRule(rule)
            
            segmentIteration += eval(str(prefixSegment + '*' + str(tempRule)))
        
        arrayPrefixRules.append(tempRule) # Recordar las reglas de insercion TAL CUAL.

    valorDeAcopio = maximaExcursion / segmentIteration
    
    tempRegrex = 0
    flag = 0
    for rule in arrayPrefixRules:
        tempRegrex += int(segmentRegrex[flag])
        dictTamSegmento[str(tempRegrex)] = valorDeAcopio * float(rule)
        flag+= 1

    for key, value in dictTamSegmento.items():
        dictTamIntervalo[key] = value / tamIntervalo
    
    bitsDeSegmento = int(math.log2(sum(segmentRegrex)))

    print(bitsDeSegmento)

    return maximaExcursion, bitsDeSegmento, dictTamSegmento, dictTamIntervalo, valorDeAcopio


# Funcion que crea segmentos e intervalos
def generateSegmentsAndIntervals(firstPosition, actualExcursion, tamArray, temporaryExcusrion):
    array = [0] if firstPosition else []

    for _ in range(0, tamArray):
        actualExcursion += temporaryExcusrion
        array.append(actualExcursion)
        # Buscar lib para crear excel

    return array

def recursiveFun(dictTamSegmento, tamIntervalo):
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