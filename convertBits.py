import buildSegmentsAndIntervals as bsi

bitDeSigno = 1
bitsDeSegmento = 1
bitsDeIntervalo = 3
valorDeAcopio = 0.0
dictTamSegmento = {}
dictTamIntervalo = {}

maximaExcursion, bitsDeSegmento, dictTamSegmento, dictTamIntervalo, valorDeAcopio = bsi.obtainForm()
bitsCodificacion = bitDeSigno + bitsDeIntervalo + bitsDeSegmento
arraySegmento, dictIntervalo  = bsi.recursiveFun(dictTamSegmento)

chain = "01001000 01101111 01101100 01100001 00100000 01100001 00100000 01110100 01101111 01100100 01101111 01110011 00101100 00100000 01100101 01110011 01110100 01101111 00100000 01100101 01110011 00100000 01110101 01101110 01100001 00100000 01110000 01110010 01110101 01100101 01100010 01101001 01101110 01101000 11100001 00100000 01110011 01101111 01100010 01110010 01100101 00100000 01101000 01100101 01110010 01110010 01101111 01110010 01100101 01110011 00100000 01100100 01100101 00100000 01101111 01110100 01110010 01101111 10110100 01100111 01110010 11100001 01100110 01101001 01100001 00100000 01110001 01101111 01100100 01101001 01100110 01101001 01101011 01100001 01100100 01101111 01111010 00101110 "

arrayOrder = ["Signo", "Segmento", "Intervalo"]

# Funcion que rellena los zeros faltantes en la ultima posicion
def putZeros(chain, bitsCodificacion):
    zeros = ""
    for _ in range(len(chain), bitsCodificacion):
        zeros += "0"
    chain += zeros
    
    return chain 

# Funcion que crea el arreglo de binarios
def makeArray(chain, bitsCodificacion):
    tam = 0
    arrayBits = []
    while tam < len(chain):
        bitChain = ""
        for i in range(0, bitsCodificacion):
            if tam >= len(chain):
                break
            bitChain += chain[tam]
            tam+= 1
        arrayBits.append(bitChain)

    arrayBits[-1] = putZeros(arrayBits[-1], bitsCodificacion)

    return arrayBits

# Labmas que evaluan el signo del voltaje y transforman de binario a entero
getSigno = lambda bitSigno, voltaje: -voltaje if bitSigno == "0" else voltaje
getPosicion = lambda binValue: int(binValue, 2) 

# Funcion que interpreta el orden de codificacion
def castArrayByCodexOrder(chain):
    print(chain)
    dictValue = {"Signo" : chain[0]}
    if arrayOrder[1] == "Segmento":
        dictValue["Segmento"] = chain[bitDeSigno:bitsDeSegmento+1]
        dictValue["Intervalo"] = chain[bitsDeSegmento+1:]
    
    elif arrayOrder[1] == "Intervalo":
        dictValue["Intervalo"] = chain[bitDeSigno:bitsDeIntervalo+1]
        dictValue["Segmento"] = chain[bitsDeIntervalo+1:]
    
    return dictValue

# Convierte las posiciones de la cadena en valores enteros (p.e. 0 111 0001 -> 0,7,1) 
# Luego, va creando el voltaje
def castBitIntoArrayPosition(arrayBits):
    arrayVolts = []
    for chainBits in arrayBits:
        voltaje = 0.0
        values = castArrayByCodexOrder(chainBits)

        posSegmento = getPosicion(values["Segmento"])
        voltaje += arraySegmento[posSegmento]
        
        for key in dictIntervalo.keys():
            pos = key
            if int(pos) > posSegmento:
                break

        print(pos)
        arrayIntervalo = dictIntervalo[pos]
        voltaje += arrayIntervalo[getPosicion(values["Intervalo"])]

        voltaje = getSigno(values["Signo"], voltaje)
        arrayVolts.append(voltaje)

    return arrayVolts

def hello_world():
    arrayBits = makeArray(chain.replace(" ", ""), bitsCodificacion)

    arrayResponse = [str(a) for a in castBitIntoArrayPosition(arrayBits)]
    
    return str.join(",", arrayResponse)
