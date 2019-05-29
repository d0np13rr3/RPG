"""pip install Pillow for Python 3.7 imagery"""
 
from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import ttk
from PIL import ImageTk, Image
import os
import numpy as np
from os import path
from tkinter import messagebox
import random
 
 
main = Tk()

exists = os.path.isfile('./PLL.txt')
if exists:
    pass
else:
    fp=open("PLL.txt", "w+")
    

"""Databases"""

PlayerDict = {"Pierre":{"attack": 100, "Defense": 80, "Magic" : 50, "Dexterity": 20, "Drinking" : 75, "Jester" : 50, "Class": "Warrior", "Name": "Pierre"}}
EnemyDict = {"Batman":{"attack": 100, "Defense": 100, "Magic" : 0, "Dexterity": 100, "Drinking" : 100, "Jester" : 0, "Class": "Warrior", "Name": "Batman"},
             "Goblin":{"attack": 1, "Defense": 1, "Magic" : 0, "Dexterity": 1, "Drinking" : 10, "Jester" : 50, "Class": "Warrior", "Name": "Goblin"},
             "Dragon":{"attack": 1000, "Defense": 1000, "Magic" : 1000, "Dexterity": 1000, "Drinking" : 1000, "Jester" : 0, "Class": "Warrior", "Name": "Dragon"},
             "Olivier":{"attack": 100000, "Defense": 100000, "Magic" : 100000, "Dexterity": 100000, "Drinking" : 100000, "Jester" : 100000, "Class": "Warrior", "Name": "Olivier"},
             "Diablo":{"attack": 10000000, "Defense": 10000000, "Magic" : 10000000, "Dexterity": 10000000, "Drinking" : 10000000, "Jester" : 10000000, "Class": "Warrior", "Name": "Diablo"},
             "Kater":{"attack": 10, "Defense": 10, "Magic" : 10, "Dexterity": 10, "Drinking" : 99999999, "Jester" : 10, "Class": "Warrior", "Name": "Kater"},
             "Olivier":{"attack": 100000, "Defense": 100000, "Magic" : 100000, "Dexterity": 100000, "Drinking" : 100000, "Jester" : 100000, "Class": "Warrior", "Name": "Olivier"},
             "Olivier":{"attack": 100000, "Defense": 100000, "Magic" : 100000, "Dexterity": 100000, "Drinking" : 100000, "Jester" : 100000, "Class": "Warrior", "Name": "Olivier"},
             "Olivier":{"attack": 100000, "Defense": 100000, "Magic" : 100000, "Dexterity": 100000, "Drinking" : 100000, "Jester" : 100000, "Class": "Warrior", "Name": "Olivier"}}
PlayerList = []
EnemyList = ["Goblin", "Batman", "Dragon", "Olivier","Diablo","Kater"]

with open ('PLL.txt', 'rt') as myfile:
        for mylin in myfile:
            myline = mylin.rstrip()
            PlayerList.append(myline)

PBDict = {}
tempPPB = []
tempPPBCom = []
Wspot = 6
AddedAttack = [0,0,0,0,0,0]
AddedDefense = [0,0,0,0,0,0]
ScoreDone = [0,0,0]
StartA = 0
Hspot = 6
Aspot = 6
Sspot = 6
Bspot = 6
Pspot = 6

Classes =["Warrior", "Archer", "Mage", "Necromancer", "Bard", "Jester", "Wanderer"]
Weapons =["axe.png","sword.png", "smart.png","ulti.png"]
WName = ["Axe of Apocalypse", "Sword of Fire & ice", "Trumps wand"]
Helmets = ["pet.png", "behe.png", "pirate.png"]
HName = ["Hardcore klak", "Bierhelm", "Pirate hat"]
LoreBase =["Oehw Yeah!!", "Fuck!", "Will you raise your drunk\n as you did your dead?", "I'm about to kick ass and chew bubble gum.\n But I'm all out of gum", "Say hello to my little friend", "Ne me quitte pas", "Why so serious?",
           "Wanna see my wand?", "Apocalypse Now", "We're men, we're men in tights", "Arrrr!!!"]
AName = ["Dragon Armor", "Marcelleke", "Metal Shirt"]
Armors = ["armor.png", "marcel.png", "metalsh.png"]
SName = ["Firewall", "Skull shield", "Pint"]
Shields = ["shield.png", "skull.png", "pint.png"]
BName = ["F*ck Me Boots", "Rock Boots", "Skateboard"]
Boots = ["boots.png","boot.png","skate.png"]
PName = ["Fiery Pants", "Black jeans", "Speedo"]
Pants = ["fire.png","jeans.png","speedo.png"]


"""GUI"""

main.title('RPG')
main.geometry('1000x600')

def LB():
    N = ABX.get()
    N1 = N.rstrip()

    Cla = Clbl.get()
    ClaX = Cla.rstrip()  
    
    if N1 == "Pierre":
        LB1.configure(text = LoreBase[1])
    elif ClaX == "Necromancer":
        LB1.configure(text = LoreBase[2])
    elif ClaX == "Bard":
        LB1.configure(text = LoreBase[5])
    elif ClaX == "Jester":
        LB1.configure(text = LoreBase[6])
    elif ClaX == "Mage":
        LB1.configure(text = LoreBase[7])
    elif ClaX == "Wanderer":
        LB1.configure(text = LoreBase[8])
    elif ClaX == "Archer":
        LB1.configure(text = LoreBase[9])
    elif ClaX == "Warrior":
        LB1.configure(text = LoreBase[10])
    else:
        pass

def Info1():
    messagebox.showinfo("Info", "New: clear all fields.\n Get: Fill in name in upper field to get your player. \n Show: Pick a class to show it's attributes. \n Save: After picking a class and Name you can save your character.")
def Info3():
    messagebox.showinfo("Info", "Pick weapons in the upper fiels, save 'em with save and get 'em with get o.0")
def Info2():
    messagebox.showinfo("Info", "Input the players and their scores ranging up to down. Save with enter heroes, you do this only once. Later you can view the rank with this button.")
def Info4():
    messagebox.showinfo("Info", "Quests: Pick a quest, if needed fill number done and then Add. Your experience rises. \n Battle: Pick an enemy and fight it, see how strong you are. \n Il morituri te salutant: See the top three platers; \n All souls: See all the player and their total experience.")
def Info5():
    messagebox.showinfo("Info", "Input the players and their scores ranging up to down. Save with enter heroes, you do this only once. Later you can view the rank with this button.")
def Fight():
    """PLayer One"""

    P1 = ABX.get()
    
    mylines = []
    with open (P1+'.txt', 'rt') as myfile:
        for myline in myfile:
            mylines.append(myline)
    
    a = AD.cget("text")
    d = AD2.cget("text")
       
    A2 = a
    LB2.configure(text = A2)
    print(A2)
    A3 = d
    LB3.configure(text = A3)
    print(A3)
    A4 = mylines[4] 
    LB4.configure(text = A4)
    print(A4)
    A5 = mylines[5] 
    LB5.configure(text = A5)
    print(A5)
    A6 = mylines[6] 
    LB6.configure(text = A6)
    print(A6)
    A7 = mylines[7] 
    LB7.configure(text = A7)
    print(A7)

    CalcP1Att = int(A2) + int(A4) + int(A5)/2 + int(A6)/2
    CalcP1Def = int(A3) + int(A4) + (int(A5)/2) - (int(A6)/3) + int(A7)

    
    """Player 2"""
    P2 =ttk.e2.get()
    
    mylines2 = [0,0,0,0,0,0,0,0,0]
    mylines2[2] = EnemyDict[P2]["attack"]
    mylines2[3] = EnemyDict[P2]["Defense"]
    mylines2[4] = EnemyDict[P2]["Magic"]
    mylines2[5] = EnemyDict[P2]["Dexterity"]
    mylines2[6] = EnemyDict[P2]["Drinking"]
    mylines2[7] = EnemyDict[P2]["Jester"]
    print(mylines2)
    
  
    A22 = mylines2[2] 
    LB2.configure(text = A2)
    A32 = mylines2[3] 
    LB3.configure(text = A3)
    A42 = mylines2[4] 
    LB4.configure(text = A4)
    A52 = mylines2[5] 
    LB5.configure(text = A5)
    A62 = mylines2[6] 
    LB6.configure(text = A6)
    A72 = mylines2[7] 
    LB7.configure(text = A7)

    CalcP2Att = int(A22) + int(A42) + int(A52)/2 + int(A62)/2
    CalcP2Def = int(A32) + int(A42) + (int(A52)/2) - (int(A62)/3) + int(A72)

    print(str(CalcP1Att) + " is Att1 " + str(CalcP1Def) + " is Def1")
    print(str(CalcP2Att) + " is Att2 " +  str(CalcP2Def) + " is Def2")

    DefensePlayer1 = A3
    print("DefPl1 is "+ str(DefensePlayer1))
    DefensePlayer2 = A32
    print("DefPl2 is "+ str(DefensePlayer2))

    while 0 <= int(DefensePlayer1) and 0 <= int(DefensePlayer2):

        Rand1 = random.randint(1,8)
        Rand2 = random.randint(1,8)

            
        DefAtt1 = ((CalcP1Att - (CalcP2Def /2))*Rand1)/10
        if DefAtt1 <0:
            DefAtt1 = 0
        DefAtt2 = ((CalcP2Att - (CalcP1Def /2))*Rand2)/10
        if DefAtt2 <0:
            DefAtt2 = 0

        print(str(DefAtt1) + " is definitieve attack pl1")
        print(str(DefAtt2) + " is definitieve attack pl2")
        
        messagebox.showinfo("Info", P1 +" doet " + str(int(DefAtt1)) + " schade.")
        messagebox.showinfo("info", P2 +" doet " + str(int(DefAtt2)) + " schade.")

        
        DefensePlayer1 = int(DefensePlayer1) - DefAtt2
        print(str(DefensePlayer1)+"Pl1 Defense")
        DefensePlayer2 = int(DefensePlayer2) - DefAtt1
        print(str(DefensePlayer2)+"Pl2 Defense")
        Winner = ""
        if DefensePlayer1 < 0:
            
            Winner = P2
        if DefensePlayer2 < 0:
            
            Winner = P1

            """if DefensePlayer2 < 0:
            
                if Winner == P2:
                    pass
                else:
                    Winner == P1"""
                    
   
    messagebox.showinfo("Winnaar", Winner + " is victorious") 

def Battle():

        top = ttk.top = Toplevel()

         
        tkinter.Label(top, text="Choose players", font = 'Bold').grid(row=7,column=2)
        P1 = ABX.get()
        AD3 = tkinter.Label(top, text="No Player",borderwidth=1  )
        AD3.grid(row=8,column=2)
        AD3.configure(text = P1)
        """LBLPL1 = tkinter.Label(page1, "" "" ,borderwidth=1 )
        LBLPL1.grid(row=8,column=2)
        LBLPL1.configure(Text = P1)"""
        """ttk.e = ttk.Combobox(top, values = P1)
        ttk.e.grid(row=8,column=2)"""
        ttk.e2 = ttk.Combobox(top, values = EnemyList)
        ttk.e2.grid(row=8,column=3)

        b = Button(top, text="Fight", command=Fight)
        b.grid(row=9,column=2)

