ACTUAL_YEAR = 2025

(Credito1, Credito2, Credito3) = input().split(" ")

AhorroCreditos = [
    int(Credito1),
    int(Credito2),
    int(Credito3)
]

ValorMaximo = {
    "Valor": 0,
    "Posicion": 0
}


for Indice in range(len(AhorroCreditos)):
    if (AhorroCreditos[Indice] > ValorMaximo["Valor"]):
        ValorMaximo["Valor"] = AhorroCreditos[Indice]
        ValorMaximo["Posicion"] = Indice

def TrazarViajeTemporal(ValorMaximoIndicado):
    STOP = False
    NEW_ACTUAL_YEAR = ACTUAL_YEAR - ValorMaximoIndicado["Valor"]

    for Indice in range(len(AhorroCreditos)):
        if (AhorroCreditos[Indice] == ValorMaximoIndicado["Valor"] and Indice != ValorMaximoIndicado["Posicion"]):
            NEW_ACTUAL_YEAR += AhorroCreditos[Indice]
            STOP = True
        break

    if (STOP):
        return "S"
    
    SUMA_ANOS_POSIBLES = 0
    
    for Indice in range(len(AhorroCreditos)):
        if (Indice != ValorMaximoIndicado["Posicion"]):
            SUMA_ANOS_POSIBLES += AhorroCreditos[Indice]

    if ((NEW_ACTUAL_YEAR + SUMA_ANOS_POSIBLES) == ACTUAL_YEAR):
        return "S"

    return "N"

print(TrazarViajeTemporal(ValorMaximo))
    