
def leggSammen():
    try:
        tall1 = int(input("Skriv inn det første tallet: "))
        tall2 = int(input("Skriv inn det andre tallet: "))
        summen = tall1 + tall2
        print(f'{tall1} + {tall2} = {summen}')
    except ValueError:
        print("Vennligst skriv inn gyldige tall.")
        return
        
        

def trekkFra():
    try:
        tall1 = int(input("Skriv inn det andre tallet: "))
        tall2 = int(input("Skriv inn det andre tallet: "))
        diff = int(tall1) - int(tall2)
        print(f'{tall1} - {tall2} = {diff}')
    except ValueError:
        print("Vennligst skriv inn gyldige tall.")
        return
        
        
    
def gange():
    try:
        tall1 = int(input("Skriv inn det andre tallet: "))
        tall2 = int(input("Skriv inn det andre tallet: "))
        ganging = tall1 * tall2
        print(f'{tall1} * {tall2} = {ganging}')
    except ValueError:
        print("Bro skriv inn gyldige tall.")
        return
        
        
def deling():
    try:
        tall1 = int(input("skriv inn det første tallet du vil dele: "))
        tall2 = int(input("Skriv inn det andre tallet du vil dele: "))
        
        if tall2 == 0:
            print("Du kan ikke dele med null xd.")
            
        
        resultat = tall1 / tall2 
        print(f'{tall1} / {tall2} = {resultat}')
    except ValueError:
        print("Vennligst skriv inn gyldige tall. ")
        return
    