"""Zuipspel Score"""
def ZS(NrZS):
    ScoreD = []
    print(NrZS)
    with open ('SD.txt', 'rt') as myfile:
        for myline in myfile:
            myli = myline.rstrip()
            ScoreD.append(myli)
            print("File open")
            


    if NrZS == 1:
        Scorecounter = NrZS + 2
        if ScoreD[Scorecounter] == str(0):

            ScoreD[Scorecounter] = str(1)

            TextZS = "ZS" + str(NrZS)
       
            fc=open(TextZS+"Com.txt", "w+")
            PB1  = PPBComList[0].get()
            PB2  = PPBComList[1].get()
            PB3  = PPBComList[2].get()
            PB4  = PPBComList[3].get()
            PB5  = PPBComList[4].get()
            PB6  = PPBComList[5].get()
            PB7  = PPBComList[2].get()
            PB8  = PPBComList[3].get()
            PB9  = PPBComList[4].get()
            PB10  = PPBComList[5].get()
            PB11  = PPBComList[0].get()
            PB12  = PPBComList[1].get()
            PB13  = PPBComList[2].get()
            PB14  = PPBComList[3].get()
            PB15  = PPBComList[4].get()
            PB16  = PPBComList[5].get()
            PB17  = PPBComList[2].get()
            PB18  = PPBComList[3].get()
            PB19  = PPBComList[4].get()
            PB20  = PPBComList[5].get()
        
            """Add experience according to rank"""

            width = 7
            fillchar = "0"
        
            f=open(PB1+"exp.txt", "r")
            if f.mode == 'r':
                contents =f.read()
            f.close()
            PG = int(contents) + 10000
            PGfill = str(PG).rjust(width, fillchar)

            f= open(PB1+"exp.txt","w")
            f.write(PGfill)
            f.close()

            f=open(PB2+"exp.txt", "r")
            if f.mode == 'r':
                contents =f.read()
            f.close()
            PG = int(contents) + 5000
            PGfill = str(PG).rjust(width, fillchar)

            f= open(PB2+"exp.txt","w")
            f.write(PGfill)
            f.close()

            f=open(PB3+"exp.txt", "r")
            if f.mode == 'r':
                contents =f.read()
            f.close()
            PG = int(contents) + 2500
            PGfill = str(PG).rjust(width, fillchar)

            f= open(PB3+"exp.txt","w")
            f.write(PGfill)
            f.close()
        
            fc.write(str(PB1+"\n"))
            fc.write(str(PB2+"\n"))
            fc.write(str(PB3 +"\n"))
            fc.write(str(PB4+"\n"))
            fc.write(str(PB5+"\n"))
            fc.write(str(PB6 +"\n"))
            fc.write(str(PB7 +"\n"))
            fc.write(str(PB8+"\n"))
            fc.write(str(PB9+"\n"))
            fc.write(str(PB10 +"\n"))
            fc.write(str(PB11+"\n"))
            fc.write(str(PB12+"\n"))
            fc.write(str(PB13 +"\n"))
            fc.write(str(PB14+"\n"))
            fc.write(str(PB15+"\n"))
            fc.write(str(PB16 +"\n"))
            fc.write(str(PB17 +"\n"))
            fc.write(str(PB18+"\n"))
            fc.write(str(PB19+"\n"))
            fc.write(str(PB20 +"\n"))
        
            f=open(TextZS+".txt", "w+")
    
            PB1  = PPBList[0].get()
            PB2  = PPBList[1].get()
            PB3  = PPBList[2].get()
            PB4  = PPBList[3].get()
            PB5  = PPBList[4].get()
            PB6  = PPBList[5].get()
            PB7  = PPBList[2].get()
            PB8  = PPBList[3].get()
            PB9  = PPBList[4].get()
            PB10  = PPBList[5].get()
            PB11  = PPBList[0].get()
            PB12  = PPBList[1].get()
            PB13  = PPBList[2].get()
            PB14  = PPBList[3].get()
            PB15  = PPBList[4].get()
            PB16  = PPBList[5].get()
            PB17  = PPBList[2].get()
            PB18  = PPBList[3].get()
            PB19  = PPBList[4].get()
            PB20  = PPBList[5].get()

            f.write(str(PB1+"\n"))
            f.write(str(PB2+"\n"))
            f.write(str(PB3 +"\n"))
            f.write(str(PB4+"\n"))
            f.write(str(PB5+"\n"))
            f.write(str(PB6 +"\n"))
            f.write(str(PB7 +"\n"))
            f.write(str(PB8+"\n"))
            f.write(str(PB9+"\n"))
            f.write(str(PB10 +"\n"))
            f.write(str(PB11+"\n"))
            f.write(str(PB12+"\n"))
            f.write(str(PB13 +"\n"))
            f.write(str(PB14+"\n"))
            f.write(str(PB15+"\n"))
            f.write(str(PB16 +"\n"))
            f.write(str(PB17 +"\n"))
            f.write(str(PB18+"\n"))
            f.write(str(PB19+"\n"))
            f.write(str(PB20 +"\n"))                


            fp=open("SD.txt", "w+")     
            o=0
            for i in ScoreD:
                fp.write(str(ScoreD[o])+"\n")
                o = o +1
            print("File written")

            f.close()
            fp.close()
            fc.close()
        

        elif ScoreD[Scorecounter] == str(1):
                TextZS = "ZS" + str(NrZS)
                with open (TextZS+'Com.txt', 'rt') as myfile:
                     for myline in myfile:
                        myl = myline.rstrip()
                        tempPPB.append(myl)
                        print("File PC open")
                with open (TextZS+'.txt', 'rt') as myfile:
                      for myline in myfile:
                        my = myline.rstrip()
                        tempPPBCom.append(my)
                        print("File P open")
                            
                for i in range(20):
                    PBDict[tempPPB[i]] = tempPPBCom[i]
                
                top = ttk.top = Toplevel()

         
                tkinter.Label(top, text=TextZS, font = 'Bold').grid(row=1,column=1)

                tkinter.Label(top, text=PBDict,borderwidth=1 ).grid(row=4,column=1)

                pass

    if NrZS == 2:
        Scorecounter = NrZS + 2
        if ScoreD[Scorecounter] == str(0):

            ScoreD[Scorecounter] = str(1)

            TextZS = "ZS" + str(NrZS)
       
            fc=open(TextZS+"Com.txt", "w+")
            PB1  = ACComList[0].get()
            PB2  = ACComList[1].get()
            PB3  = ACComList[2].get()
            PB4  = ACComList[3].get()
            PB5  = ACComList[4].get()
            PB6  = ACComList[5].get()
            PB7  = ACComList[2].get()
            PB8  = ACComList[3].get()
            PB9  = ACComList[4].get()
            PB10  = ACComList[5].get()
            PB11  = ACComList[0].get()
            PB12  = ACComList[1].get()
            PB13  = ACComList[2].get()
            PB14  = ACComList[3].get()
            PB15  = ACComList[4].get()
            PB16  = ACComList[5].get()
            PB17  = ACComList[2].get()
            PB18  = ACComList[3].get()
            PB19  = ACComList[4].get()
            PB20  = ACComList[5].get()
        
            """Add experience according to rank"""

            width = 7
            fillchar = "0"
        
            f=open(PB1+"exp.txt", "r")
            if f.mode == 'r':
                contents =f.read()
            f.close()
            PG = int(contents) + 10000
            PGfill = str(PG).rjust(width, fillchar)

            f= open(PB1+"exp.txt","w")
            f.write(PGfill)
            f.close()

            f=open(PB2+"exp.txt", "r")
            if f.mode == 'r':
                contents =f.read()
            f.close()
            PG = int(contents) + 5000
            PGfill = str(PG).rjust(width, fillchar)

            f= open(PB2+"exp.txt","w")
            f.write(PGfill)
            f.close()

            f=open(PB3+"exp.txt", "r")
            if f.mode == 'r':
                contents =f.read()
            f.close()
            PG = int(contents) + 2500
            PGfill = str(PG).rjust(width, fillchar)

            f= open(PB3+"exp.txt","w")
            f.write(PGfill)
            f.close()
        
            fc.write(str(PB1+"\n"))
            fc.write(str(PB2+"\n"))
            fc.write(str(PB3 +"\n"))
            fc.write(str(PB4+"\n"))
            fc.write(str(PB5+"\n"))
            fc.write(str(PB6 +"\n"))
            fc.write(str(PB7 +"\n"))
            fc.write(str(PB8+"\n"))
            fc.write(str(PB9+"\n"))
            fc.write(str(PB10 +"\n"))
            fc.write(str(PB11+"\n"))
            fc.write(str(PB12+"\n"))
            fc.write(str(PB13 +"\n"))
            fc.write(str(PB14+"\n"))
            fc.write(str(PB15+"\n"))
            fc.write(str(PB16 +"\n"))
            fc.write(str(PB17 +"\n"))
            fc.write(str(PB18+"\n"))
            fc.write(str(PB19+"\n"))
            fc.write(str(PB20 +"\n"))
        
            f=open(TextZS+".txt", "w+")
    
            PB1  = ACList[0].get()
            PB2  = ACList[1].get()
            PB3  = ACList[2].get()
            PB4  = ACList[3].get()
            PB5  = ACList[4].get()
            PB6  = ACList[5].get()
            PB7  = ACList[2].get()
            PB8  = ACList[3].get()
            PB9  = ACList[4].get()
            PB10  = ACList[5].get()
            PB11  = ACList[0].get()
            PB12  = ACList[1].get()
            PB13  = ACList[2].get()
            PB14  = ACList[3].get()
            PB15  = ACList[4].get()
            PB16  = ACList[5].get()
            PB17  = ACList[2].get()
            PB18  = ACList[3].get()
            PB19  = ACList[4].get()
            PB20  = ACList[5].get()

            f.write(str(PB1+"\n"))
            f.write(str(PB2+"\n"))
            f.write(str(PB3 +"\n"))
            f.write(str(PB4+"\n"))
            f.write(str(PB5+"\n"))
            f.write(str(PB6 +"\n"))
            f.write(str(PB7 +"\n"))
            f.write(str(PB8+"\n"))
            f.write(str(PB9+"\n"))
            f.write(str(PB10 +"\n"))
            f.write(str(PB11+"\n"))
            f.write(str(PB12+"\n"))
            f.write(str(PB13 +"\n"))
            f.write(str(PB14+"\n"))
            f.write(str(PB15+"\n"))
            f.write(str(PB16 +"\n"))
            f.write(str(PB17 +"\n"))
            f.write(str(PB18+"\n"))
            f.write(str(PB19+"\n"))
            f.write(str(PB20 +"\n"))                


            fp=open("SD.txt", "w+")     
            o=0
            for i in ScoreD:
                fp.write(str(ScoreD[o])+"\n")
                o = o +1
            print("File written")

            f.close()
            fp.close()
            fc.close()
        

        elif ScoreD[Scorecounter] == str(1):
                TextZS = "ZS" + str(NrZS)
                with open (TextZS+'Com.txt', 'rt') as myfile:
                     for myline in myfile:
                        myl = myline.rstrip()
                        tempPPB.append(myl)
                        print("File PC open")
                with open (TextZS+'.txt', 'rt') as myfile:
                      for myline in myfile:
                        my = myline.rstrip()
                        tempPPBCom.append(my)
                        print("File P open")
                            
                for i in range(20):
                    PBDict[tempPPB[i]] = tempPPBCom[i]
                
                top = ttk.top = Toplevel()

         
                tkinter.Label(top, text=TextZS, font = 'Bold').grid(row=1,column=1)

                tkinter.Label(top, text=PBDict,borderwidth=1 ).grid(row=4,column=1)

                pass
    if NrZS == 3:
        Scorecounter = NrZS + 2
        if ScoreD[Scorecounter] == str(0):

            ScoreD[Scorecounter] = str(1)

            TextZS = "ZS" + str(NrZS)
       
            fc=open(TextZS+"Com.txt", "w+")
            PB1  = VComList[0].get()
            PB2  = VComList[1].get()
            PB3  = VComList[2].get()
            PB4  = VComList[3].get()
            PB5  = VComList[4].get()
            PB6  = VComList[5].get()
            PB7  = VComList[2].get()
            PB8  = VComList[3].get()
            PB9  = VComList[4].get()
            PB10  = VComList[5].get()
            PB11  = VComList[0].get()
            PB12  = VComList[1].get()
            PB13  = VComList[2].get()
            PB14  = VComList[3].get()
            PB15  = VComList[4].get()
            PB16  = VComList[5].get()
            PB17  = VComList[2].get()
            PB18  = VComList[3].get()
            PB19  = VComList[4].get()
            PB20  = VComList[5].get()
        
            """Add experience according to rank"""

            width = 7
            fillchar = "0"
        
            f=open(PB1+"exp.txt", "r")
            if f.mode == 'r':
                contents =f.read()
            f.close()
            PG = int(contents) + 10000
            PGfill = str(PG).rjust(width, fillchar)

            f= open(PB1+"exp.txt","w")
            f.write(PGfill)
            f.close()

            f=open(PB2+"exp.txt", "r")
            if f.mode == 'r':
                contents =f.read()
            f.close()
            PG = int(contents) + 5000
            PGfill = str(PG).rjust(width, fillchar)

            f= open(PB2+"exp.txt","w")
            f.write(PGfill)
            f.close()

            f=open(PB3+"exp.txt", "r")
            if f.mode == 'r':
                contents =f.read()
            f.close()
            PG = int(contents) + 2500
            PGfill = str(PG).rjust(width, fillchar)

            f= open(PB3+"exp.txt","w")
            f.write(PGfill)
            f.close()
        
            fc.write(str(PB1+"\n"))
            fc.write(str(PB2+"\n"))
            fc.write(str(PB3 +"\n"))
            fc.write(str(PB4+"\n"))
            fc.write(str(PB5+"\n"))
            fc.write(str(PB6 +"\n"))
            fc.write(str(PB7 +"\n"))
            fc.write(str(PB8+"\n"))
            fc.write(str(PB9+"\n"))
            fc.write(str(PB10 +"\n"))
            fc.write(str(PB11+"\n"))
            fc.write(str(PB12+"\n"))
            fc.write(str(PB13 +"\n"))
            fc.write(str(PB14+"\n"))
            fc.write(str(PB15+"\n"))
            fc.write(str(PB16 +"\n"))
            fc.write(str(PB17 +"\n"))
            fc.write(str(PB18+"\n"))
            fc.write(str(PB19+"\n"))
            fc.write(str(PB20 +"\n"))
        
            f=open(TextZS+".txt", "w+")
    
            PB1  = VList[0].get()
            PB2  = VList[1].get()
            PB3  = VList[2].get()
            PB4  = VList[3].get()
            PB5  = VList[4].get()
            PB6  = VList[5].get()
            PB7  = VList[2].get()
            PB8  = VList[3].get()
            PB9  = VList[4].get()
            PB10  = VList[5].get()
            PB11  = VList[0].get()
            PB12  = VList[1].get()
            PB13  = VList[2].get()
            PB14  = VList[3].get()
            PB15  = VList[4].get()
            PB16  = VList[5].get()
            PB17  = VList[2].get()
            PB18  = VList[3].get()
            PB19  = VList[4].get()
            PB20  = VList[5].get()

            f.write(str(PB1+"\n"))
            f.write(str(PB2+"\n"))
            f.write(str(PB3 +"\n"))
            f.write(str(PB4+"\n"))
            f.write(str(PB5+"\n"))
            f.write(str(PB6 +"\n"))
            f.write(str(PB7 +"\n"))
            f.write(str(PB8+"\n"))
            f.write(str(PB9+"\n"))
            f.write(str(PB10 +"\n"))
            f.write(str(PB11+"\n"))
            f.write(str(PB12+"\n"))
            f.write(str(PB13 +"\n"))
            f.write(str(PB14+"\n"))
            f.write(str(PB15+"\n"))
            f.write(str(PB16 +"\n"))
            f.write(str(PB17 +"\n"))
            f.write(str(PB18+"\n"))
            f.write(str(PB19+"\n"))
            f.write(str(PB20 +"\n"))                


            fp=open("SD.txt", "w+")     
            o=0
            for i in ScoreD:
                fp.write(str(ScoreD[o])+"\n")
                o = o +1
            print("File written")

            f.close()
            fp.close()
            fc.close()
        

        elif ScoreD[Scorecounter] == str(1):
                TextZS = "ZS" + str(NrZS)
                with open (TextZS+'Com.txt', 'rt') as myfile:
                     for myline in myfile:
                        myl = myline.rstrip()
                        tempPPB.append(myl)
                        print("File PC open")
                with open (TextZS+'.txt', 'rt') as myfile:
                      for myline in myfile:
                        my = myline.rstrip()
                        tempPPBCom.append(my)
                        print("File P open")
                            
                for i in range(20):
                    PBDict[tempPPB[i]] = tempPPBCom[i]
                
                top = ttk.top = Toplevel()

         
                tkinter.Label(top, text=TextZS, font = 'Bold').grid(row=1,column=1)

                tkinter.Label(top, text=PBDict,borderwidth=1 ).grid(row=4,column=1)

                pass


