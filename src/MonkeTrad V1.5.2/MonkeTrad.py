# MonkeTrad by MOSEMBIK
# V1.5.2

# ABC to Monke
def ABC2Monke(txt: str) -> str:
    '''
    Just a simple function that encode from human latin ABC
    to Reims' DUT Info 2020's Monke Language.
    
    Disclamer :
            This code is not based on science. It
            dosen't make you able to speak the
            monkey's language.
    '''
    
    Txt = txt.lower()
    Monke = ""
    abc = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    Mabc = [" ", "O", "Oh", "U", "H", "Ou", "Hi", "I", "A", "Ha", "Ho", "Uh", "Hu", "Hou", "Ah", "Houhi", "Haha", "Oug", "Houg", "Ag", "Hiha", "Hoho", "Hihahou", "Hahouhi", "Houghi", "Haaaa", "Hiiiho"]
    symb = ["?", ",", ".", "'", "!", "/", ";", ":", "&", "@", "#", "(", ")", "_", "\"", "\\", "*"]
    nmbrs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    for i in range(len(Txt)):
    
        #test for symbols and nubers
        for nb in range(len(nmbrs)):
            if txt[i] == nmbrs[nb]:
                Monke = Monke + nmbrs[nb]
                
        for k in range(len(symb)):
            if txt[i] == symb[k]:
                Monke = Monke + symb[k]
            
        for j in range(len(abc)):
            if txt[i] == abc[j]:
                Monke = Monke + Mabc[j]
        
    return Monke  

# Monke to ABC
def Monke2ABC(txt: str) -> str:
    '''
    Just a simple function that decode from Reims' DUT Info
    2020's Monke Language
    to human latin ABC.
    
    Disclamer :
            This code is not based on science. It
            dosen't make you able to speak the
            monkey's language.
    '''
    
    TrueABC = ""
    abc = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    Mabc = [" ", "O", "Oh", "U", "H", "Ou", "Hi", "I", "A", "Ha", "Ho", "Uh", "Hu", "Hou", "Ah", "Houhi", "Haha", "Oug", "Houg", "Ag", "Hiha", "Hoho", "Hihahou", "Hahouhi", "Houghi", "Haaaa", "Hiiiho"]
    symb = ["?", ",", ".", "'", "!", "/", ";", ":", "&", "@", "#", "(", ")", "_", "\"", "\\", "*"]
    nmbrs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    txt = txt + "¤"
    
    for i in range(len(txt)):
        
        #test for symbols and nubers
        for nb in range(len(nmbrs)):
            if txt[i] == nmbrs[nb]:
                TrueABC = TrueABC + nmbrs[nb]
                
        for k in range(len(symb)):
            if txt[i] == symb[k]:
                TrueABC = TrueABC + symb[k]
        Temp = ""
        if txt[i] != "¤":
            if txt[i].isspace() == True:
                TrueABC = TrueABC + " "
            elif txt[i].isupper() == True:
                Temp = Temp + txt[i]
                nb = 1
                while txt[i + nb].islower() == True:
                    Temp = Temp + txt[i + nb]
                    nb += 1
                
            for j in range(len(Mabc)):
                if Temp == Mabc[j]:
                    TrueABC = TrueABC + abc[j]
                
    return TrueABC


# main
def main() -> None:
    print("Welcome in MonkeTrad by MOSEMBIK.", "Press enter to start :     ", sep="\n")
    OSEF = input(" ")
    Start = 1
    while Start == 1:
        print("Insert M if you want to traduce from RDIML to a Language that use Latin alphabet. Insert H if you want to traduce from a Language that use Latin alphabet to RDIML.")
        Lng = input("     ")
        if Lng.upper() == "M":
            txt = input("Insert your text now :   ")
            ToPrint = Monke2ABC(txt)
            print(ToPrint)
            print(" ", "Press enter to continue :    ", sep="\n")
            restart = input(" ")
        elif Lng.upper() == "H":
            txt = input("Insert your text now :   ")
            ToPrint = ABC2Monke(txt.lower())
            print(ToPrint)
            print(" ", "Press enter to continue :    ", sep="\n")
            restart = input(" ")
        else:
            print("OMG, are u stupid ? Insert M or H. Dude.")
        
        print(" ", "Press enter to restart or EXIT to exit :    ", sep="\n")
        restart = input(" ")
        if restart.upper() == "EXIT":
            Start = 0
        else :
            Start = 1
    
    return None
# ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
# End of functions

# Start
main()