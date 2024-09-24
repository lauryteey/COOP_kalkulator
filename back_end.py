history = []

def leggSammen():
    try:
        tall1 = int(input("Skriv inn det første tallet: "))
        tall2 = int(input("Skriv inn det andre tallet: "))
        summen = tall1 + tall2
        print(f'{tall1} + {tall2} = {summen}')
        history.append(f'{tall1} + {tall2} = {summen}')
    except ValueError:
        print("Vennligst skriv inn gyldige tall.")
        return
        
        
def trekkFra():
    try:
        tall1 = int(input("Skriv inn det andre tallet: "))
        tall2 = int(input("Skriv inn det andre tallet: "))
        diff = int(tall1) - int(tall2)
        print(f'{tall1} - {tall2} = {diff}')
        history.append(f'{tall1} - {tall2} = {diff}')
    except ValueError:
        print("Vennligst skriv inn gyldige tall.")
        return
        
         
def gange():
    try:
        tall1 = int(input("Skriv inn det første tallet: "))
        tall2 = int(input("Skriv inn det andre tallet: "))
        ganging = tall1 * tall2
        print(f'{tall1} * {tall2} = {ganging}')
        history.append(f'{tall1} * {tall2} = {ganging}')
    except ValueError:
        print("Vennlig skriv inn gyldige tall.")
        return
        
        
def deling():
    try:
        tall1 = int(input("skriv inn det første tallet: "))
        tall2 = int(input("Skriv inn det andre tallet: "))
        
        if tall2 == 0:
            print("Du kan ikke dele med null.")
            return
        
        resultat = tall1 / tall2 
        print(f'{tall1} / {tall2} = {resultat}')
        history.append(f'{tall1} / {tall2} = {resultat}')
    except ValueError:
        print("Vennligst skriv inn gyldige tall. ")
        return
    
def visHistorikk():
    if history:
        print("Beregninger så langt:")
        for entry in history:
            print(entry)
    else:
        print("Ingen beregninger er lagret ennå.")
    


