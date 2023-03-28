import random

def noppa(tulos):
    nopat = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    }

    return nopat


def luvut(montako):
    #Random numerot listaan
    numerot = []

    for i in range(montako):
        luku = random.randint(1, 6)
        numerot.append(luku)
    return numerot

#Tulostaa nopat
def tulostus(tulos, nopat):
    #Tulostaa ~~~~~~~~~~~~~~ TULOS ~~~~~~~~~~~~~~
    leveys = len(nopat[1][0]) * len(tulos) + len(tulos) - 1
    merkki = ("~" * ((leveys - 7) // 2))
    
    print(merkki + " TULOS " + merkki)

    #Tulostaa nopat
    for rivi in range(5):
        for luku in tulos:
            print(nopat[luku][rivi], end=" ")
        print()

    print(f"Sait {len(tulos)} nopalla {sum(tulos)}")
    
    

def main():
    while True:
        montako = int(input("Kuinka monta noppaa haluat heittää? (1-6) 0 lopettaa\n"))
        
        if montako == 0:
            break
        #Tarkistaa oliko numero 1-6
        elif montako in range(1, 7):

            #Heittojen tulokset
            tulos = luvut(montako)

            #Palauttaa noppa listan
            nopat = noppa(tulos)
            
            tulostus(tulos, nopat)

        else:
            print("Anna numero väliltä 1-6")

    
if __name__ == "__main__":
    main()