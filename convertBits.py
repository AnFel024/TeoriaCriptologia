import pandas as pd
import numpy as np
import buildSegmentsAndIntervals as bsi

bitDeSigno = 1
bitsDeSegmento = 1
bitsDeIntervalo = 3
valorDeAcopio = 0.0
dictTamSegmento = {}
dictTamIntervalo = {}

maximaExcursion, bitsDeSegmento, dictTamSegmento, bitsDeIntervalo, dictTamIntervalo, valorDeAcopio = bsi.obtainForm()
bitsCodificacion = bitDeSigno + bitsDeIntervalo + bitsDeSegmento
arraySegmento, dictIntervalo  = bsi.recursiveFun(dictTamSegmento)

df_segmentos = pd.DataFrame(arraySegmento).T
df_blanco = pd.DataFrame([" "]).T
df_intervalos = pd.DataFrame(dictIntervalo).T
df_info = pd.DataFrame(["valorDeAcopio", valorDeAcopio, "Max Excursion", maximaExcursion, "bitsCodificacion", bitsCodificacion, "bitsDeSegmento", bitsDeSegmento, "bitsDeIntervalo", bitsDeIntervalo]).T

df = pd.concat([df_segmentos, df_blanco, df_intervalos, df_blanco, df_info], sort= False)
df.to_excel(excel_writer = "./codificador_prueba.xlsx")

#chainTemp = "1010000110100001101000011010000110100001"

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

    #print(arrayBits)
    arrayBits[-1] = putZeros(arrayBits[-1], bitsCodificacion)

    return arrayBits

# Labmas que evaluan el signo del voltaje y transforman de binario a entero
getSigno = lambda bitSigno, voltaje: -voltaje if bitSigno == "0" else voltaje
getPosicion = lambda binValue: int(binValue, 2) 

# Funcion que interpreta el orden de codificacion
def castArrayByCodexOrder(chain):
    #print(chain)
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
        voltaje += round(arraySegmento[posSegmento], 10)
        
        for key in dictIntervalo.keys():
            pos = key
            if int(pos) > posSegmento:
                break

        #print(pos)
        arrayIntervalo = dictIntervalo[pos]

        voltaje += round(arrayIntervalo[getPosicion(values["Intervalo"])], 10)

        voltaje = getSigno(values["Signo"], voltaje)
        arrayVolts.append(np.round(voltaje, 10))

    return arrayVolts

def hello_world(chain):
    #print(bitsCodificacion)
    arrayBits = makeArray(chain.replace(" ", ""), bitsCodificacion)
    arrayResponse = [str(a) for a in castBitIntoArrayPosition(arrayBits)]
    print(f"El tamnaño es -> {len(arrayResponse)}")
    f= open("response.txt","w+")
    f.write(str(arrayResponse))
    f.close()

    return str.join(",", arrayResponse)