"""Paintball Score"""
def PB():
    ScoreD = []
    with open ('SD.txt', 'rt') as myfile:
        for myline in myfile:
            myli = myline.rstrip()
            ScoreD.append(myli)
            print("File open")

    if ScoreD[0] == str(0):

        ScoreD[0] = str(1)
       
        fc=open("PBLCom.txt", "w+")
        PB1  = PPBComList[0].get()
        PB2  = PPBComList[1].get()
        PB3  = PPBComList[2].get()
        PB4  = PPBComList[3].get()
        PB5  = PPBComList[4].get()
        PB6  = PPBComList[5].get()
        PB7  = PPBComList[2].get()
        PB8  = PPBComList[3].get()
        PB9  = PPBComList[4].get()
        PB10  = PPBComList[5].get()
        PB11  = PPBComList[0].get()
        PB12  = PPBComList[1].get()
        PB13  = PPBComList[2].get()
        PB14  = PPBComList[3].get()
        PB15  = PPBComList[4].get()
        PB16  = PPBComList[5].get()
        PB17  = PPBComList[2].get()
        PB18  = PPBComList[3].get()
        PB19  = PPBComList[4].get()
        PB20  = PPBComList[5].get()
        
        """Add experience according to rank"""

        width = 7
        fillchar = "0"
        
        f=open(PB1+"exp.txt", "r")
        if f.mode == 'r':
            contents =f.read()
        f.close()
        PG = int(contents) + 10000
        PGfill = str(PG).rjust(width, fillchar)

        f= open(PB1+"exp.txt","w")
        f.write(PGfill)
        f.close()

        f=open(PB2+"exp.txt", "r")
        if f.mode == 'r':
            contents =f.read()
        f.close()
        PG = int(contents) + 5000
        PGfill = str(PG).rjust(width, fillchar)

        f= open(PB2+"exp.txt","w")
        f.write(PGfill)
        f.close()

        f=open(PB3+"exp.txt", "r")
        if f.mode == 'r':
            contents =f.read()
        f.close()
        PG = int(contents) + 2500
        PGfill = str(PG).rjust(width, fillchar)

        f= open(PB3+"exp.txt","w")
        f.write(PGfill)
        f.close()
        
        fc.write(str(PB1+"\n"))
        fc.write(str(PB2+"\n"))
        fc.write(str(PB3 +"\n"))
        fc.write(str(PB4+"\n"))
        fc.write(str(PB5+"\n"))
        fc.write(str(PB6 +"\n"))
        fc.write(str(PB7 +"\n"))
        fc.write(str(PB8+"\n"))
        fc.write(str(PB9+"\n"))
        fc.write(str(PB10 +"\n"))
        fc.write(str(PB11+"\n"))
        fc.write(str(PB12+"\n"))
        fc.write(str(PB13 +"\n"))
        fc.write(str(PB14+"\n"))
        fc.write(str(PB15+"\n"))
        fc.write(str(PB16 +"\n"))
        fc.write(str(PB17 +"\n"))
        fc.write(str(PB18+"\n"))
        fc.write(str(PB19+"\n"))
        fc.write(str(PB20 +"\n"))
        
        f=open("PBL.txt", "w+")

        PB1  = PPBList[0].get()
        PB2  = PPBList[1].get()
        PB3  = PPBList[2].get()
        PB4  = PPBList[3].get()
        PB5  = PPBList[4].get()
        PB6  = PPBList[5].get()
        PB7  = PPBList[2].get()
        PB8  = PPBList[3].get()
        PB9  = PPBList[4].get()
        PB10  = PPBList[5].get()
        PB11  = PPBList[0].get()
        PB12  = PPBList[1].get()
        PB13  = PPBList[2].get()
        PB14  = PPBList[3].get()
        PB15  = PPBList[4].get()
        PB16  = PPBList[5].get()
        PB17  = PPBList[2].get()
        PB18  = PPBList[3].get()
        PB19  = PPBList[4].get()
        PB20  = PPBList[5].get()

        f.write(str(PB1+"\n"))
        f.write(str(PB2+"\n"))
        f.write(str(PB3 +"\n"))
        f.write(str(PB4+"\n"))
        f.write(str(PB5+"\n"))
        f.write(str(PB6 +"\n"))
        f.write(str(PB7 +"\n"))
        f.write(str(PB8+"\n"))
        f.write(str(PB9+"\n"))
        f.write(str(PB10 +"\n"))
        f.write(str(PB11+"\n"))
        f.write(str(PB12+"\n"))
        f.write(str(PB13 +"\n"))
        f.write(str(PB14+"\n"))
        f.write(str(PB15+"\n"))
        f.write(str(PB16 +"\n"))
        f.write(str(PB17 +"\n"))
        f.write(str(PB18+"\n"))
        f.write(str(PB19+"\n"))
        f.write(str(PB20 +"\n"))                


        fp=open("SD.txt", "w+")     
        o=0
        for i in ScoreD:
            fp.write(str(ScoreD[o])+"\n")
            o = o +1
        print("File written")

        f.close()
        fp.close()
        fc.close()
       
    elif ScoreD[0] == str(1):
        with open ('PBLCom.txt', 'rt') as myfile:
            for myline in myfile:
                myl = myline.rstrip()
                tempPPB.append(myl)
                print("File PC open")
        with open ('PBL.txt', 'rt') as myfile:
            for myline in myfile:
                my = myline.rstrip()
                tempPPBCom.append(my)
                print("File P open")
        for i in range(20):
            PBDict[tempPPB[i]] = tempPPBCom[i]
                
        top = ttk.top = Toplevel()

         
        tkinter.Label(top, text="Paintball Winners", font = 'Bold').grid(row=1,column=1)

        tkinter.Label(top, text=PBDict,borderwidth=1 ).grid(row=4,column=1)

        pass

