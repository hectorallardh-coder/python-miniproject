import random

def ladda_citat_fran_fil(filnamn):
    with open(filnamn, "w", encoding="utf-8") as fil:
        lines = []
        for element in filnamn.txt:
            line = filnamn.loads(element) 
            lines.append(line)
        return lines
    """""
    Laddar citat från en textfil.
    
    Parametrar:
        filnamn (str): Namnet på filen att läsa från
    
    Returnerar:
        list: En lista med alla citat (varje rad är ett citat)
              Returnerar tom lista om filen inte finns.
    """
    # TODO: Implementera funktionen
    # Tips: Använd try/except för att hantera FileNotFoundError
    # Tips: Använd open() med "r" och readlines()
    


def spara_citat_till_fil(citatlista, filnamn):
    fil = ladda_citat_fran_fil("citat.txt")
    fil.write(citatlista)

    """
    Sparar alla citat till en textfil.
    
    Parametrar:
        citatlista (list): Listan med citat som ska sparas
        filnamn (str): Namnet på filen att skriva till
    """
    # TODO: Implementera funktionen
    # Tips: Använd open() med "w"
    # Tips: Loop'a igenom listan och skriv varje citat + "\n"
    pass


def visa_alla_citat(citatlista):
    for elements in citatlista:
        print(elements)
    """
    Skriver ut alla citat med numrering.
    
    Parametrar:
        citatlista (list): Listan med citat som ska visas
    """
    # TODO: Implementera funktionen
    # Tips: Använd enumerate() för att få index
    # Tips: Använd strip() för att ta bort radbrytningar
    pass


def lagg_till_citat(citatlista):
    print("")
    """
    Lägger till ett nytt citat i listan.
    Användaren får mata in citat och författare.
    
    Parametrar:
        citatlista (list): Listan som citatet ska läggas till i
    
    Returnerar:
        bool: True om citatet lades till, False annars
    """
    # TODO: Implementera funktionen
    # Tips: Använd input() för att fråga efter citat och författare
    # Tips: Formatet bör vara "Citatet - Författare"
    pass


def slumpa_citat(citatlista):
    """
    Visar ett slumpmässigt citat från listan.
    
    Parametrar:
        citatlista (list): Listan att välja citat från
    """
    # TODO: Implementera funktionen
    # Tips: Använd random.randint() eller random.choice()
    # Tips: Kontrollera att listan inte är tom först
    pass


def huvudprogram():
    """
    Huvudprogrammet som styr menyn och programflödet.
    """
    # TODO: Implementera huvudprogrammet
    # 1. Ladda befintliga citat med ladda_citat_fran_fil()
    # 2. Skapa en while-loop som visar menyn
    # 3. Hantera användarens val med if/elif/else
    # 4. Vid val 2: lägg till citat och spara med spara_citat_till_fil()
    # 5. Vid val 4: avsluta loopen
    pass


# Starta programmet om filen körs direkt
if __name__ == "__main__":
    huvudprogram()