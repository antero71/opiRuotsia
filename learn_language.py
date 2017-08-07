from random import randint
from luetiedosto import readFile
def tarkistaVastaus(kieli,vastaus,pisteet):
    if kieli=="r" and vastaus==outer_list[index][index_ruotsi]:
        print("oikein!")
        pisteet+=1
    elif kieli=="s" and vastaus==outer_list[index][index_suomi]:
        print("Oikein!")
        pisteet+=1
    elif kieli=="r":
        print("Väärin")
        print("Oikea vastaus on "+str(outer_list[index][index_ruotsi]))
    else:
        print("Väärin")
        print("Oikea vastaus on "+str(outer_list[index][index_suomi]))
    return pisteet


outer_list=[]
lines = readFile("sanasto.txt")
for x in range(0,len(lines)):
    outer_list.append(lines[x].strip().split(";"))

pisteet=0
lukumaara=0
index_ruotsi=0
index_suomi=1
kieli=input("vastaa kielellä, ruotsi=r ja suomi=s ")
while 1==1:
   lukumaara+=1
   index=randint(0,100)
   if kieli=="r":
       print("suomi "+str(outer_list[index][index_suomi]))
   else:
       print("ruotsi "+str(outer_list[index][index_ruotsi]))
   vastaus=input("Anna sana toisella kielellä ")
   pisteet=tarkistaVastaus(kieli,vastaus,pisteet)
   jatka=input("Jatketaanko k/e ")
   if jatka=="e":
      print("Kiitos ruotsin opiskelusta, tervetuloa uudelleen!")
      prosentit = pisteet/lukumaara*100
      print("sait "+str(pisteet)+"/"+str(lukumaara)+" pistetta, eli %22.2f prosenttia oikein" % prosentit)
      break;