"""AlpenChallengeScore""" 
def AC():
    ScoreD = []
    with open ('SD.txt', 'rt') as myfile:
        for myline in myfile:
            myli = myline.rstrip()
            ScoreD.append(myli)
            print("File open")

    if ScoreD[1] == str(0):

        ScoreD[1] = str(1)
       
        fc=open("ACCom.txt", "w+")
        PB1  = ACComList[0].get()
        PB2  = ACComList[1].get()
        PB3  = ACComList[2].get()
        PB4  = ACComList[3].get()
        PB5  = ACComList[4].get()
        PB6  = ACComList[5].get()
        PB7  = ACComList[2].get()
        PB8  = ACComList[3].get()
        PB9  = ACComList[4].get()
        PB10  = ACComList[5].get()
        PB11  = ACComList[0].get()
        PB12  = ACComList[1].get()
        PB13  = ACComList[2].get()
        PB14  = ACComList[3].get()
        PB15  = ACComList[4].get()
        PB16  = ACComList[5].get()
        PB17  = ACComList[2].get()
        PB18  = ACComList[3].get()
        PB19  = ACComList[4].get()
        PB20  = ACComList[5].get()

        """Add experience according to rank"""
        width = 7
        fillchar = "0"
        
        f=open(PB1+"exp.txt", "r")
        if f.mode == 'r':
            contents =f.read()
        f.close()
        PG = int(contents) + 10000
        PGfill = str(PG).rjust(width, fillchar)

        f= open(PB1+"exp.txt","w")
        f.write(PGfill)
        f.close()

        f=open(PB2+"exp.txt", "r")
        if f.mode == 'r':
            contents =f.read()
        f.close()
        PG = int(contents) + 5000
        PGfill = str(PG).rjust(width, fillchar)

        f= open(PB2+"exp.txt","w")
        f.write(PGfill)
        f.close()

        f=open(PB3+"exp.txt", "r")
        if f.mode == 'r':
            contents =f.read()
        f.close()
        PG = int(contents) + 2500
        PGfill = str(PG).rjust(width, fillchar)

        f= open(PB3+"exp.txt","w")
        f.write(PGfill)
        f.close()


        

        fc.write(str(PB1+"\n"))
        fc.write(str(PB2+"\n"))
        fc.write(str(PB3 +"\n"))
        fc.write(str(PB4+"\n"))
        fc.write(str(PB5+"\n"))
        fc.write(str(PB6 +"\n"))
        fc.write(str(PB7 +"\n"))
        fc.write(str(PB8+"\n"))
        fc.write(str(PB9+"\n"))
        fc.write(str(PB10 +"\n"))
        fc.write(str(PB11+"\n"))
        fc.write(str(PB12+"\n"))
        fc.write(str(PB13 +"\n"))
        fc.write(str(PB14+"\n"))
        fc.write(str(PB15+"\n"))
        fc.write(str(PB16 +"\n"))
        fc.write(str(PB17 +"\n"))
        fc.write(str(PB18+"\n"))
        fc.write(str(PB19+"\n"))
        fc.write(str(PB20 +"\n"))
        
        f=open("AC.txt", "w+")

        PB1  = ACList[0].get()
        PB2  = ACList[1].get()
        PB3  = ACList[2].get()
        PB4  = ACList[3].get()
        PB5  = ACList[4].get()
        PB6  = ACList[5].get()
        PB7  = ACList[2].get()
        PB8  = ACList[3].get()
        PB9  = ACList[4].get()
        PB10  = ACList[5].get()
        PB11  = ACList[0].get()
        PB12  = ACList[1].get()
        PB13  = ACList[2].get()
        PB14  = ACList[3].get()
        PB15  = ACList[4].get()
        PB16  = ACList[5].get()
        PB17  = ACList[2].get()
        PB18  = ACList[3].get()
        PB19  = ACList[4].get()
        PB20  = ACList[5].get()

        f.write(str(PB1+"\n"))
        f.write(str(PB2+"\n"))
        f.write(str(PB3 +"\n"))
        f.write(str(PB4+"\n"))
        f.write(str(PB5+"\n"))
        f.write(str(PB6 +"\n"))
        f.write(str(PB7 +"\n"))
        f.write(str(PB8+"\n"))
        f.write(str(PB9+"\n"))
        f.write(str(PB10 +"\n"))
        f.write(str(PB11+"\n"))
        f.write(str(PB12+"\n"))
        f.write(str(PB13 +"\n"))
        f.write(str(PB14+"\n"))
        f.write(str(PB15+"\n"))
        f.write(str(PB16 +"\n"))
        f.write(str(PB17 +"\n"))
        f.write(str(PB18+"\n"))
        f.write(str(PB19+"\n"))
        f.write(str(PB20 +"\n"))                


        fp=open("SD.txt", "w+")     
        o=0
        for i in ScoreD:
            fp.write(str(ScoreD[o])+"\n")
            o = o +1
        print("File written")

        f.close()
        fp.close()
        fc.close()
       
    elif ScoreD[1] == str(1):
        with open ('ACCom.txt', 'rt') as myfile:
            for myline in myfile:
                myl = myline.rstrip()
                tempPPB.append(myl)
                print("File PC open")
        with open ('AC.txt', 'rt') as myfile:
            for myline in myfile:
                my = myline.rstrip()
                tempPPBCom.append(my)
                print("File P open")
        for i in range(20):
            PBDict[tempPPB[i]] = tempPPBCom[i]
                
        top = ttk.top = Toplevel()

         
        tkinter.Label(top, text="AlpenChallenge Winners", font = 'Bold').grid(row=1,column=1)
        tkinter.Label(top, text=PBDict,borderwidth=1 ).grid(row=4,column=1)

        pass

"""Varia Score"""
def V():
    ScoreD = []
    with open ('SD.txt', 'rt') as myfile:
        for myline in myfile:
            myli = myline.rstrip()
            ScoreD.append(myli)
            print("File open")

    if ScoreD[2] == str(0):

        ScoreD[2] = str(1)
       
        fc=open("VCom.txt", "w+")
        PB1  = VComList[0].get()
        PB2  = VComList[1].get()
        PB3  = VComList[2].get()
        PB4  = VComList[3].get()
        PB5  = VComList[4].get()
        PB6  = VComList[5].get()
        PB7  = VComList[2].get()
        PB8  = VComList[3].get()
        PB9  = VComList[4].get()
        PB10  = VComList[5].get()
        PB11  = VComList[0].get()
        PB12  = VComList[1].get()
        PB13  = VComList[2].get()
        PB14  = VComList[3].get()
        PB15  = VComList[4].get()
        PB16  = VComList[5].get()
        PB17  = VComList[2].get()
        PB18  = VComList[3].get()
        PB19  = VComList[4].get()
        PB20  = VComList[5].get()

        """Add experience according to rank"""
        width = 7
        fillchar = "0"
        
        f=open(PB1+"exp.txt", "r")
        if f.mode == 'r':
            contents =f.read()
        f.close()
        PG = int(contents) + 10000
        PGfill = str(PG).rjust(width, fillchar)

        f= open(PB1+"exp.txt","w")
        f.write(PGfill)
        f.close()

        f=open(PB2+"exp.txt", "r")
        if f.mode == 'r':
            contents =f.read()
        f.close()
        PG = int(contents) + 5000
        PGfill = str(PG).rjust(width, fillchar)

        f= open(PB2+"exp.txt","w")
        f.write(PGfill)
        f.close()

        f=open(PB3+"exp.txt", "r")
        if f.mode == 'r':
            contents =f.read()
        f.close()
        PG = int(contents) + 2500
        PGfill = str(PG).rjust(width, fillchar)

        f= open(PB3+"exp.txt","w")
        f.write(PGfill)
        f.close()
        

        fc.write(str(PB1+"\n"))
        fc.write(str(PB2+"\n"))
        fc.write(str(PB3 +"\n"))
        fc.write(str(PB4+"\n"))
        fc.write(str(PB5+"\n"))
        fc.write(str(PB6 +"\n"))
        fc.write(str(PB7 +"\n"))
        fc.write(str(PB8+"\n"))
        fc.write(str(PB9+"\n"))
        fc.write(str(PB10 +"\n"))
        fc.write(str(PB11+"\n"))
        fc.write(str(PB12+"\n"))
        fc.write(str(PB13 +"\n"))
        fc.write(str(PB14+"\n"))
        fc.write(str(PB15+"\n"))
        fc.write(str(PB16 +"\n"))
        fc.write(str(PB17 +"\n"))
        fc.write(str(PB18+"\n"))
        fc.write(str(PB19+"\n"))
        fc.write(str(PB20 +"\n"))
        
        f=open("V.txt", "w+")

        PB1  = VList[0].get()
        PB2  = VList[1].get()
        PB3  = VList[2].get()
        PB4  = VList[3].get()
        PB5  = VList[4].get()
        PB6  = VList[5].get()
        PB7  = VList[2].get()
        PB8  = VList[3].get()
        PB9  = VList[4].get()
        PB10  = VList[5].get()
        PB11  = VList[0].get()
        PB12  = VList[1].get()
        PB13  = VList[2].get()
        PB14  = VList[3].get()
        PB15  = VList[4].get()
        PB16  = VList[5].get()
        PB17  = VList[2].get()
        PB18  = VList[3].get()
        PB19  = VList[4].get()
        PB20  = VList[5].get()

        f.write(str(PB1+"\n"))
        f.write(str(PB2+"\n"))
        f.write(str(PB3 +"\n"))
        f.write(str(PB4+"\n"))
        f.write(str(PB5+"\n"))
        f.write(str(PB6 +"\n"))
        f.write(str(PB7 +"\n"))
        f.write(str(PB8+"\n"))
        f.write(str(PB9+"\n"))
        f.write(str(PB10 +"\n"))
        f.write(str(PB11+"\n"))
        f.write(str(PB12+"\n"))
        f.write(str(PB13 +"\n"))
        f.write(str(PB14+"\n"))
        f.write(str(PB15+"\n"))
        f.write(str(PB16 +"\n"))
        f.write(str(PB17 +"\n"))
        f.write(str(PB18+"\n"))
        f.write(str(PB19+"\n"))
        f.write(str(PB20 +"\n"))                


        fp=open("SD.txt", "w+")     
        o=0
        for i in ScoreD:
            fp.write(str(ScoreD[o])+"\n")
            o = o +1
        print("File written")

        f.close()
        fp.close()
        fc.close()
       
    elif ScoreD[2] == str(1):
        with open ('VCom.txt', 'rt') as myfile:
            for myline in myfile:
                myl = myline.rstrip()
                tempPPB.append(myl)
                print("File PC open")
        with open ('V.txt', 'rt') as myfile:
            for myline in myfile:
                my = myline.rstrip()
                tempPPBCom.append(my)
                print("File P open")
        for i in range(20):
            PBDict[tempPPB[i]] = tempPPBCom[i]
                
        top = ttk.top = Toplevel()

         
        tkinter.Label(top, text="Varia Winners", font = 'Bold').grid(row=1,column=1)
        tkinter.Label(top, text=PBDict,borderwidth=1 ).grid(row=4,column=1)

        pass
def go(top):
    print ("my work here is done")
    top.destroy()

    


def takeSecond(elem):
    return elem[1]

def ListAll():
    """ """
    mylines = []
    mylinesEXP = []
    myDict = {}
    ListVal = []
    with open ('PLL.txt', 'rt') as myfile:
        for myline in myfile:
            myl = myline.rstrip()
            print(myl)
            if myl == "":
                pass
            else:
                f=open(myl + 'exp.txt', 'r')
                if f.mode == 'r':
                    contents =f.read()
                    print(contents)

                    for e in mylinesEXP:
                        if contents == e:
                            contents = int(contents) +1
                    con = str(contents)
                    mylinesEXP.append(con)
                f.close()            
                mylines.append(myline)

                myDict = {"Name":myl, "Score":con}
                print (myDict)

                ListVal.append((myl,con))

    """print (ListVal)"""
    ListVal.sort( key=takeSecond)

    messagebox.showinfo("All souls", ListVal)    
    print (ListVal)


    """p = 0    
    for l in mylines:
        myDict[mylinesEXP[p]] = mylines[p]
        p = p + 1
    print(myDict)
    for key, value in sorted(myDict.items()):
        print(key, value)
    KDY = sorted(ListVal(), key=itemgetter(1), reverse=True)
    print (KDY)"""

def calc():
    """ """
    PLRZ = []
    EXPPLRZ = []
    SrcExp = []
    with open ('PLL.txt', 'rt') as myfile:
        for myline in myfile:
            PLRZ.append(myline)
            print(myline)
            
    cntr = 0
    for xx in PLRZ:
        PLZ = str(PLRZ[cntr]).rstrip()
        print(PLZ)

        if PLZ == "":
            pass
        else:
            f=open(PLZ+"exp.txt", "r")
            if f.mode == 'r':
                contents =f.read()
                con=str(contents)
                EXPPLRZ.append(con)
                SrcExp.append(con)
                cntr = cntr + 1
                print(contents)

    
    
    go1 = max(EXPPLRZ)
    EXPPLRZ.remove(max(EXPPLRZ))
    go2 = max(EXPPLRZ)
    EXPPLRZ.remove(max(EXPPLRZ))
    go3 = max(EXPPLRZ)

    gol1 = SrcExp.index(go1)
    gold1 = PLRZ[gol1]
    gol2 = SrcExp.index(go2)
    gold2 = PLRZ[gol2]
    gol3 = SrcExp.index(go3)
    gold3 = PLRZ[gol3]
    
    G1.configure(text = gold1)
    G2.configure(text = gold2)
    G3.configure(text = gold3)
            
