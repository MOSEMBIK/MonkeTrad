from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import pyperclip
import re

# functions
def Copy2Clp(txt: str, windw: str):
    pyperclip.copy(txt)

# new Window
def openNewWindow(title: str, txt: str) -> None: 
      
    # Toplevel object which will  
    # be treated as a new window 
    newWindow = Toplevel(window) 
  
    # sets the title of the 
    # Toplevel widget 
    newWindow.title(title) 

    newWindow.iconbitmap('icon.ico')
  
    # sets the geometry of toplevel 
    newWindow.geometry("320x180") 

    newWindow.resizable(0, 0)
  
    # A Label widget to show in toplevel 
    Trad = scrolledtext.ScrolledText(newWindow, width=40, height=6, font=("Arial Bold", 10))
    Trad.insert(INSERT, txt)
    Trad.grid(column = 0, row=0, pady = 10, padx = 10)
    Trad.configure(state ='disabled') 
    
    LbV = Label(newWindow, text=" ", font=("Arial Bold", 10))
    LbV.grid(column=0, row=1)

    cpbtn = Button(newWindow, text="COPY TO CLIPBOARD", bg="black", fg="white", command=lambda:[Copy2Clp(txt, newWindow), newWindow.destroy()])
    cpbtn.grid(column=0, row=3)
          
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
    
    symb = ["?", ",", ".", "'", "!", "/", ";", ":", "&", "@", "#", "(", ")", "_", "\"", "\\", "*", "%", "-", "`", "€", "£", "$", "µ", "^", "§"]
    # Msymb =

    nmbrs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    Mnmbrs = ["Hio", "Hin", "Heu", "Hoi", "Houat", "Hink", "Hik", "Het", "Hui", "Hof"]
   
   # Code wrote w/ Bepop
    for i in range(len(Txt)):

        if Txt[i] in abc:
            Monke += Mabc[abc.index(Txt[i])]

        elif Txt[i] in nmbrs:
            Monke += Mnmbrs[nmbrs.index(Txt[i])]

        elif Txt[i] in symb:
            Monke += symb[symb.index(Txt[i])]

        else:
            Monke += Txt[i]
    # Code wrote w/ Bepop
    
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
    
    symb = ["?", ",", ".", "'", "!", "/", ";", ":", "&", "@", "#", "(", ")", "_", "\"", "\\", "*", "%", "-", "`", "€", "£", "$", "µ", "^", "§"]
    # Msymb =

    nmbrs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    Mnmbrs = ["Hio", "Hin", "Heu", "Hoi", "Houat", "Hink", "Hik", "Het", "Hui", "Hof"]

    Txt = RDIMLTxt.get()
   
    # Code wrote w/ Bepop
    liste = re.findall(r'[A-Z][a-z]*|[^A-Za-z]', Txt)

    for element in liste:

        if element in Mabc:
            TrueABC += abc[Mabc.index(element)]

        elif element in Mnmbrs:
            TrueABC += Mnmbrs[nmbrs.index(element)]

        elif element in symb:
            TrueABC += symb[symb.index(element)]

        else:
            TrueABC += element
    # Code wrote w/ Bepop

    openNewWindow("Monke 2 ABC", TrueABC)
                
    return None

# ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
# End of functions
# Def Window
window = Tk()

window.resizable(0, 0)

window.title("MonkeTrad V2.3")

window.geometry("500x400")

window.iconbitmap('icon.ico')

# Header
LbV1 = Label(window, text=" ", font=("Arial Bold", 5))
LbV1.grid(column=0, row=0)

TitleM = Label(window, text="MonkeTrad ©", font=("Impact", 22))
TitleM.grid(column=1, row=1)

LbV1b = Label(window, text=" ", font=("Arial Bold", 40))
LbV1b.grid(column=0, row=1)

# ABC 2 Monke
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

LbV5 = Label(window, text=" ", font=("Arial Bold", 20))
LbV5.grid(column=0, row=11)

Credits = Label(window, text="Reims - DUT Info 2020 ©", font=("Arial Bold", 7))
Credits.grid(column=1, row=12)
Credits2 = Label(window, text="by MOSEMBIK & Bepop", font=("Arial Bold", 7))
Credits2.grid(column=1, row=13)
# ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
# End of GUI

window.mainloop()

# main
