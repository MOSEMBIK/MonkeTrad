from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext

# functions
# new Window
def openNewWindow(title: str, txt: str) -> None: 
      
    # Toplevel object which will  
    # be treated as a new window 
    newWindow = Toplevel(window) 
  
    # sets the title of the 
    # Toplevel widget 
    newWindow.title(title) 
  
    # sets the geometry of toplevel 
    newWindow.geometry("340x100") 
  
    # A Label widget to show in toplevel 
    Trad = scrolledtext.ScrolledText(newWindow,width=40,height=6)
    Trad.insert(INSERT, txt)
    Trad.grid(column=0, row=0)
    
    LbV = Label(newWindow, text=" ", font=("Arial Bold", 40))
    LbV.grid(column=0, row=1)
          
    return None
    
   
# ABC to Monke
def ABC2Monke() -> None:
    '''
    Just a simple function that encode from human latin ABC
    to Reims' DUT Info 2020's Monke Language.
    
    Disclamer :
            This code is not based on science. It
            dosen't make you able to speak the
            monkey's language.
    '''
    
    Txt = CLabcTxt.get().lower()
    Monke = ""
    abc = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    Mabc = [" ", "O", "Oh", "U", "H", "Ou", "Hi", "I", "A", "Ha", "Ho", "Uh", "Hu", "Hou", "Ah", "Houhi", "Haha", "Oug", "Houg", "Ag", "Hiha", "Hoho", "Hihahou", "Hahouhi", "Houghi", "Haaaa", "Hiiiho"]
    symb = ["?", ",", ".", "'", "!", "/", ";", ":", "&", "@", "#", "(", ")", "_", "\"", "\\", "*"]
    nmbrs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    for i in range(len(Txt)):
    
        #test for symbols and nubers
        for nb in range(len(nmbrs)):
            if Txt[i] == nmbrs[nb]:
                Monke = Monke + nmbrs[nb]
                
        for k in range(len(symb)):
            if Txt[i] == symb[k]:
                Monke = Monke + symb[k]
            
        for j in range(len(abc)):
            if Txt[i] == abc[j]:
                Monke = Monke + Mabc[j]
    
    openNewWindow("ABC 2 Monke", Monke)

        
    return None 
    
# Monke to ABC
def Monke2ABC() -> None:
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
    
    Txt = RDIMLTxt.get() + "¤"
    
    for i in range(len(Txt)):
        
        #test for symbols and nubers
        for nb in range(len(nmbrs)):
            if Txt[i] == nmbrs[nb]:
                TrueABC = TrueABC + nmbrs[nb]
                
        for k in range(len(symb)):
            if Txt[i] == symb[k]:
                TrueABC = TrueABC + symb[k]
        Temp = ""
        if Txt[i] != "¤":
            if Txt[i].isspace() == True:
                TrueABC = TrueABC + " "
            elif Txt[i].isupper() == True:
                Temp = Temp + Txt[i]
                nb = 1
                while Txt[i + nb].islower() == True:
                    Temp = Temp + Txt[i + nb]
                    nb += 1
                
            for j in range(len(Mabc)):
                if Temp == Mabc[j]:
                    TrueABC = TrueABC + abc[j]
    
    openNewWindow("Monke 2 ABC", TrueABC)
                
    return None

# ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
# End of functions

# Def Window
window = Tk()

window.title("MonkeTrad")

window.geometry("500x350")

# ABC 2 Monke
LbV1 = Label(window, text=" ", font=("Arial Bold", 30))
LbV1.grid(column=0, row=0)

CLabc = Label(window, text="Classic latin abc :                                               ", font=("Arial Bold", 16))
CLabc.grid(column=1, row=2)

CLabcTxt = Entry(window, width=70)
CLabcTxt.grid(column=1, row=3)

LbV2 = Label(window, text=" ", font=("Arial Bold", 8))
LbV2.grid(column=1, row=4)

TradCL2Mk = Button(window, text="Traduce", bg="orange", fg="black", command=ABC2Monke)
TradCL2Mk.grid(column=1, row=5)

# Monke 2 ABC
LbV3 = Label(window, text=" ", font=("Arial Bold", 30))
LbV3.grid(column=0, row=6)

RDIML = Label(window, text="RDIML :                                                               ", font=("Arial Bold", 16))
RDIML.grid(column=1, row=7)

RDIMLTxt = Entry(window, width=70)
RDIMLTxt.grid(column=1, row=8)

LbV4 = Label(window, text=" ", font=("Arial Bold", 8))
LbV4.grid(column=1, row=9)

TradMk2ABC = Button(window, text="Traduce", bg="orange", fg="black", command=Monke2ABC)
TradMk2ABC.grid(column=1, row=10)

# ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
# End of GUI

window.mainloop()

# main