"""define ChooseWeapon"""
def chW():
    WGXX = GXX5.get()
    WINDXX = WName.index(WGXX)
    Wspot = WINDXX

    StartA = Atr21.cget("text")
    a = AD.cget("text")
    if a == "":
        messagebox.showinfo("Info", "You have no player selected")
    

    if a != StartA:
        a = StartA

    d = AD2.cget("text")

    aN = int(a)

    if WINDXX == 1:
        AddedAttack[0] =  100
        Sat = 0
        for n in AddedAttack:
            Sat = Sat + n
        aN = aN + Sat
        AD.configure(text = str(aN))
        Atr1.configure(text = "")    
        Atr2.configure(text = "II. You enflame or encase your enemy in ice.")
        Atr3.configure(text = "")
    elif WINDXX == 0:
        AddedAttack[0] =  500
        Sat = 0
        for n in AddedAttack:
            Sat = Sat + n
        aN = aN + Sat
        AD.configure(text = str(aN))
        Atr1.configure(text = "I. You have a chance to clobber an opponent in a single blow.")
        Atr2.configure(text = "")
        Atr3.configure(text = "") 
    elif WINDXX == 2:
        AddedAttack[0] =  1000
        Sat = 0
        for n in AddedAttack:
            Sat = Sat + n
            print(Sat, n, aN)
        aN = aN + Sat
        Atr1.configure(text = "")    
        Atr2.configure(text = "")
        Atr3.configure(text = "III.You control the world with a single touch on your screen.")
        AD.configure(text = str(aN))
        
   
    a = AD.cget("text")
    d = AD2.cget("text")
        
    Atr24.configure(text = a)
    Atr25.configure(text = d)

    avddd =str(a)+ "/" + str(d)

    AD3.configure(text = avddd)
    
    PicCl = ["orcf.png", "archer.png", "mage.png", "necro.png", "bard.png", "joker.png", "wanderer.png"]
    Cla = Clbl.get()
    ClaX = Cla.rstrip()    
    CIND = Classes.index(ClaX)

    try:
        image = Image.open(PicCl[CIND])
        photo = ImageTk.PhotoImage(image)
    
        imglabel1 = Label(page1, image = photo).grid(row=2, column=1)
   
        imglabel1.image = photo
    
        imglabel1.pack()
    finally: 

        """ """    
        global wind
        wind = Toplevel()
        if wind is not None:
            wind.destroy()      
        try:
            top = ttk.top = Toplevel()
            """Label(top, text="Value").grid()"""
            imgQ = PhotoImage(file=Weapons[WINDXX])
            imglabelQ = Label(top, image = imgQ).grid(row=5, column=2)
            imglabelQ.config(top, image =imgQ)
        finally:
    
            """ """

   



   

"""define ChooseHelmet"""
def chH():
    WGXXH = GXX.get()
    WINDXXH = HName.index(WGXXH)
    Hspot = WINDXXH
	
    StartA = Atr21.cget("text")	
    StartD = Atr22.cget("text")
    a = AD.cget("text")
    if a == "":
        messagebox.showinfo("Info", "You have no player selected")
 
    if a != StartA:
        a = StartA

    d = AD2.cget("text")

    if d != StartD:
        d = StartD

    aN = int(a)
    dN = int(d)

    if WINDXXH == 0:
        AddedDefense[1] =  10
        Sat = 0
        for n in AddedDefense:
            Sat = Sat + n
        dN = dN + Sat

        Atr4.configure(text = "IV. Met een paar bollen ben je in lalaland.")
        Atr5.configure(text = "")
        Atr6.configure(text = "")
        AD2.configure(text = str(dN))
    elif WINDXXH == 1:
        AddedDefense[1] = 50
        Sat = 0
        for n in AddedDefense:
            Sat = Sat + n
        dN = dN + Sat

        Atr4.configure(text = "")    
        Atr5.configure(text = "V. More beer, here.")
        Atr6.configure(text = "")
        AD2.configure(text = str(dN))
    elif WINDXXH == 2:
        AddedDefense[1] =  100
        Sat = 0
        for n in AddedDefense:
            Sat = Sat + n
            print(Sat, n, aN)
        dN = dN + Sat
        Atr4.configure(text = "")    
        Atr5.configure(text = "")
        Atr6.configure(text = "VI. Aye! ")
        AD2.configure(text = str(dN))
        
   
    a = AD.cget("text")
    d = AD2.cget("text")
        
    Atr24.configure(text = a)
    Atr25.configure(text = d)

    avddd =str(a)+ "/" + str(d)

    AD3.configure(text = avddd)
    
    PicCl = ["orcf.png", "archer.png", "mage.png", "necro.png", "bard.png", "joker.png", "wanderer.png"]
    Cla = Clbl.get()
    ClaX = Cla.rstrip()    
    CIND = Classes.index(ClaX)

    try:
        image = Image.open(PicCl[CIND])
        photo = ImageTk.PhotoImage(image)
    
        imglabel1 = Label(page1, image = photo).grid(row=2, column=1)
   
        imglabel1.image = photo
    
        imglabel1.pack()
    finally: 

        """ """    
        global wind
        wind = Toplevel()
        if wind is not None:
            wind.destroy()     
        try:
            top = ttk.top = Toplevel()
            """Label(top, text="Value").grid()"""
            imgQ = PhotoImage(file=Helmets[WINDXXH])
            imglabelQ = Label(top, image = imgQ).grid(row=5, column=2)
            imglabelQ.config(top, image =imgQ)
        finally:
    
            """ """


"""define ChooseArmor"""
def chA():
    WGXXA = GXX1.get()
    WINDXXA = AName.index(WGXXA)
    Aspot = WINDXXA
	
    StartA = Atr21.cget("text")	
    StartD = Atr22.cget("text")
    a = AD.cget("text")
    if a == "":
        messagebox.showinfo("Info", "You have no player selected")
    if a != StartA:
        a = StartA

    d = AD2.cget("text")

    if d != StartD:
        d = StartD

    aN = int(a)
    dN = int(d)

    if WINDXXA== 1:
        AddedDefense[2] =  100
        Sat = 0
        for n in AddedDefense:
            Sat = Sat + n
        dN = dN + Sat
        Atr7.configure(text = "")    
        Atr8.configure(text = "VIII. Normaly only on sundays.")
        Atr9.configure(text = "")
        AD2.configure(text = str(dN))
    elif WINDXXA== 0:
        AddedDefense[2] = 1000 
        Sat = 0
        for n in AddedDefense:
            Sat = Sat + n
        dN = dN + Sat
        Atr7.configure(text = "VII. Either you killed the dragon or bought this from a merchant.")
        Atr8.configure(text = "")
        Atr9.configure(text = "") 

        AD2.configure(text = str(dN))
    elif WINDXXA== 2:
        AddedDefense[2] =  500
        Sat = 0
        for n in AddedDefense:
            Sat = Sat + n
            print(Sat, n, aN)
        dN = dN + Sat
        Atr7.configure(text = "")    
        Atr8.configure(text = "")
        Atr9.configure(text = "IX. Mosh Pit. ")
        AD2.configure(text = str(dN))
        
   
    a = AD.cget("text")
    d = AD2.cget("text")
        
    Atr24.configure(text = a)
    Atr25.configure(text = d)

    avddd =str(a)+ "/" + str(d)

    AD3.configure(text = avddd)
    
    PicCl = ["orcf.png", "archer.png", "mage.png", "necro.png", "bard.png", "joker.png", "wanderer.png"]
    Cla = Clbl.get()
    ClaX = Cla.rstrip()    
    CIND = Classes.index(ClaX)

    try:
        image = Image.open(PicCl[CIND])
        photo = ImageTk.PhotoImage(image)
    
        imglabel1 = Label(page1, image = photo).grid(row=2, column=1)
   
        imglabel1.image = photo
    
        imglabel1.pack()
    finally: 

        """ """    
        global wind
        wind = Toplevel()
        if wind is not None:
            wind.destroy()      
        try:
            top = ttk.top = Toplevel()
            imgA = PhotoImage(file=Armors[WINDXXA])
            imglabelQA = Label(top, image = imgA).grid(row=5, column=3)
            imglabelQA.config(top, image =imgA)
        finally:
    
            """ """

   



"""define Choosehield"""
def chS():
   
    WGXXS = GXX4.get()
    WINDXXS = SName.index(WGXXS)
    Sspot = WINDXXS
	
    StartA = Atr21.cget("text")	
    StartD = Atr22.cget("text")
    a = AD.cget("text")
    if a == "":
        messagebox.showinfo("Info", "You have no player selected")
    if a != StartA:
        a = StartA

    d = AD2.cget("text")

    if d != StartD:
        d = StartD

    aN = int(a)
    dN = int(d)

    if WINDXXS == 0:
        AddedDefense[3] =  50
        Sat = 0
        for n in AddedDefense:
            Sat = Sat + n
        dN = dN + Sat
        Atr10.configure(text = "X. No hacker will harm you. Do they ever?.")
        Atr11.configure(text = "")
        Atr12.configure(text = "") 
        AD2.configure(text = str(dN))
    elif WINDXXS == 1:
        AddedDefense[3] = 500
        Sat = 0
        for n in AddedDefense:
            Sat = Sat + n
        dN = dN + Sat
        Atr10.configure(text = "")    
        Atr11.configure(text = "XI. For some serious ass-whoopin..")
        Atr12.configure(text = "")
        AD2.configure(text = str(dN))
    elif WINDXXS == 2:
        AddedDefense[3] =  1
        Sat = 0
        for n in AddedDefense:
            Sat = Sat + n
            print(Sat, n, aN)
        dN = dN + Sat
        Atr10.configure(text = "")    
        Atr11.configure(text = "")
        Atr12.configure(text = "XII. Ad Fundum! Ad Fundum! Ad Fundum! ")
        AD2.configure(text = str(dN))
        
   
    a = AD.cget("text")
    d = AD2.cget("text")
        
    Atr24.configure(text = a)
    Atr25.configure(text = d)

    avddd =str(a)+ "/" + str(d)

    AD3.configure(text = avddd)
    
    PicCl = ["orcf.png", "archer.png", "mage.png", "necro.png", "bard.png", "joker.png", "wanderer.png"]
    Cla = Clbl.get()
    ClaX = Cla.rstrip()    
    CIND = Classes.index(ClaX)

    try:
        image = Image.open(PicCl[CIND])
        photo = ImageTk.PhotoImage(image)
    
        imglabel1 = Label(page1, image = photo).grid(row=2, column=1)
   
        imglabel1.image = photo
    
        imglabel1.pack()
    finally: 

        """ """
        global wind
        wind = Toplevel()
        if wind is not None:
            wind.destroy()    
        try:
            top = ttk.top = Toplevel()
            imgS = PhotoImage(file=Shields[WINDXXS])
            imglabelQS = Label(top, image = imgS).grid(row=5, column=4)
            imglabelQS.config(top, image =imgS)
        finally:
    
            """ """

   




