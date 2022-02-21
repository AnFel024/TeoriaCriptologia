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

chain = "01001110 01101111 00100000 01100101 01110011 01110100 01101111 01111001 00100000 01100110 01100101 01101100 01101001 01111010 00001010 01010000 01100101 01110010 01101111 00100000 01110100 01100001 01101101 01110000 01101111 01100011 01101111 00100000 01100101 01110011 01110100 01101111 01111001 00100000 01110100 01110010 01101001 01110011 01110100 01100101 00001010 01011001 00100000 01101110 01101111 00100000 01100101 01110011 00100000 01110001 01110101 01100101 00100000 01101110 01101111 00100000 01101101 01100101 00100000 01100001 01100110 01100101 01100011 01110100 01100101 00001010 01010100 01101111 01100100 01101111 00100000 01101100 01101111 00100000 01110001 01110101 01100101 00100000 01101101 01100101 00100000 01100100 01101001 01101010 01101001 01110011 01110100 01100101 00001010 01000101 01110011 00100000 01110001 01110101 01100101 00100000 01110011 01101001 01100101 01101110 01110100 01101111 00100000 01110001 01110101 01100101 00100000 01101110 01101111 00100000 01110000 01110101 01100101 01100100 01101111 00100000 01101100 01101100 01100101 01100111 01100001 01110010 00001010 01001000 01101001 01100011 01101001 01101101 01101111 01110011 00100000 01100001 00100000 01101100 01101111 01110011 00100000 01100100 01101001 01101111 01110011 01100101 01110011 00100000 01101001 01101101 01110000 01101111 01110011 01101001 01100010 01101100 01100101 01110011 00100000 01100100 01100101 00100000 01100001 01101100 01100011 01100001 01101110 01111010 01100001 01110010 00001010 01011001 00100000 01100001 00100000 01101100 01101111 00100000 01101101 01100101 01101010 01101111 01110010 00100000 01100101 01110011 00100000 01101101 11100001 01110011 00100000 01110011 01100101 01101110 01100011 01101001 01101100 01101100 01101111 00001010 01001100 01100001 00100000 01101101 01100001 01101110 01101111 00100000 01100101 01101110 00100000 01101100 01101111 01110011 00100000 01100010 01101111 01101100 01110011 01101001 01101100 01101100 01101111 01110011 00001010 01011001 00100000 01110101 01101110 01100001 00100000 01100011 01100001 01101110 01100011 01101001 11110011 01101110 00100000 01110011 01101001 01101100 01100010 01100001 01110010 00001010 01001110 01101111 00100000 01110011 11101001 00100000 01110000 01101111 01110010 00100000 01110001 01110101 11101001 00100000 01100101 01110011 00100000 01110001 01110101 01100101 00100000 01101101 01100101 00100000 01100011 01101111 01101101 01110000 01101100 01101001 01100011 01101111 00001010 01010011 01101001 00100000 01100001 01101100 00100000 01100110 01101001 01101110 01100001 01101100 00100000 01100100 01100101 00100000 01100011 01110101 01100101 01101110 01110100 01100001 01110011 00100000 01110011 01100101 01100111 01110101 01110010 01101111 00100000 01110011 01100001 01101100 01100101 00100000 01101101 01100001 01101100 00001010 01010001 01110101 01101001 01100101 01110010 01101111 00100000 01110110 01100101 01110010 01110100 01100101 00100000 01110000 01100001 01110011 01100001 01100100 01100001 01110011 00100000 01101100 01100001 01110011 00100000 01110100 01110010 01100101 01110011 00001010 01000001 01110101 01101110 00100000 01100100 01100101 01110011 01101110 01110101 01100100 01100001 00100000 01111001 00100000 01100101 01101110 00100000 01101100 01100001 00100000 01100011 01100001 01101101 01100001 00001010 01011001 00100000 01110001 01110101 01100101 00100000 01100100 01100101 01101010 01100101 01101101 01101111 01110011 00100000 01110100 01101111 01100100 01101111 00100000 01101100 01101111 00100000 01100100 01100101 01101101 11100001 01110011 00001010 01010000 01100001 01110010 01100001 00100000 01101101 01100001 11110001 01100001 01101110 01100001 00001010 01001101 01100001 11110001 01100001 01101110 01100001 00001010 01001110 01101111 00100000 01100101 01110011 01110100 01101111 01111001 00100000 01100110 01100101 01101100 01101001 01111010 00001010 01000001 01101100 00100000 01101101 01100101 01101110 01101111 01110011 00100000 01101110 01101111 00100000 01110100 01101111 01100100 01101111 00100000 01100101 01101100 00100000 01110100 01101001 01100101 01101101 01110000 01101111 00001010 01000100 01100101 01110011 01100011 01101111 01101110 01100110 11101101 01101111 00100000 01100100 01100101 01101100 00100000 01110000 01110010 01101111 01100110 01100101 01110100 01100001 00001010 01010001 01110101 01100101 00100000 01100100 01101001 01100011 01100101 00100000 01110011 01101001 01100101 01101101 01110000 01110010 01100101 00100000 01100101 01110011 01110100 01100001 01110010 00100000 01100011 01101111 01101110 01110100 01100101 01101110 01110100 01101111 00001010 01000101 01110011 00100000 01110001 01110101 01100101 00100000 01110011 01101001 00100000 01100101 01110011 01110100 01100101 00100000 01101101 01110101 01101110 01100100 01101111 00100000 01101000 01100001 00100000 01100100 01100101 00100000 01100111 01101001 01110010 01100001 01110010 00001010 01000100 01100101 00100000 01110101 01101110 00100000 01101100 01100001 01100100 01101111 00100000 01110011 01100101 01110010 11100001 00100000 01100100 01100101 00100000 01100100 11101101 01100001 00001010 01011001 00100000 01100100 01100101 01101100 00100000 01101111 01110100 01110010 01101111 00100000 01101111 01110011 01100011 01110101 01110010 01101001 01100100 01100001 01100100 00001010 01011001 01101111 00100000 01111001 01100001 00100000 01110011 11101001 00100000 01110001 01110101 01100101 00100000 01101110 01101111 00100000 01101000 01100001 01111001 00100000 01110011 01100101 01101110 01110100 01101001 01100100 01101111 00001010 01000100 01100001 00100000 01101001 01100111 01110101 01100001 01101100 00100000 01110011 01101001 00100000 01101100 01101100 01101111 01110010 01101111 00100000 01101111 00100000 01110010 11101101 01101111 00001010 01010000 01100101 01110010 01101111 00100000 01110000 01110010 01100101 01100110 01101001 01100101 01110010 01101111 00100000 01110010 01100101 01101001 01110010 00001010 01011001 00100000 01100011 01110101 01100001 01101110 01100100 01101111 00100000 01101101 01100001 11110001 01100001 01101110 01100001 00100000 01101100 01101100 01101111 01110010 01100101 00001010 01000001 11111010 01101110 00100000 01101101 01100101 00100000 01110001 01110101 01100101 01100100 01100001 01110010 11100001 01101110 00100000 01101100 01100001 01110011 00100000 01100110 01101100 01101111 01110010 01100101 01110011 00001010 01010001 01110101 01100101 00100000 01100100 01100101 01101010 01100001 01101101 01101111 01110011 00100000 01101101 01101111 01110010 01101001 01110010 00001010 01000100 01100101 00100000 01100001 00100000 01100100 01101111 01110011 00001010 01000001 01101000 00100000 01100001 01101000 00100000 01100001 01101000 00001010 01011001 01101111 00100000 01111001 01100001 00100000 01110011 11101001 00100000 01110001 01110101 01100101 00100000 01101110 01101111 00100000 01101000 01100001 01111001 00100000 01110011 01100101 01101110 01110100 01101001 01100100 01101111 00001010 00101000 01111001 01101111 00100000 01111001 01100001 00100000 01110011 01100101 00101001 00001010 01011001 00100000 01110001 01110101 01100101 00100000 01101110 01101001 00100000 01101101 01101001 00100000 01100011 01110101 01100101 01110010 01110000 01101111 00100000 01100101 01110011 00100000 01101101 11101101 01101111 00001010 00101000 01101101 01101001 00100000 01100011 01110101 01100101 01110010 01110000 01101111 00100000 01100101 01110011 00100000 01101101 11101101 01101111 00101001 00001010 01001100 01101111 00100000 01101000 01100001 01100010 01110010 11101001 00100000 01100100 01100101 00100000 01100100 01100101 01110110 01101111 01101100 01110110 01100101 01110010 00001010 01011001 00100000 01100011 01110101 01100001 01101110 01100100 01101111 00100000 01101101 01100001 11110001 01100001 01101110 01100001 00100000 01101100 01101100 01101111 01110010 01100101 01110011 00001010 01000001 11111010 01101110 00100000 01110100 01100101 00100000 01110001 01110101 01100101 01100100 01100001 01110010 11100001 01101110 00100000 01101100 01100001 01110011 00100000 01100110 01101100 01101111 01110010 01100101 01110011 00001010 01010001 01110101 01100101 00100000 01100100 01100101 01101010 01100001 01101101 01101111 01110011 00100000 01110110 01101001 01110110 01101001 01110010 00001010 01001100 01101111 01110011 00100000 01100100 01101111 01110011 00001010 01011001 00100000 01100001 00100000 01101100 01101111 00100000 01101101 01100101 01101010 01101111 01110010 00100000 01100101 01110011 00100000 01101101 11100001 01110011 00100000 01110011 01100101 01101110 01100011 01101001 01101100 01101100 01101111 00001010 01001100 01100001 01110011 00100000 01101101 01100001 01101110 01101111 00100000 01100101 01101110 00100000 01101100 01101111 01110011 00100000 01100010 01101111 01101100 01110011 01101001 01101100 01101100 01101111 00001010 01011001 00100000 01110101 01101110 01100001 00100000 01100011 01100001 01101110 01100011 01101001 11110011 01101110 00100000 01110011 01101001 01101100 01100010 01100001 01110010 00001010 01001110 01101111 00100000 01110011 11101001 00100000 01110000 01101111 01110010 00100000 01110001 01110101 11101001 00100000 01100101 01110011 00100000 01110001 01110101 01100101 00100000 01101101 01100101 00100000 01100011 01101111 01101101 01110000 01101100 01101001 01100011 01101111 00001010 01010011 01101001 00100000 01100001 01101100 00100000 01100110 01101001 01101110 01100001 01101100 00100000 01100100 01100101 00100000 01100011 01110101 01100101 01101110 01110100 01100001 01110011 00001010 01010011 01100101 01100111 01110101 01110010 01101111 00100000 01101101 01100001 01101100 01100101 00100000 01110011 01100001 01101100 00001010 01010001 01110101 01101001 01100101 01110010 01101111 00100000 01110110 01100101 01110010 01110100 01100101 00100000 01110000 01100001 01110011 01100001 01100100 01100001 01110011 00100000 01101100 01100001 01110011 00100000 01110100 01110010 01100101 01110011 00001010 01000001 11111010 01101110 00100000 01100100 01100101 01110011 01101110 01110101 01100100 01100001 00100000 01111001 00100000 01100101 01101110 00100000 01101100 01100001 00100000 01100011 01100001 01101101 01100001 00001010 01011001 00100000 01110001 01110101 01100101 00100000 01100100 01100101 01101010 01100101 01101101 01101111 01110011 00100000 01110100 01101111 01100100 01101111 00100000 01101100 01101111 00100000 01100100 01100101 01101101 11100001 01110011 00001010 01011001 00100000 01110001 01110101 01100101 00100000 01100100 01100101 01101010 01100101 01101101 01101111 01110011 00100000 01110100 01101111 01100100 01101111 00100000 01101100 01101111 00100000 01100100 01100101 01101101 11100001 01110011 00001010 01010000 01100001 01110010 01100001 00100000 01101101 01100001 11110001 01100001 01101110 01100001 00001010 01010000 01100001 01110010 01100001 00100000 01101101 01100001 11110001 01100001 01101110 01100001 00001010 00101000 01110101 01101110 01100001 00100000 01100011 01100001 01101110 01100011 01101001 11110011 01101110 00100000 01110011 01101001 01101100 01100010 01100001 01110010 00101001 00001010 01011001 00100000 01100001 00100000 01101100 01101111 00100000 01101101 01100101 01101010 01101111 01110010 00100000 01100101 01110011 00100000 01101101 11100001 01110011 00100000 01110011 01100101 01101110 01100011 01101001 01101100 01101100 01101111 00001010 00101000 01010000 01100001 01110010 01100001 00100000 01101101 01100001 11110001 01100001 01101110 01100001 00101001 00001010 01011001 00100000 01100001 00100000 01101100 01101111 00100000 01101101 01100101 01101010 01101111 01110010 00100000 01100101 01110011 00100000 01101101 11100001 01110011 00100000 01110011 01100101 01101110 01100011 01101001 01101100 01101100 01101111 00001010 00101000 01010001 01110101 01101001 01100101 01110010 01101111 00100000 01110110 01100101 01110010 01110100 01100101 00101001 00001010 01011001 00100000 01100001 00100000 01101100 01101111 00100000 01101101 01100101 01101010 01101111 01110010 00100000 01100101 01110011 00100000 01101101 11100001 01110011 00100000 01110011 01100101 01101110 01100011 01101001 01101100 01101100 01101111 00001010 00101000 01010001 01110101 01101001 01100101 01110010 01101111 00100000 01110110 01100101 01110010 01110100 01100101 00101001 00001010 01011001 00100000 01100001 00100000 01101100 01101111 00100000 01101101 01100101 01101010 01101111 01110010 00100000 01100101 01110011 00100000 01101101 11100001 01110011 00100000 01110011 01100101 01101110 01100011 01101001 01101100 01101100 01101111 00001010 00101000 01010101 01101110 01100001 00100000 01100011 01100001 01101110 01100011 01101001 11110011 01101110 00100000 01110011 01101001 01101100 01100010 01100001 01110010 00101001 00001010 01011001 00100000 01100001 00100000 01101100 01101111 00100000 01101101 01100101 01101010 01101111 01110010 00100000 01100101 01110011 00100000 01101101 11100001 01110011 00100000 01110011 01100101 01101110 01100011 01101001 01101100 01101100 01101111 00001010 00101000 01101110 01101111 00100000 01110001 01110101 01100101 01100100 01100001 01110010 11100001 01101110 00100000 01101100 01100001 01110011 00100000 01100110 01101100 01101111 01110010 01100101 01110011 00101001 00001010 00101000 01010001 01110101 01101001 01100101 01110010 01101111 00100000 01110110 01100101 01110010 01110100 01100101 00101001 00001010 01011001 00100000 01100001 00100000 01101100 01101111 00100000 01101101 01100101 01101010 01101111 01110010 00100000 01100101 01110011 00100000 01101101 11100001 01110011 00100000 01110011 01100101 01101110 01100011 01101001 01101100 01101100 01101111 00001010 01010011 01101001 00100000 01100101 01110011 00100000 01100100 01100101 00100000 01100001 00100000 01100100 01101111 01110011 00001010 01011001 00100000 01100001 00100000 01101100 01101111 00100000 01101101 01100101 01101010 01101111 01110010 00100000 01100101 01110011 00100000 01101101 11100001 01110011 00100000 01110011 01100101 01101110 01100011 01101001 01101100 01101100 01101111 00001010 01010011 01101001 00100000 01100101 01110011 00100000 01100100 01100101 00100000 01100001 00100000 01100100 01101111 01110011 00001010 01011001 00100000 01100001 00100000 01101100 01101111 00100000 01101101 01100101 01101010 01101111 01110010 00100000 01100101 01110011 00100000 01101101 11100001 01110011 00100000 01110011 01100101 01101110 01100011 01101001 01101100 01101100 01101111 00001010 01010011 01101001 00100000 01100101 01110011 00100000 01100100 01100101 00100000 01100001 00100000 01100100 01101111 01110011 00001010 01011001 00100000 01100001 00100000 01101100 01101111 00100000 01101101 01100101 01101010 01101111 01110010 00100000 01100101 01110011 00100000 01101101 11100001 01110011 00100000 01110011 01100101 01101110 01100011 01101001 01101100 01101100 01101111 00001010 01010011 01101001 00100000 01100101 01110011 00100000 01100100 01100101 00100000 01100001 00100000 01100100 01101111 01110011 00001010 01011001 00100000 01100001 00100000 01101100 01101111 00100000 01101101 01100101 01101010 01101111 01110010 00100000 01100101 01110011 00100000 01101101 11100001 01110011 00100000 01110011 01100101 01101110 01100011 01101001 01101100 01101100 01101111 00001010 01010011 01101001 00100000 01100101 01110011 00100000 01100100 01100101 00100000 01100001 00100000 01100100 01101111 01110011 00001010 01011001 00100000 01100001 00100000 01101100 01101111 00100000 01101101 01100101 01101010 01101111 01110010 00100000 01100101 01110011 00100000 01101101 11100001 01110011 00100000 01110011 01100101 01101110 01100011 01101001 01101100 01101100 01101111 00001010 01010011 01101001 00100000 01100101 01110011 00100000 01100100 01100101 00100000 01100001 00100000 01100100 01101111 01110011 00001010 01011001 00100000 01100001 00100000 01101100 01101111 00100000 01101101 01100101 01101010 01101111 01110010 00100000 01100101 01110011 00100000 01101101 11100001 01110011 00100000 01110011 01100101 01101110 01100011 01101001 01101100 01101100 01101111 00001010 01010011 01101001 00100000 01100101 01110011 00100000 01100100 01100101 00100000 01100001 00100000 01100100 01101111 01110011 00001010 01011001 00100000 01100001 00100000 01101100 01101111 00100000 01101101 01100101 01101010 01101111 01110010 00100000 01100101 01110011 00100000 01101101 11100001 01110011 00100000 01110011 01100101 01101110 01100011 01101001 01101100 01101100 01101111 00001010 01010011 01101001 00100000 01100101 01110011 00100000 01100100 01100101 00100000 01100001 00100000 01100100 01101111 01110011 "

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

def hello_world():
    #print(bitsCodificacion)
    arrayBits = makeArray(chain.replace(" ", ""), bitsCodificacion)
    arrayResponse = [str(a) for a in castBitIntoArrayPosition(arrayBits)]
    
    return str.join(",", arrayResponse)
