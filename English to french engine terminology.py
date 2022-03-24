engl = {
    "i": " ",
    "engine": "moteur",
    "motor": "moteur",
    "intake": "entrée",
    "compression": "compression",
    "power": "puissance",
    "exhaust": "échappement",
    "piston": "piston",
    "piston rings": "segments de piston",
    "ring gap": "espace annulaire",
    "piston pin": "axe de piston",
    "piston skirt": "jupe du piston",
    "connecting rod": "tige de connexion",
    "crankshaft": "vilebrequin",
    "main journal": "journal principal",
    "camshaft": "arbre à cames",
    "valve": "vanne",
    "valve lifter": "poussoir de soupape",
    "valve overlap": "chevauchement des valves",
    "valve margin": "marge de valve",
    "valve spring": "ressort de valve",
    "valve timing": "timing des valves",
    "dwell": "Duree de contact",
    "piston slap": "claquement de piston",
    "octane rating": "indice d'octane",
    "ignition timing": "timing d'allumage",
    "push rod": "tige de poussée",
    "connecting rod journal" : "tourillon de bielle",
    "horsepower": "chevaux-vapeur",
    "torque": "couple",
    "transaxle": "Boîte de vitesses",
    "oil": "huile",
    "gasoline": "essence",
    "gasket": "joint d'étanchéité",
    "spark plug": "bougie d'allumage",
}
def ind():
    print("     engine           ")
    print("      motor           ")
    print("     intake           ")
    print("    compression       ")
    print("      power           ")
    print("      exhaust         ")
    print("      piston          ")
    print("   piston rings       ")
    print("    ring gap          ")
    print("    piston pin        ")
    print("   piston skirt       ")
    print("  connecting rod      ")        
    print("  crankshaft          ")
    print("  main journal        ")
    print("   camshaft           ")
    print("    valve             ")
    print("   valve lifter       ")
    print("  valve overlap       ")
    print("  valve margin        ")
    print("  valve spring        ")
    print("  valve timing        ")
    print("   dwell              ")
    print(" piston slap          ")
    print(" octane rating        ")
    print(" ignition timing      ")
    print("   push rod           ")
    print("connecting rod journal")
    print("   horsepower         ")
    print("     torque           ")
    print("   transaxle          ")
    print("     oil              ")
    print("   gasoline           ")
    print("    gasket            ")
    print("  spark plug          ")
    

print("Converts 34 english words to french engine terminology.")
print("Enter i for index x to exit.")
print()
while True:
    try:
        print("Enter a english word.")
        eng = input()
        if eng == "x":
            break
        elif eng == "i":
            ind()
        print(engl[eng])
    except KeyError:
        print("Enter a  english word in index.")
        print("Try again.")    
            
    
        
        
        
         