"""define ChoosePants"""
def chP():

    WGXXP = GXX2.get()
    WINDXXP = PName.index(WGXXP)
    Pspot = WINDXXP
	
    StartA = Atr21.cget("text")	
    StartD = Atr22.cget("text")
    a = AD.cget("text")
    if a == "":
        messagebox.showinfo("Info", "You have no player selected")
    if a != StartA:
        a = StartA

    d = AD2.cget("text")

    if d != StartD:
        d = StartD

    aN = int(a)
    dN = int(d)

    if WINDXXP == 0:
        AddedDefense[4] =  150
        Sat = 0
        for n in AddedDefense:
            Sat = Sat + n
        dN = dN + Sat
        Atr13.configure(text = "XIII. Liar liar, pants on fire.")
        Atr14.configure(text = "")
        Atr15.configure(text = "") 
        AD2.configure(text = str(dN))
    elif WINDXXP == 1:
        AddedDefense[4] = 5
        Sat = 0
        for n in AddedDefense:
            Sat = Sat + n
        dN = dN + Sat
        Atr13.configure(text = "")    
        Atr14.configure(text = "XIV. Your classic jeans.")
        Atr15.configure(text = "")
        AD2.configure(text = str(dN))
    elif WINDXXP == 2:
        AddedDefense[4] =  10
        Sat = 0
        for n in AddedDefense:
            Sat = Sat + n
            print(Sat, n, aN)
        dN = dN + Sat
        Atr13.configure(text = "")    
        Atr14.configure(text = "")
        Atr15.configure(text = "XV. It's for aerodynamica! ")
        AD2.configure(text = str(dN))
        
   
    a = AD.cget("text")
    d = AD2.cget("text")
        
    Atr24.configure(text = a)
    Atr25.configure(text = d)

    avddd =str(a)+ "/" + str(d)

    AD3.configure(text = avddd)
    
    PicCl = ["orcf.png", "archer.png", "mage.png", "necro.png", "bard.png", "joker.png", "wanderer.png"]
    Cla = Clbl.get()
    ClaX = Cla.rstrip()    
    CIND = Classes.index(ClaX)

    try:
        image = Image.open(PicCl[CIND])
        photo = ImageTk.PhotoImage(image)
    
        imglabel1 = Label(page1, image = photo).grid(row=2, column=1)
   
        imglabel1.image = photo
    
        imglabel1.pack()
    finally: 

        """ """
        global wind
        wind = Toplevel()
        if wind is not None:
            wind.destroy()     
        try:
            top = ttk.top = Toplevel()
            imgPa = PhotoImage(file=Pants[WINDXXP])
            imglabelQP = Label(top, image = imgPa).grid(row=6, column=3)
            imglabelQP.config(top, image =imgPa)
        finally:
    
            """ """

"""define ChooseBoots"""
def chB():
   
    WGXXB = GXX3.get()
    WINDXXB = BName.index(WGXXB)
    Bspot = WINDXXB

    StartA = Atr21.cget("text")
    a = AD.cget("text")
    if a == "":
        messagebox.showinfo("Info", "You have no player selected")
    if a != StartA:
        a = StartA

    d = AD2.cget("text")

    aN = int(a)

    if WINDXXB == 0:
        AddedAttack[5] =  250
        Sat = 0
        for n in AddedAttack:
            Sat = Sat + n
        aN = aN + Sat
        AD.configure(text = str(aN))
        Atr16.configure(text = "XVI. Fuck me boots. What else?")
        Atr17.configure(text = "")
        Atr18.configure(text = "") 
    elif WINDXXB == 1:
        AddedAttack[5] =  1000
        Sat = 0
        for n in AddedAttack:
            Sat = Sat + n
        aN = aN + Sat
        AD.configure(text = str(aN))
        Atr16.configure(text = "")    
        Atr17.configure(text = "XVII. You're in for the blood.")
        Atr18.configure(text = "")
    elif WINDXXB == 2:
        AddedAttack[5] =  750
        Sat = 0
        for n in AddedAttack:
            Sat = Sat + n
            print(Sat, n, aN)
        aN = aN + Sat
        Atr16.configure(text = "")    
        Atr17.configure(text = "")
        Atr18.configure(text = "XVIII. If heaven had a half-pipe. ") 
        AD.configure(text = str(aN))
        
   
    a = AD.cget("text")
    d = AD2.cget("text")
        
    Atr24.configure(text = a)
    Atr25.configure(text = d)

    avddd =str(a)+ "/" + str(d)

    AD3.configure(text = avddd)
    
    PicCl = ["orcf.png", "archer.png", "mage.png", "necro.png", "bard.png", "joker.png", "wanderer.png"]
    Cla = Clbl.get()
    ClaX = Cla.rstrip()    
    CIND = Classes.index(ClaX)

    try:
        image = Image.open(PicCl[CIND])
        photo = ImageTk.PhotoImage(image)
    
        imglabel1 = Label(page1, image = photo).grid(row=2, column=1)
   
        imglabel1.image = photo
    
        imglabel1.pack()
    finally: 

        """ """
        global wind
        wind = Toplevel()
        if wind is not None:
            wind.destroy()



      
        try:
            top = ttk.top = Toplevel()
            imgB = PhotoImage(file=Boots[WINDXXB])
            imglabelQB = Label(top, image = imgB).grid(row=7, column=3)
            imglabelQB.config(top, image =imgB)
        finally:
    
            """ """

   




    
        
"""functie Show"""
"""["Warrior", "Archer", "Mage", "Necromancer", "Bard", "Jester", "Wanderer"]"""
def ca():

    ABX.delete(0, END)
    
    VATT = [100, 50, 25, 25, 5, 5, 50]
    VDEF = [75, 50, 25, 25, 5, 5, 50]
    VMAG = [10, 25, 100, 100, 25, 25, 10]
    VDEX = [25, 100, 25, 25, 50, 50, 50]
    VDRI = [100, 100, 50, 50, 100, 100, 100]
    VJES = [50, 75, 50, 0, 80, 100, 75]

    PicCl = ["orcf.png", "archer.png", "mage.png", "necro.png", "bard.png", "joker.png", "wanderer.png"]

    ClaX = Clbl.get()
    CIND = Classes.index(ClaX)

    A2 = VATT[CIND] 
    LB2.configure(text = A2)
    A3 = VDEF[CIND] 
    LB3.configure(text = A3)
    A4 = VMAG[CIND] 
    LB4.configure(text = A4)
    A5 = VDEX[CIND] 
    LB5.configure(text = A5)
    A6 = VDRI[CIND] 
    LB6.configure(text = A6)
    A7 = VJES[CIND] 
    LB7.configure(text = A7)

    
    try:
        LoreBase = LB
        LoreBase()
    finally:
        """ """
        
    try:
        image = Image.open(PicCl[CIND])
        photo = ImageTk.PhotoImage(image)
    
        imglabel1 = Label(page1, image = photo).grid(row=2, column=1)
   
        imglabel1.image = photo
    
        imglabel1.pack()
    finally: 
          
        print(ClaX)


    
"""functie New"""
def callback():
    Clbl.delete(0, "")
    LB2.configure(text = "")
    LB3.configure(text = "")
    LB4.configure(text = "")
    LB5.configure(text = "")
    LB6.configure(text = "")
    LB7.configure(text = "")
    
    ABX.delete(0, END)

"""functie Get"""
def call():
    SN11 = ABX.get()
    f=open(SN11+"exp.txt", "r")
    if f.mode == 'r':
        contents =f.read()
    f.close()
    if int(contents) > 50000:
        WName.append("Ultimate Nullifier")
        print(WName)
    """GXX5 = ttk.Combobox(page3, values= WName )"""
    
        
    N = ABX.get()
    N1 = N.rstrip()
    
    mylines = []
    with open (N1+'.txt', 'rt') as myfile:
        for myline in myfile:
            mylines.append(myline)
    """PlayerDict["Pierre"]["Class"]"""

    Clbl.set("")
    A0 = mylines[0]
    Clbl.insert(0, A0)
    """A1 = mylines[1] 
    ABX.insert(0, str(A1))"""
    A2 = mylines[2] 
    LB2.configure(text = A2)
    A3 = mylines[3] 
    LB3.configure(text = A3)
    A4 = mylines[4] 
    LB4.configure(text = A4)
    A5 = mylines[5] 
    LB5.configure(text = A5)
    A6 = mylines[6] 
    LB6.configure(text = A6)
    A7 = mylines[7] 
    LB7.configure(text = A7)

    ValueAttack = int(A2)+int(A4)+(int(A5)/2)+(int(A6)/4)
    ValueDef = int(A3)+int(A4)+(int(A5)/2)+(int(A7)/2)-(int(A6)/4)
  
    A = ValueAttack
    D = ValueDef
    
    AVD =str(A )+ "/" + str(D)
    AD.configure(text = A)
    AD2.configure(text = D)
    AD3.configure(text = AVD)

    Atr21.configure(text = A)
    Atr22.configure(text = D)

    PicCl = ["orcf.png", "archer.png", "mage.png", "necro.png", "bard.png", "joker.png", "wanderer.png"]

    
    
    Cla = Clbl.get()
    ClaX = Cla.rstrip()    
    CIND = Classes.index(ClaX)
    
    LoreBase = LB
    try:
        LoreBase()
    finally:
        """ """
        
    try:
        image = Image.open(PicCl[CIND])
        photo = ImageTk.PhotoImage(image)
    
        imglabel1 = Label(page1, image = photo).grid(row=2, column=1)
   
        imglabel1.image = photo
    
        imglabel1.pack()
    finally: 

        """ """
   
"""Waarden aanvullen bij wijziging van Class"""



"""functie save"""
def cal():
    """Class"""
    SC1 = Clbl.get()
    """Name"""
    SN1 = ABX.get()
    DORN = 0
    for oi in PlayerList:
        if str(oi) == SN1:
            messagebox.showinfo("Info", "We have found another soul with your name.")
            DORN = 1
            
    if DORN == 0:
    
        """Attack"""
        S1 = LB2.cget("text")
        """Defense"""
        S2 = LB3.cget("text")
        """Magic""" 
        S3 = LB4.cget("text")
        """Dexterity"""
        S4 = LB5.cget("text")
        """Drinking"""
        S5 = LB6.cget("text")
        """Jester"""
        S6 = LB7.cget("text") 

         

        PlayerDict.update({SN1:{"attack": S1, "Defense": S2, "Magic" : S3, "Dexterity": S4, "Drinking" : S5, "Jester" : S6, "Class": SC1, "Name": SN1}})
        print (PlayerDict)
    
        PlayerList.append(SN1)

        print (PlayerList)

        afa = open(SN1+"exp.txt","w+")
        width = 7
        fillchar = "0"
        exp = 1
        expfill = str(exp).rjust(width, fillchar)
        afa.write(expfill)


        fp=open("PLL.txt", "w+")
        o = 0
        for i in PlayerList:
        
            fp.write(str(PlayerList[o])+"\n")
            o = o+1
        
        f=open(SN1+".txt", "w+")
        f.write(str(SC1)+"\n")
        f.write(str(SN1)+"\n")
        f.write(str(S1)+"\n")
        f.write(str(S2)+"\n")
        f.write(str(S3)+"\n")
        f.write(str(S4)+"\n")
        f.write(str(S5)+"\n")
        f.write(str(S6)+"\n")
        f.close()

    

    """functie Add"""
