import pandas as pd
import numpy  as np
import buildSegmentsAndIntervals as bsi

maximaExcursion = 0

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

chain = "-1.826923077,2.5961538462,0.0180288462,-0.6610576925,-0.9375000002,0.1622596155,2.5961538462,0.1923076924,-3.1250000001,1.6586538463,0.8052884617,-1.7067307694,0.3966346156,-1.6346153848,-0.3004807694,0.9855769232,-3.7740384616,-1.1778846155,1.9951923078,-0.1322115385,2.2596153847,-0.1622596155,2.3317307693,0.9495192309,-0.3846153848,1.6586538463,1.8028846155,0.4567307694,4.3870192308,-0.480769231,-0.3485576925,-0.9855769232,-3.3413461539,3.1610576924,1.9951923078,-0.5769230771,0.5168269233,-0.480769231,-0.3305288463,-0.9495192309,-0.3846153848,1.6586538463,1.7548076924,-0.0420673077,-0.2764423078,0.685096154,-1.5384615386,-0.9375000002,-3.7740384616,-1.1778846155,0.9014423079,-0.6009615386,-0.0721153846,-0.685096154,0.3004807694,0.8052884617,-4.1346153846,1.6346153848,-0.6009615386,0.4567307694,4.2788461539,0.1622596155,1.5384615386,-0.9134615386,-3.7740384616,-1.1778846155,1.4182692309,0.6490384617,-2.0192307694,-0.1622596155,-2.3557692309,0.1923076924,-2.9807692308,2.0432692309,0.6129807694,-1.7067307694,-0.9375000002,0.1502403847,-1.2740384617,-0.4447115386,-4.0625,-1.1778846155,1.4182692309,0.6490384617,-2.0192307694,-0.1682692308,2.403846154,0.8293269232,-3.701923077,3.3052884616,1.0697115386,-0.0420673077,-0.2764423078,0.685096154,-1.5384615386,-0.9375000002,-3.7740384616,-1.1778846155,1.2259615386,0.6490384617,-2.2115384616,0.1622596155,1.5384615386,-0.9134615386,-3.5576923077,1.6586538463,0.3545673079,-0.1382211539,-0.3966346156,-1.5865384617,-0.3125000002,0.8052884617,-3.3413461539,2.4278846155,1.0937500002,0.3004807694,-0.0721153846,-0.480769231,-0.3245192309,-0.9495192309,-4.0625,-1.1778846155,0.2103365386,-1.6826923078,4.3509615385,-3.5937500001,-2.5240384616,0.1923076924,-3.3413461539,2.4278846155,1.2259615386,-4.6754807692,-0.9254807694,-0.6730769233,0.3245192309,-0.8293269232,-4.0625,-1.1778846155,0.2103365386,-0.6009615386,-0.0721153846,-0.7091346156,-0.294471154,0.7812500002,-3.701923077,4.170673077,0.0661057693,0.1923076924,0.5168269233,-0.480769231,-0.2884615386,0.1923076924,-3.5576923077,2.5961538462,0.0180288462,-3.4855769231,-2.2355769232,-1.8028846155,2.5240384616,-0.1923076924,-3.0528846155,3.1250000001,0.0180288462,-3.7740384616,-0.2764423078,-2.9807692308,-0.3425480771,0.8293269232,-3.701923077,1.466346154,0.5168269233,-2.9086538462,1.466346154,2.764423077,0.2283653847,-0.7812500002,-0.3846153848,2.4278846155,0.0661057693,-4.0625,3.9903846154,-0.1502403847,-2.4759615386,-0.1923076924,-3.5576923077,2.6201923078,1.7548076924,-0.0360576923,-0.5408653848,3.6658653847,-0.3425480771,0.8774038463,-3.5576923077,2.3317307693,1.0937500002,0.2884615386,0.5168269233,-0.480769231,-0.3485576925,0.9375000002,-2.764423077,-1.1778846155,0.1622596155,-0.1322115385,3.1250000001,-3.6298076924,-4.7475961539,0.9375000002,-0.3846153848,3.1610576924,0.5168269233,-2.9086538462,-0.528846154,-0.7211538463,0.0300480769,-0.5528846156,-3.7740384616,-1.1778846155,1.8990384617,-1.5865384617,-0.0841346154,-0.1622596155,2.5240384616,-0.1923076924,-3.9182692308,3.5216346154,0.4927884617,-0.0360576923,-2.2596153847,-2.9807692308,-0.3365384617,1.0216346155,-3.0528846155,-1.1778846155,0.9014423079,-0.6009615386,-0.0721153846,-3.6658653847,2.451923077,0.9615384617,-3.5576923077,2.0432692309,0.1622596155,-4.4230769231,0.5048076925,-3.6298076924,-1.5384615386,-0.7812500002,-3.5576923077,-1.1778846155,0.3064903848,-1.6826923078,3.1250000001,-0.7091346156,-0.0961538462,-0.8173076925,-3.0528846155,-1.1778846155,0.1622596155,0.6490384617,-2.2355769232,1.8509615386,-0.2884615386,0.997596154,-0.3846153848,3.1610576924,0.2584134617,-1.0456730771,-2.2596153847,-1.8028846155,1.5384615386,-0.997596154,-2.764423077,2.3317307693,0.2463942309,-0.0360576923,2.2115384616,-0.7091346156,-0.0300480769,-0.5889423079,-4.2067307693,2.0432692309,0.2584134617,0.2283653847,3.9903846154,-0.1742788462,0.3004807694,0.9855769232,-4.1346153846,1.6346153848,0.0180288462,0.0360576923,-0.2764423078,-3.5576923077,-2.3557692309,-0.7812500002,-4.0625,-1.1778846155,0.8052884617,-0.1382211539,-0.8173076925,-0.1742788462,-0.3425480771,-0.8293269232,-4.0625,-0.2463942309,-0.0661057693,0.6490384617,2.8365384616,-0.1502403847,-0.3004807694,0.997596154,-3.701923077,3.4495192308,0.2103365386,-0.108173077,-0.0901442308,-0.480769231,-0.3004807694,0.9375000002,-0.3846153848,2.3317307693,0.0540865385,-0.0360576923,-0.9134615386,-0.7091346156,-2.3076923078,0.0600961539,-2.3557692309,-1.1778846155,1.4182692309,0.6490384617,-2.0192307694,-0.1502403847,-0.3004807694,0.8894230771,-3.0528846155,2.4278846155,1.0937500002,0.3004807694,-0.0841346154,0.1622596155,2.3557692309,-0.9495192309,-0.3846153848,2.3317307693,1.0697115386,-0.0360576923,-1.4423076924,0.7091346156,-4.4230769231,0.997596154,-0.1201923078,0.3966346156,0.0661057693,0.2283653847,-0.216346154,-0.1622596155,-2.3076923078,4.4591346154,-2.764423077,2.5240384616,0.0480769231,-2.0192307694,2.2115384616,-1.1057692309,-2.3076923078,0.9375000002,-2.764423077,-0.2463942309,-0.997596154,-4.4951923077,-0.0721153846,0.7211538463,2.5480769232,-0.9495192309,-4.4951923077,-1.1778846155,0.3064903848,-0.6490384617,1.466346154,-0.7451923079,0.0300480769,-0.3966346156,-3.5576923077,-1.1778846155,0.9014423079,-0.6490384617,3.1610576924,3.701923077,1.5384615386,-0.9375000002,-3.7740384616,-1.1778846155,1.9951923078,-4.6394230769,-1.466346154,2.9807692308,-0.3004807694,0.9134615386,-0.3846153848,3.3052884616,0.5168269233,-0.6490384617,2.2596153847,-0.1622596155,1.2740384617,-0.4326923079,-3.0528846155,3.1610576924,0.1622596155,-4.6394230769,3.1250000001,2.5721153847,-2.4759615386,0.1923076924,-2.9807692308,1.6586538463,0.7812500002,-0.0420673077,-0.0841346154,-1.8028846155,2.3798076924,-0.8293269232,-4.1346153846,1.2500000002,-0.6009615386,0.1382211539,-2.2115384616,0.480769231,-0.3004807694,-0.8774038463,-2.9086538462,1.6346153848,0.0180288462,0.3245192309,0.264423077,0.7091346156,-2.5000000001,-0.9855769232,-3.0528846155,-1.1778846155,0.2584134617,0.3305288463,-1.4423076924,-0.7211538463,0.0961538462,-0.8052884617,-3.7740384616,2.5240384616,1.9951923078,-0.6490384617,3.1971153847,0.1622596155,1.2740384617,-0.4447115386,-4.0625,-1.1778846155,1.4182692309,0.6490384617,-2.0192307694,-0.1682692308,2.403846154,0.1923076924,-3.0528846155,3.1610576924,1.9951923078,-0.6009615386,-0.078125,0.7331730771,-2.4759615386,-0.8173076925,-3.7740384616,-1.1778846155,0.4206730771,-0.108173077,-0.0721153846,0.1502403847,-1.5384615386,-0.8533653848,-3.3413461539,3.0168269232,0.0661057693,0.1923076924,0.480769231,0.1502403847,-1.5384615386,-1.0216346155,-3.701923077,-1.1778846155,0.8052884617,-0.1322115385,-1.466346154,2.9807692308,-0.3425480771,0.8293269232,-4.0264423077,1.2500000002,0.0180288462,-0.4567307694,-2.0192307694,-0.1502403847,-1.0336538463,0.7812500002,-0.1201923078,0.8173076925,0.0180288462,-0.4567307694,-2.2355769232,0.0480769231,-0.3305288463,1.0096153848,-3.9903846154,2.5961538462,0.0180288462,-4.6754807692,-0.9134615386,-3.7379807693,-2.5240384616,-0.8774038463,-2.9807692308,1.2740384617,0.1923076924,-2.0432692309,0.2704326924,2.9807692308,-0.3605769232,0.7812500002,-0.3846153848,3.233173077,0.4927884617,-0.0420673077,-0.2764423078,0.685096154,-1.5384615386,-0.9375000002,-3.7740384616,-1.1778846155,0.4206730771,-0.1382211539,0.216346154,-0.1682692308,2.3557692309,0.9375000002,-4.1346153846,2.0432692309,0.2103365386,-4.4230769231,0.480769231,0.1442307693,-1.5384615386,-0.8774038463,-3.1971153847,3.4495192308,0.0661057693,-2.764423077,-0.0841346154,-3.6298076924,-1.5384615386,-0.9134615386,-3.5576923077,2.6201923078,1.6105769232,-4.4951923077,-0.078125,2.9807692308,-0.3425480771,-4.3149038462,-3.7740384616,-0.2463942309,-1.2259615386,-0.6610576925,-0.5408653848,2.9807692308,-0.3365384617,-0.9855769232,-3.0528846155,1.7548076924,0.5168269233,-0.6610576925,-0.5408653848,2.9807692308,-0.3425480771,-0.8293269232,-3.3413461539,2.9807692308,-0.6009615386,1.5865384617,-0.0721153846,-3.7379807693,-2.3076923078,0.9375000002,-2.9807692308,2.5961538462,0.0180288462,-3.4855769231,-0.372596154,-0.6730769233,-2.4759615386,-0.7812500002,-0.3846153848,2.3317307693,0.8052884617,-4.6754807692,-0.528846154,0.4086538463,0.1923076924,4.7836538462,-3.701923077,-1.1778846155,0.9014423079,-0.6009615386,-0.0841346154,-0.7331730771,-2.3557692309,0.8173076925,-2.764423077,3.0889423078,0.0661057693,-3.9182692308,-0.078125,0.1442307693,-2.5240384616,0.1923076924,-3.1250000001,2.3317307693,1.0937500002,0.2283653847,-2.2596153847,-2.764423077,0.2403846155,1.0216346155,-3.0528846155,-1.1778846155,0.2103365386,-0.6490384617,0.528846154,-0.7091346156,-2.4759615386,0.997596154,-0.3846153848,2.4278846155,1.0937500002,0.2283653847,0.2764423078,-1.2019230771,0.2043269232,-0.8293269232,-0.3846153848,1.2500000002,0.0180288462,-0.4567307694,4.3509615385,-2.764423077,0.1923076924,0.8653846156,-0.3846153848,1.2740384617,0.3966346156,-0.0360576923,-0.2704326924,-0.0120192308,0.264423077,0.9495192309,-0.3846153848,4.0264423077,0.0540865385,-0.0420673077,-1.1177884617,-0.480769231,-0.3365384617,1.0216346155,-3.0528846155,-1.1778846155,0.997596154,-4.4951923077,-0.078125,-0.1442307693,-2.5961538462,0.1923076924,-4.0625,1.6586538463,0.997596154,0.4567307694,0.264423077,0.1622596155,1.2740384617,-0.2403846155,-4.4951923077,2.5961538462,0.0180288462,1.6826923078,-0.216346154,-0.1682692308,2.3557692309,0.2463942309,-0.1201923078,0.8173076925,0.0180288462,0.1382211539,-2.2115384616,0.480769231,-0.3305288463,-0.8774038463,-0.3846153848,2.4278846155,0.4927884617,-0.0360576923,-0.9375000002,0.685096154,-2.5240384616,-0.9615384617,-3.7740384616,-1.1778846155,0.2584134617,0.3004807694,-0.078125,1.0937500002,-2.4759615386,0.0600961539,-0.5769230771,2.4278846155,0.4927884617,-0.0360576923,-0.9375000002,0.685096154,-2.5240384616,-0.9615384617,-3.7740384616,-1.1778846155,0.2584134617,0.3004807694,-0.078125,1.0937500002,-2.4759615386,0.2463942309,-0.1201923078,0.294471154,1.0697115386,-0.0360576923,0.0721153846,-0.6730769233,0.3425480771,-4.170673077,-0.3846153848,1.5625000001,0.2463942309,-0.0360576923,-1.4423076924,0.7331730771,0.3305288463,0.9134615386,-4.2788461539,1.6586538463,1.5384615386,-2.0432692309,0.216346154,-0.1442307693,2.5480769232,0.7812500002,-3.701923077,1.5625000001,1.0697115386,-0.0360576923,2.2115384616,-1.1057692309,-2.3076923078,0.9375000002,-2.764423077,-1.1778846155,0.8052884617,-2.9086538462,4.3509615385,-1.7548076924,-2.5240384616,0.0600961539,-1.2259615386,4.170673077,0.9735576925,-0.0420673077,-1.4423076924,0.480769231,-0.3365384617,1.0216346155,-3.0528846155,1.5625000001,0.0661057693,0.2764423078,-0.2704326924,1.3461538463,-0.3245192309,-0.7812500002,-4.0625,-1.1778846155,0.3064903848,-2.9086538462,4.3509615385,-1.7548076924,-2.5240384616,0.0600961539,-1.9711538463,3.4495192308,0.2463942309,-0.0360576923,-1.4423076924,0.6971153848,0.2884615386,0.9254807694,-3.7740384616,3.1250000001,0.0180288462,0.841346154,0.2764423078,1.778846154,-2.5240384616,-0.0600961539,-1.7307692309,2.6201923078,1.7548076924,-0.0360576923,-1.466346154,3.701923077,1.2740384617,-0.685096154,-0.3846153848,1.2500000002,0.0180288462,-2.9086538462,3.9903846154,-0.1622596155,-2.3557692309,0.8894230771,-3.7740384616,2.9807692308,0.0180288462,-0.6610576925,-0.8173076925,-0.1622596155,-4.4230769231,0.997596154,-0.3846153848,3.1610576924,0.2584134617,-4.0625,-0.9254807694,-0.7091346156,-0.3245192309,-0.9495192309,-0.1201923078,0.294471154,0.0661057693,0.3004807694,-0.078125,0.6730769233,-2.4759615386,-0.9495192309,-0.3846153848,1.6586538463,0.9735576925,-0.0360576923,1.466346154,3.701923077,1.5384615386,-0.7932692309,-3.7740384616,2.3317307693,1.8028846155,-1.6826923078,1.466346154,0.1622596155,1.2740384617,-0.685096154,-0.3846153848,3.4495192308,0.997596154,-0.108173077,-0.0721153846,-3.5576923077,-2.4759615386,-0.8052884617,-3.3774038462,3.1610576924,0.9735576925,-0.0420673077,-0.9254807694,-0.7091346156,-0.294471154,-0.7812500002,-3.9903846154,-0.2463942309,-0.997596154,-4.4951923077,-0.0841346154,-4.7836538462,-1.5384615386,-0.9615384617,-3.7740384616,2.9807692308,0.0180288462,0.1382211539,-2.6201923078,-0.480769231,-0.3004807694,0.997596154,-0.3846153848,2.8725961539,2.1875000001,-0.6009615386,-0.078125,0.685096154,-1.5384615386,-0.8052884617,-3.7740384616,2.4278846155,1.2259615386,-2.9086538462,0.264423077,-3.6658653847,1.2740384617,-0.6129807694,-3.3413461539,-1.1778846155,0.0661057693,-2.764423077,-0.0721153846,1.778846154,-2.4759615386,-0.7812500002,-3.5576923077,-1.1778846155,0.2103365386,-0.6009615386,-0.0721153846,-3.7379807693,-2.3557692309,0.9375000002,-4.1346153846,1.2740384617,1.7307692309,-2.0432692309,-0.9134615386,0.685096154,2.5480769232,0.9855769232,-3.7740384616,-1.1778846155,0.9014423079,-0.1322115385,1.4423076924,0.480769231,-0.3425480771,0.7812500002,-3.5576923077,-0.2463942309,-1.4182692309,0.6490384617,0.264423077,0.7211538463,0.3305288463,0.1923076924,-4.2788461539,1.6586538463,1.6105769232,0.4567307694,-2.0192307694,-0.1682692308,-0.2884615386,0.997596154,-2.764423077,1.5625000001,0.0661057693,0.3004807694,-0.078125,0.1442307693,-2.5240384616,0.1923076924,-4.1346153846,3.0168269232,0.2584134617,0.2884615386,0.480769231,-1.1298076925,0.3305288463,-0.1923076924,-2.9807692308,1.6586538463,1.8028846155,-4.0985576923,-2.2115384616,0.1442307693,-1.5384615386,-1.0697115386,-0.3846153848,1.6586538463,0.9735576925,-0.0360576923,1.4423076924,-0.480769231,-0.294471154,0.7812500002,-3.6298076924,1.2500000002,-0.6009615386,1.5865384617,-0.0841346154,-0.7331730771,-2.3557692309,0.1923076924,-2.9807692308,1.6586538463,0.6129807694,-0.6490384617,2.2355769232,3.701923077,1.5384615386,-1.0096153848,-3.7740384616,1.5625000001,1.0697115386,-0.0360576923,1.466346154,2.9807692308,-0.3004807694,-0.8293269232,-3.6658653847,1.2740384617,1.7307692309,-2.0432692309,0.216346154,-0.1682692308,-2.5480769232,0.8293269232,-0.3846153848,1.5625000001,0.2584134617,-2.0673076924,-2.2355769232,0.7091346156,2.5240384616,0.1923076924,-4.1346153846,2.6201923078,0.2103365386,-4.4951923077,-0.078125,0.1622596155,1.5384615386,-0.8173076925,-3.0528846155,2.4759615386,0.0661057693,0.2884615386,0.5048076925,-0.1442307693,-2.5240384616,-0.7812500002,-0.3846153848,2.4278846155,0.0901442308,0.1322115385,-0.2704326924,1.7307692309,-1.2740384617,-0.5769230771,-2.764423077,3.0168269232,0.0540865385,-0.0360576923,2.2115384616,-1.1057692309,-2.3076923078,0.9375000002,-2.764423077,-0.2403846155,0.4206730771,0.6490384617,3.1250000001,-0.480769231,-0.294471154,0.7812500002,-3.701923077,1.466346154,0.5649038463,0.3245192309,2.8365384616,-0.1682692308,2.403846154,0.9134615386,-2.8365384616,1.2740384617,1.5625000001,-1.5384615386,0.5168269233,-0.480769231,-0.2884615386,0.1923076924,-3.5576923077,2.5961538462,0.0180288462,-3.4855769231,-2.2355769232,-1.8028846155,2.5240384616,-0.1923076924,-3.0528846155,3.1250000001,0.0180288462,-3.7740384616,-0.2764423078,-2.9807692308,-0.3425480771,0.8293269232,-3.701923077,1.466346154,0.5168269233,-2.9086538462,1.466346154,2.764423077,0.1201923078,-0.5769230771,-2.764423077,3.0168269232,0.0540865385,-0.0360576923,2.2115384616,-1.1057692309,-2.3076923078,0.9375000002,-2.764423077,-2.0192307694,-0.6009615386,1.5865384617,-0.0721153846,-0.480769231,-0.3245192309,-0.9495192309,-0.3846153848,2.4278846155,0.2584134617,-2.0673076924,4.3509615385,-1.3461538463,-0.3004807694,0.997596154,-0.3846153848,2.4759615386,0.0661057693,0.3004807694,-0.0841346154,-3.5937500001,-2.4759615386,-0.8052884617,-3.3413461539,2.3317307693,0.8052884617,-4.4230769231,0.4447115386,-0.1201923078,-2.5480769232,0.8774038463,-3.0528846155,3.0168269232,1.0697115386,-0.0420673077,-3.1250000001,0.7211538463,0.3485576925,-0.8293269232,-0.6009615386,-0.2463942309,-3.0168269232,-0.0360576923,-0.216346154,-0.1622596155,-0.3305288463,0.1923076924,-3.6298076924,1.6586538463,0.6129807694,-4.6754807692,-0.4326923079,-0.1502403847,-2.5240384616,0.1923076924,-3.6658653847,1.2740384617,1.7548076924,-0.0420673077,-0.9134615386,0.7091346156,0.294471154,0.8774038463,-3.5576923077,2.3317307693,1.0576923079,-1.9711538463,0.0600961539,-0.7331730771,-2.403846154,0.8293269232,-3.9903846154,2.5961538462,0.0180288462,0.841346154,-2.2596153847,-1.8509615386,-0.3004807694,0.2463942309,-0.1201923078,0.8173076925,0.0180288462,-0.108173077,-0.078125,0.1622596155,1.5384615386,-0.9254807694,-3.0528846155,2.139423077,1.0937500002,0.2043269232,-0.0721153846,0.7211538463,1.5384615386,-0.9254807694,2.764423077,3.1250000001,0.0180288462,0.3245192309,-2.2355769232,1.7307692309,2.403846154,0.9134615386,-3.5576923077,2.5961538462,-0.5889423079,-1.2740384617,-2.2355769232,1.7307692309,-1.5384615386,-0.8052884617,-2.764423077,2.5240384616,0.1622596155,-1.8990384617,-0.9254807694,1.3461538463,-0.3425480771,0.8774038463,-3.5576923077,1.3701923078,0.0661057693,0.2043269232,0.1983173078,-1.6826923078,-1.5384615386,-0.7812500002,-0.3846153848,2.3317307693,1.0697115386,-0.0360576923,2.2115384616,0.6971153848,0.3305288463,0.9855769232,-0.3846153848,1.6586538463,1.7548076924,-0.0360576923,2.5961538462,-0.7211538463,1.5384615386,-0.997596154,-3.0528846155,2.5240384616,0.1622596155,-1.6826923078,1.466346154,0.1622596155,1.2740384617,-0.2403846155,-3.701923077,2.5961538462,0.0180288462,0.1382211539,-2.2115384616,0.685096154,-0.2884615386,0.9855769232,2.764423077,2.5000000001,0.0180288462,-2.9086538462,-0.2764423078,-2.9807692308,-0.3064903848,-0.9134615386,-3.7740384616,3.0168269232,0.2584134617,0.3004807694,0.1983173078,-1.3942307694,-0.2403846155,1.0216346155,-3.3413461539,1.6586538463,1.6105769232,-4.4951923077,-0.0841346154,1.7548076924,-2.5240384616,-1.0096153848,-3.0528846155,-2.0192307694,-0.6009615386,1.5865384617,-0.0721153846,-0.480769231,-0.3245192309,-0.9495192309,-0.3846153848,2.4278846155,0.2584134617,-2.0673076924,4.3509615385,-1.3461538463,-0.3004807694,0.997596154,-0.3846153848,2.4759615386,0.0661057693,0.3004807694,-0.0841346154,-3.5937500001,-2.4759615386,-0.8052884617,-3.3413461539,2.3317307693,0.8052884617,-4.4230769231,0.5048076925,-3.6298076924,-1.5384615386,-0.8293269232,-4.0625,-1.1778846155,0.2103365386,-0.6009615386,-0.0721153846,-0.480769231,-0.3004807694,-0.9495192309,-4.0625,-0.2463942309,-3.0168269232,-0.0360576923,-0.216346154,-0.1622596155,-0.3305288463,0.1923076924,-3.6298076924,1.6586538463,0.6129807694,-4.6754807692,-0.4326923079,-0.1502403847,-2.5240384616,0.1923076924,-3.6658653847,1.2740384617,1.7548076924,-0.0420673077,-0.9134615386,0.7091346156,0.294471154,0.8774038463,-3.5576923077,2.3317307693,1.0576923079,-2.0432692309,-0.9254807694,-0.480769231,-0.3004807694,0.997596154,-0.3846153848,1.5625000001,0.2463942309,-0.0360576923,-0.216346154,-0.1502403847,-0.3305288463,0.997596154,-0.1201923078,0.8173076925,0.0180288462,-0.108173077,-0.078125,0.1622596155,1.5384615386,-0.9254807694,-3.0528846155,2.139423077,1.0937500002,0.2043269232,-0.0721153846,0.7211538463,1.5384615386,-0.9254807694,2.764423077,3.1250000001,0.0180288462,0.3245192309,-2.2355769232,1.7307692309,2.403846154,0.9134615386,-3.5576923077,2.5961538462,-0.6009615386,0.3245192309,0.216346154,-0.1502403847,-2.5240384616,0.1923076924,-2.9807692308,1.6346153848,0.0180288462,-0.108173077,-0.0721153846,0.1622596155,2.5240384616,0.0600961539,-2.3557692309,-1.1778846155,0.0540865385,-0.0360576923,1.466346154,2.9807692308,-0.3245192309,0.8293269232,-3.4134615385,2.6201923078,1.5625000001,-0.0360576923,-2.2596153847,-2.9807692308,-0.3245192309,3.8822115385,-4.0625,-1.1778846155,1.8028846155,-0.6490384617,3.1250000001,-3.6298076924,-2.451923077,-0.9134615386,-3.7740384616,-0.2463942309,-1.8028846155,-1.5865384617,-0.0721153846,0.7211538463,1.5384615386,-0.8173076925,-3.0528846155,-1.1778846155,0.0540865385,-0.0360576923,-1.466346154,3.701923077,1.2740384617,-0.685096154,-0.3846153848,1.2500000002,0.0180288462,-2.9086538462,3.9903846154,-0.1622596155,-2.3557692309,0.8894230771,-3.7740384616,2.9807692308,0.0180288462,-0.6610576925,-0.8173076925,-0.1622596155,-4.4230769231,0.997596154,-0.3846153848,3.1610576924,0.2584134617,-4.0625,-0.9254807694,-0.7091346156,-0.3245192309,-0.9495192309,-0.1201923078,0.5408653848,0.4927884617,-0.0360576923,-2.2596153847,-2.9807692308,-0.3004807694,-0.8293269232,-0.3846153848,1.2500000002,0.0180288462,-0.4567307694,4.3509615385,-2.764423077,0.264423077,0.1923076924,-2.764423077,-1.1778846155,0.8052884617,-4.4951923077,-0.078125,0.685096154,-2.4278846155,-0.9495192309,-3.9903846154,-1.1778846155,0.2584134617,0.3004807694,-0.078125,1.0576923079,-2.5240384616,0.1923076924,-4.0625,1.6586538463,0.997596154,-0.3245192309,0.2704326924,0.1622596155,-0.3305288463,0.0600961539,-2.0673076924,2.0192307694,0.0180288462,-0.6610576925,-0.8173076925,-0.1502403847,-0.3004807694,0.1923076924,-2.764423077,-1.1778846155,0.2103365386,-4.6754807692,-0.7812500002,-1.6826923078,-1.5384615386,-0.7812500002,-0.3846153848,2.3317307693,1.0697115386,-0.0360576923,2.2115384616,0.6971153848,0.3305288463,0.9855769232,-0.3846153848,1.6586538463,1.7548076924,-0.0360576923,2.5961538462,-0.7211538463,1.5384615386,-0.997596154,-3.0528846155,2.5240384616,0.1622596155,-1.6826923078,1.466346154,0.1622596155,1.2740384617,-0.6129807694,-3.3413461539,-1.1778846155,0.2584134617,0.3004807694,-0.0721153846,0.1502403847,-1.5384615386,-0.7812500002,-0.3846153848,1.5625000001,1.0937500002,0.2884615386,0.5168269233,-0.480769231,-0.2884615386,0.1923076924,-3.5576923077,2.5961538462,0.0180288462,-3.4855769231,-2.2355769232,-1.8028846155,2.5240384616,-0.1923076924,-3.0528846155,3.1250000001,0.0180288462,-3.7740384616,-0.2764423078,-2.9807692308,-0.3425480771,0.8293269232,-3.701923077,1.466346154,0.5168269233,-2.9086538462,1.466346154,2.764423077,0.2463942309,0.8774038463,-0.3846153848,1.6586538463,1.7548076924,-0.0360576923,-1.4423076924,0.480769231,-0.2884615386,0.1923076924,-2.9807692308,2.6201923078,1.7307692309"

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
        print(volt)
        
        volt = abs(volt)

        intSegmento, keyIntervals = searchInMeta(volt)
        tempBinSegment = convertIntToBin(intSegmento)
        print(intSegmento)
        
        binSegment = putZerosBefore(tempBinSegment, bitsDeSegmento)

        volInterval = np.round(volt - arraySegmento[intSegmento], 10) # Restamos el tamaño del segmento por el voltaje y obtenemos el intervalo
        intInterval = int(round(abs(volInterval) / dictTamIntervalo[keyIntervals])) # Dividimos el voltaje restante entre el tamaño del intervalo
        tempBinInterval = convertIntToBin(intInterval)
        binInterval = putZerosBefore(tempBinInterval, bitsDeIntervalo)
        print(intInterval)
        print(binInterval)
        print("---")
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
    print(bitsDeSegmento)
    #return response + " | " + responseAS + " | " + responseAI

    return response