def c():
    multi = [1,2,3]
    MP = 1
    if GXX6.get() == "Drink een pintje":
        MP = multi[0]
        print(MP)
    elif GXX7.get() == "Drink een pintje":
        MP = multi[1]
        print(MP)
    elif GXX8.get() == "Drink een pintje":
            MP = multi[2]
            print(MP)
                
    if GXX6.get() == "Drink een pintje" or GXX7.get() == "Drink een pintje"  or GXX8.get() == "Drink een pintje" :
        a = AD.cget("text")
        if a == "":
            messagebox.showinfo("Info", "You have no player selected")
        width = 7
        fillchar = "0"
        
        PVal = ABXD1.get()
        if PVal == "":
            PVal = ABXD2.get()
            if PVal == "":
                PVal = ABXD3.get()
        SN11 = ABX.get()
        f=open(SN11+"exp.txt", "r")
        if f.mode == 'r':
            contents =f.read()
        f.close()

        ResP = 50 * MP * int(PVal)
        PG = int(contents) + ResP
        PGfill = str(PG).rjust(width, fillchar)

        print(PGfill)

        f= open(SN11+"exp.txt","w")
        f.write(PGfill)
        f.close()

    if GXX6.get() == "Win een zuipspel" or GXX7.get() == "Win een zuipspel"  or GXX8.get() == "Win een zuipspel" :
        a = AD.cget("text")
        if a == "":
            messagebox.showinfo("Info", "You have no player selected")
        width = 7
        fillchar = "0"
        
        PVal = ABXD1.get()
        if PVal == "":
            PVal = ABXD2.get()
            if PVal == "":
                PVal = ABXD3.get()
        SN11 = ABX.get()
        f=open(SN11+"exp.txt", "r")
        if f.mode == 'r':
            contents =f.read()
        f.close()
        if GXX6.get() != '':
            MP = multi[0]
            if GXX7.get() != '':
                MP = multi[1]
                if GXX8.get() != '':
                    MP = multi[2]
        ResP = 500 * MP * int(PVal)
        PG = int(contents) + ResP
        PGfill = str(PG).rjust(width, fillchar)

        print(PGfill)

        f= open(SN11+"exp.txt","w")
        f.write(PGfill)
        f.close()
    if GXX6.get() == "Lach es met Danny" or GXX7.get() == "Lach es met Danny"  or GXX8.get() == "Lach es met Danny" :
        a = AD.cget("text")
        if a == "":
            messagebox.showinfo("Info", "You have no player selected")

        width = 7
        fillchar = "0"
        
        PVal = ABXD1.get()
        if PVal == "":
            PVal = ABXD2.get()
            if PVal == "":
                PVal = ABXD3.get()
        SN11 = ABX.get()
        f=open(SN11+"exp.txt", "r")
        if f.mode == 'r':
            contents =f.read()
        f.close()
        if GXX6.get() != '':
            MP = multi[0]
            if GXX7.get() != '':
                MP = multi[1]
                if GXX8.get() != '':
                    MP = multi[2]
        ResP = 2500 * MP * int(PVal)
        PG = int(contents) + ResP
        PGfill = str(PG).rjust(width, fillchar)

        print(PGfill)

        f= open(SN11+"exp.txt","w")
        f.write(PGfill)
        f.close()

"""Save Equipment"""
def SE():

    """Name"""
    SN1 = ABX.get()

    afaeq = open(SN1+"eq.txt","w+")
    
    WGXXP = GXX2.get()
    if GXX2.get() == "":
        afaeq.write(""+"\n")
    else:
        WGXXP = GXX2.get()
        afaeq.write(str(WGXXP)+"\n")
        
    WGXXS = GXX4.get()    
    if GXX4.get() == "":
        afaeq.write(""+"\n")
    else:
        WGXXS = GXX4.get()
        afaeq.write(str(WGXXS)+"\n")
        
    WGXXB = GXX3.get()

    if GXX3.get() =="":
        afaeq.write(""+"\n")
    else:
        WGXXB == GXX3.get()
        afaeq.write(str(WGXXB)+"\n")
        
    WGXXH = GXX.get()    

    if GXX.get() == "":
        afaeq.write(""+"\n")
    else:
        WGXXH == GXX.get()
        WINDXXH = HName.index(WGXXH)
        afaeq.write(str(WGXXH)+"\n")
        
    WGXXW = GXX5.get()    
    if GXX5.get() == "":
        afaeq.write(""+"\n")
    else:
        WGXXW == GXX5.get()
        afaeq.write(str(WGXXW)+"\n")
        
    WGXX = GXX1.get()    
    if GXX1.get() == "":
        afaeq.write(""+"\n")
    else:
        WGXX == GXX1.get()
        afaeq.write(str(WGXX)+"\n")

""" Get Equipment"""
def GE():

    """Name"""
    SN1 = ABX.get()

    mylines = []
    with open (SN1+'eq.txt', 'rt') as myfile:
        for myline in myfile:
            mylines.append(myline)

    a = AD.cget("text")
    if a == "":
        messagebox.showinfo("Info", "You have no player selected")
  
    GXX2.set("")
    GXX4.set("")
    GXX3.set("")
    GXX.set("")
    GXX5.set("")
    GXX1.set("")
    
    GX2 = mylines[0]
    GX4 = mylines[1]
    GX3 = mylines[2]
    GX = mylines[3]
    GX5 = mylines[4]
    GX1 = mylines[5]
    
    GXX2.insert(0, GX2.rstrip())
    GXX4.insert(0, GX4.rstrip())
    GXX3.insert(0, GX3.rstrip())
    GXX.insert(0, GX.rstrip())
    GXX5.insert(0, GX5.rstrip())
    GXX1.insert(0, GX1.rstrip ())

    
    ChooseBoots = chB
    ChooseHelmet = chH
    ChooseArmor = chA
    ChooseWeapon = chW
    ChooseShield = chS
    ChoosePants = chP

    try:
        ChooseBoots()
    finally:
        try:
            ChooseHelmet()
        finally:
            try:
                ChooseArmor()
            finally:
                try:
                    ChooseWeapon()
                finally:
                    try:
                        ChooseShield()
                    finally:
                        try:
                            ChoosePants()
                        finally:
                            """ """
    if A > 1000:
        LB1.configure(text = LoreBase[3])



    

"""Opmaak Tabs"""
     
# gives weight to the cells in the grid
rows = 0
while rows < 50:
    main.rowconfigure(rows, weight=1)
    main.columnconfigure(rows, weight=1)
    rows += 1
 
# Defines and places the notebook widget
nb = ttk.Notebook(main)
nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')
 
# Adds tab 1 of the notebook
page1 = ttk.Frame(nb)
nb.add(page1, text='View')

"""Opmaak 1ste tab"""

tkinter.Label(page1, text="Name",borderwidth=1 ).grid(row=1,column=1)
ABX = ttk.Combobox(page1, values= PlayerList, width = 80 )
"""tkinter.Entry(page1,borderwidth=1, width =80 )"""
ABX.grid(row=1,column=2)



tkinter.Label(page1, text="Class",borderwidth=1, font = 'Bold' ).grid(row=3,column=1)
Clbl = ttk.Combobox(page1, values =["Warrior", "Archer", "Mage", "Necromancer", "Bard", "Jester", "Wanderer"] )
Clbl.grid(row=4,column=1)

#Setting it up

img = ImageTk.PhotoImage(Image.open("duff.jpg"))
       
#Displaying it
imglabel1 = Label(page1, image=img).grid(row=2, column=1)


"""tkinter.Label(page1, text="",borderwidth=1 ).grid(row=5,column=1)"""
AD = tkinter.Label(page1, text="",borderwidth=1, fg="lightgrey")
AD.grid(row=8,column=1)
AD1 = tkinter.Label(page1, text="",borderwidth=1, fg="lightgrey" )
AD1.grid(row=8,column=1)
AD2 = tkinter.Label(page1, text="",borderwidth=1, fg="lightgrey" )
AD2.grid(row=8,column=1)
AD3 = tkinter.Label(page1, text="ATK/DEF",borderwidth=1  )
AD3.grid(row=8,column=1)

tkinter.Label(page1, text="",borderwidth=1 ).grid(row=7,column=1)
tkinter.Label(page1, text="",borderwidth=1 ).grid(row=6,column=1)

LB1 = tkinter.Label(page1, text="Oehw Yeah!!", bd = 1, font=("Sylfaen", 26))
LB1.grid(row=2,column=2)
tkinter.Label(page1, text="Attack", font = 'Bold').grid(row=3,column=2)



LB2 = tkinter.Label(page1, text="ValAt",borderwidth=1 )
LB2.grid(row=4,column=2)


tkinter.Label(page1, text="Defense", font = 'Bold').grid(row=5,column=2)
LB3 = tkinter.Label(page1, text="DefAt",borderwidth=1 )
LB3.grid(row=6,column=2)

tkinter.Label(page1, text="Magic", font = 'Bold').grid(row=7,column=2)
LB4 = tkinter.Label(page1, text="MagicAt")
LB4.grid(row=8,column=2)

tkinter.Label(page1, text="Dexterity", font = 'Bold').grid(row=3,column=3)
LB5 = tkinter.Label(page1, text="DexterityAt")
LB5.grid(row=4,column=3)

tkinter.Label(page1, text="Drinking", font = 'Bold').grid(row=5,column=3)
LB6 = tkinter.Label(page1, text="DrinkingAt")
LB6.grid(row=6,column=3)

tkinter.Label(page1, text="Jester", font = 'Bold').grid(row=7,column=3)
LB7 = tkinter.Label(page1, text="JesterAt")
LB7.grid(row=8,column=3)

tkinter.Label(page1, text="",borderwidth=1 ).grid(row=11,column=1)
tkinter.Label(page1, text="",borderwidth=1 ).grid(row=11,column=2)
tkinter.Label(page1, text="",borderwidth=1 ).grid(row=10,column=1)
tkinter.Label(page1, text="",borderwidth=1 ).grid(row=10,column=2)

                         
BT = tkinter.Button(page1, text="Clear", command=callback).grid(row=12,column=2)
BT2 = tkinter.Button(page1, text="Get", command=call).grid(row=12,column=1)
BT3 = tkinter.Button(page1, text="Save", command=cal).grid(row=12,column=3)
BT4 = tkinter.Button(page1, text="Show", command=ca).grid(row=5,column=1)

tkinter.Label(page1, text="").grid(row=13,column=1)
Info1 = tkinter.Button(page1, text="Info", command=Info1).grid(row=14,column=1)



# Adds tab 2 of the notebook
page2 = ttk.Frame(nb)
nb.add(page2, text='Scoreboard')

tkinter.Label(page2, text="Paintball",borderwidth=1 ).grid(row=1,column=1)

PPBList = []
PPBComList = []
for n in range(20):
    # create left side info labels
    Label(page2, text="%2d: " % n).grid(row=n+2, column=0)
    PPBComList.append(ttk.Combobox(page2, values= PlayerList ))
    PPBComList[n].grid(row=n+2,column=3)
    # create entries list
    PPBList.append(Entry(page2, bg='red', width=10))
    # grid layout the entries
    PPBList[n].grid(row=n+2, column=4)


BTPB = tkinter.Button(page2, text="Enter the heroes", command=PB).grid(row=22,column=3)

tkinter.Label(page2, text="Alpenchallenge",borderwidth=1 ).grid(row=1,column=6)

ACList = []
ACComList = []
for n in range(20):
    # create left side info labels
    Label(page2, text="%2d: " % n).grid(row=n+2, column=5)
    ACComList.append(ttk.Combobox(page2, values= PlayerList ))
    ACComList[n].grid(row=n+2,column=8)
    # create entries list
    ACList.append(Entry(page2, bg='yellow', width=10))
    # grid layout the entries
    ACList[n].grid(row=n+2, column=9)

                     

BTAC = tkinter.Button(page2, text="Enter the heroes", command=AC).grid(row=22,column=8)

tkinter.Label(page2, text="Varia",borderwidth=1 ).grid(row=1,column=11)

VList = []
VComList = []
for n in range(20):
    # create left side info labels
    Label(page2, text="%2d: " % n).grid(row=n+2, column=10)
    VComList.append(ttk.Combobox(page2, values= PlayerList ))
    VComList[n].grid(row=n+2,column=13)
    # create entries list
    VList.append(Entry(page2, bg='blue', width=10))
    # grid layout the entries
    VList[n].grid(row=n+2, column=14)

BTAC = tkinter.Button(page2, text="Enter the heroes", command=V).grid(row=22,column=13)

tkinter.Label(page2, text="").grid(row=23,column=3)
Info2 = tkinter.Button(page2, text="Info", command=Info2).grid(row=24,column=3)

# Adds tab 3 of the notebook
page3 = ttk.Frame(nb)
nb.add(page3, text='Equipment')

tkinter.Label(page3, text="Helmet",borderwidth=1 ).grid(row=1,column=1)
GXX = ttk.Combobox(page3, values= HName )
GXX.grid(row=2,column=1)
CH1 = tkinter.Button(page3, text="Show Helmet", command=chH).grid(row=3,column=1)

tkinter.Label(page3, text="Armor",borderwidth=1 ).grid(row=1,column=2)
GXX1 = ttk.Combobox(page3, values= AName )
GXX1.grid(row=2,column=2)
CH3 = tkinter.Button(page3, text="Show Armor", command=chA).grid(row=3,column=2)

tkinter.Label(page3, text="Pants",borderwidth=1 ).grid(row=1,column=3)
GXX2 = ttk.Combobox(page3, values= PName )
GXX2.grid(row=2,column=3)
CH4 = tkinter.Button(page3, text="Show Pants", command=chP).grid(row=3,column=3)

tkinter.Label(page3, text="Boots",borderwidth=1 ).grid(row=1,column=4)
GXX3 = ttk.Combobox(page3, values= BName )
GXX3.grid(row=2,column=4)
CH5 = tkinter.Button(page3, text="Show Boots", command=chB).grid(row=3,column=4)

tkinter.Label(page3, text="Shield",borderwidth=1 ).grid(row=1,column=5)
GXX4 = ttk.Combobox(page3, values= SName ) 
GXX4.grid(row=2,column=5)
CH6 = tkinter.Button(page3, text="Show Shield", command=chS).grid(row=3,column=5)

tkinter.Label(page3, text="Weapon",borderwidth=1 ).grid(row=1,column=6)
GXX5 = ttk.Combobox(page3, values= WName )
GXX5.grid(row=2,column=6)
CH2 = tkinter.Button(page3, text="Show Weapon", command=chW).grid(row=3,column=6)

Atr1 = tkinter.Label(page3, text="...",borderwidth=1 )
Atr1.grid(row=5,column=6)
Atr2 = tkinter.Label(page3, text="...",borderwidth=1 )
Atr2.grid(row=6,column=6)
Atr3 = tkinter.Label(page3, text="...",borderwidth=1 )
Atr3.grid(row=7,column=6)
Atr4 = tkinter.Label(page3, text="...",borderwidth=1 )
Atr4.grid(row=5,column=1)
Atr5 = tkinter.Label(page3, text="...",borderwidth=1 )
Atr5.grid(row=6,column=1)
Atr6 = tkinter.Label(page3, text="...",borderwidth=1 )
Atr6.grid(row=7,column=1)
Atr7 = tkinter.Label(page3, text="...",borderwidth=1 )
Atr7.grid(row=5,column=2)
Atr8 = tkinter.Label(page3, text="...",borderwidth=1 )
Atr8.grid(row=6,column=2)
Atr9 = tkinter.Label(page3, text="...",borderwidth=1 )
Atr9.grid(row=7,column=2)
Atr10 = tkinter.Label(page3, text="...",borderwidth=1 )
Atr10.grid(row=5,column=5)
Atr11 = tkinter.Label(page3, text="...",borderwidth=1 )
Atr11.grid(row=6,column=5)
Atr12 = tkinter.Label(page3, text="...",borderwidth=1 )
Atr12.grid(row=7,column=5)
Atr13 = tkinter.Label(page3, text="...",borderwidth=1 )
Atr13.grid(row=5,column=3)
Atr14 = tkinter.Label(page3, text="...",borderwidth=1 )
Atr14.grid(row=6,column=3)
Atr15 = tkinter.Label(page3, text="...",borderwidth=1 )
Atr15.grid(row=7,column=3)
Atr16 = tkinter.Label(page3, text="...",borderwidth=1 )
Atr16.grid(row=5,column=4)
Atr17 = tkinter.Label(page3, text="...",borderwidth=1 )
Atr17.grid(row=6,column=4)
Atr18 = tkinter.Label(page3, text="...",borderwidth=1 )
Atr18.grid(row=7,column=4)



Atr22 = tkinter.Label(page3, text= "Attack" ,borderwidth=1 )
Atr22.grid(row=11,column=3)
Atr23 = tkinter.Label(page3, text="Defense",borderwidth=1 )
Atr23.grid(row=11,column=4)
Atr24 = tkinter.Label(page3, text= "...",borderwidth=1 )
Atr24.grid(row=12,column=3)
Atr25 = tkinter.Label(page3, text= "...",borderwidth=1 )
Atr25.grid(row=12,column=4)

Atr19 = tkinter.Label(page3, text= "Base Attack" ,borderwidth=1 )
Atr19.grid(row=9,column=3)
Atr20 = tkinter.Label(page3, text="Base Defense",borderwidth=1 )
Atr20.grid(row=9,column=4)
Atr21 = tkinter.Label(page3, text= "...",borderwidth=1 )
Atr21.grid(row=10,column=3)
Atr22 = tkinter.Label(page3, text= "...",borderwidth=1 )
Atr22.grid(row=10,column=4)


Atr26 = tkinter.Label(page3, text="",borderwidth=1 )
Atr26.grid(row=8,column=1)
Atr27 = tkinter.Label(page3, text="",borderwidth=1 )
Atr27.grid(row=9,column=1)
Atr28 = tkinter.Label(page3, text="",borderwidth=1 )
Atr28.grid(row=10,column=1)
Atr29 = tkinter.Label(page3, text="",borderwidth=1 )
Atr29.grid(row=11,column=1)
Atr30 = tkinter.Label(page3, text="",borderwidth=1 )
Atr30.grid(row=12,column=1)
Atr31 = tkinter.Label(page3, text="",borderwidth=1 )
Atr31.grid(row=13,column=1)
Atr32 = tkinter.Label(page3, text="",borderwidth=1 )
Atr32.grid(row=14,column=1)

EQ1 = tkinter.Button(page3, text="Get Equipment", command=GE).grid(row=15,column=1)
EQ2 = tkinter.Button(page3, text="Save Equipment", command=SE).grid(row=16,column=1)

tkinter.Label(page3, text="").grid(row=17,column=1)
Info3 = tkinter.Button(page3, text="Info", command=Info3).grid(row=18,column=1)


# Adds tab 4 of the notebook
page4 = ttk.Frame(nb)
nb.add(page4, text='Adventure')

tkinter.Label(page4, text="Quests",borderwidth=4, font=("Helvetica", 20) ).grid(row=1,column=1)

tkinter.Label(page4, text="Day 1",borderwidth=1 ).grid(row=2,column=1)
GXX6 = ttk.Combobox(page4, values =["Drink een pintje", "Lach es met Danny", "Win een zuipspel"], width =40 )
GXX6.grid(row=2,column=2)

ABXD1 = tkinter.Entry(page4,borderwidth=1, width =10 )
ABXD1.grid(row=2,column=3)
BT5 = tkinter.Button(page4, text="Add", command=c).grid(row=2,column=5)

tkinter.Label(page4, text="",borderwidth=1 ).grid(row=3,column=2)


tkinter.Label(page4, text="Day 2",borderwidth=1 ).grid(row=4,column=1)
GXX7 = ttk.Combobox(page4, values =["Drink een pintje","Lach es met Danny", "Win een zuipspel"], width =40 )
GXX7.grid(row=4,column=2)

ABXD2 = tkinter.Entry(page4,borderwidth=1, width =10 )
ABXD2.grid(row=4,column=3)
BT6 = tkinter.Button(page4, text="Add", command=c).grid(row=4,column=5)

tkinter.Label(page4, text="",borderwidth=1 ).grid(row=5,column=2)

tkinter.Label(page4, text="Day 3",borderwidth=1 ).grid(row=6,column=1)
GXX8 = ttk.Combobox(page4, values =["Drink een pintje","Lach es met Danny", "Win een zuipspel"], width =40 )
GXX8.grid(row=6,column=2)

ABXD3 = tkinter.Entry(page4,borderwidth=1, width =10 )
ABXD3.grid(row=6,column=3)
BT7 = tkinter.Button(page4, text="Add", command=c).grid(row=6,column=5)

tkinter.Label(page4, text="",borderwidth=1 ).grid(row=7,column=2)

tkinter.Label(page4, text="Battles",borderwidth=4, font=("Helvetica", 20) ).grid(row=8,column=1)
tkinter.Label(page4, text="",borderwidth=1 ).grid(row=9,column=1)
BT5 = tkinter.Button(page4, text="Battle", command=Battle).grid(row=10,column=1)
tkinter.Label(page4, text="",borderwidth=1 ).grid(row=10,column=2)
tkinter.Label(page4, text="",borderwidth=1 ).grid(row=11,column=1)

tkinter.Label(page4, text="Top 3 souls",borderwidth=4, font=("Helvetica", 20) ).grid(row=12,column=1)
G1 = tkinter.Label(page4, text="",borderwidth=1 )
G1.grid(row=13,column=2)
G2 = tkinter.Label(page4, text="",borderwidth=1 )
G2.grid(row=14,column=2)
G3 = tkinter.Label(page4, text="",borderwidth=1 )
G3.grid(row=15,column=2)

BT7 = tkinter.Button(page4, text="Il morituri te salutant", command=calc).grid(row=13,column=7)
gold = ImageTk.PhotoImage(Image.open("gold.png"))
imglabel = Label(page4, image=gold).grid(row=13, column=1)
silver = ImageTk.PhotoImage(Image.open("silver.png"))
imglabel = Label(page4, image=silver).grid(row=14, column=1)
bronze = ImageTk.PhotoImage(Image.open("bronze.png"))
imglabel = Label(page4, image=bronze).grid(row=15, column=1)

BT50 = tkinter.Button(page4, text="All the souls", command=ListAll).grid(row=16,column=1)
tkinter.Label(page4, text="").grid(row=17,column=1)
Info4 = tkinter.Button(page4, text="Info", command=Info4).grid(row=18,column=1)

# Adds tab 5 of the notebook
page5 = ttk.Frame(nb)
nb.add(page5, text='Drinkboard')

tkinter.Label(page5, text="Zuipspel I",borderwidth=1 ).grid(row=1,column=1)

PPBList = []
PPBComList = []
for n in range(20):
    # create left side info labels
    Label(page5, text="%2d: " % n).grid(row=n+2, column=0)
    PPBComList.append(ttk.Combobox(page5, values= PlayerList))
    PPBComList[n].grid(row=n+2,column=3)
    # create entries list
    PPBList.append(Entry(page5, bg='yellow', width=10))
    # grid layout the entries
    PPBList[n].grid(row=n+2, column=4)
    NrZS = 1 


BTPB = tkinter.Button(page5, text="Enter the heroes", command=lambda: ZS(NrZS)).grid(row=22,column=3)

tkinter.Label(page5, text="Zuipspel II",borderwidth=1 ).grid(row=1,column=6)

ACList = []
ACComList = []
for n in range(20):
    # create left side info labels
    Label(page5, text="%2d: " % n).grid(row=n+2, column=5)
    ACComList.append(ttk.Combobox(page5, values= PlayerList ))
    ACComList[n].grid(row=n+2,column=8)
    # create entries list
    ACList.append(Entry(page5, bg='yellow', width=10))
    # grid layout the entries
    ACList[n].grid(row=n+2, column=9)
    NrZSS = 2
                     

BTAC = tkinter.Button(page5, text="Enter the heroes", command=lambda: ZS(NrZSS)).grid(row=22,column=8)

tkinter.Label(page5, text="Zuipspel III",borderwidth=1 ).grid(row=1,column=11)

VList = []
VComList = []
for n in range(20):
    # create left side info labels
    Label(page5, text="%2d: " % n).grid(row=n+2, column=10)
    VComList.append(ttk.Combobox(page5, values= PlayerList ))
    VComList[n].grid(row=n+2,column=13)
    # create entries list
    VList.append(Entry(page5, bg='yellow', width=10))
    # grid layout the entries
    VList[n].grid(row=n+2, column=14)
    NrZSSS = 3

BTAC = tkinter.Button(page5, text="Enter the heroes", command=lambda: ZS(NrZSSS)).grid(row=22,column=13)
tkinter.Label(page5, text="").grid(row=23,column=3)
Info5 = tkinter.Button(page5, text="Info", command=Info5).grid(row=23,column=3)

 
main.mainloop()
