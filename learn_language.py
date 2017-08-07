# -*- coding: utf-8 -*-
from random import randint
from readfile import readFile


from readfile import readFile
def check_answer(language, answer, points):
    if language== "r" and check(answer,outer_list[index][index_sverige]):
        print("oikein!")
        points+=1
    elif language== "s" and answer==outer_list[index][index_finnish]:
        print("Oikein!")
        points+=1
    elif language== "r":
        print("Väärin")
        print("Oikea vastaus on " + str(outer_list[index][index_sverige]))
    else:
        print("Väärin")
        print("Oikea vastaus on " + str(outer_list[index][index_finnish]))
    return points

def check(answer,right_answer):
    return len(answer)>0 and right_answer.__contains__(answer)




outer_list=[]
lines = readFile("sanasto.txt")
for x in range(0,len(lines)):
    outer_list.append(lines[x].strip().split(";"))

points=0
count=0
index_sverige=0
index_finnish=1
language=input("vastaa kielellä, ruotsi=r ja suomi=s ")
while 1==1:
   count+=1
   index=randint(0,100)
   if language== "r":
       print("suomi " + str(outer_list[index][index_finnish]))
   else:
       print("ruotsi " + str(outer_list[index][index_sverige]))
   answer=input("Anna sana toisella kielellä ")
   points=check_answer(language, answer, points)
   resume=input("Jatketaanko k/e ")
   if resume== "e":
      print("Kiitos ruotsin opiskelusta, tervetuloa uudelleen!")
      prosentit = points / count * 100
      print("sait " + str(points) + "/" + str(count) + " pistetta, eli %22.2f prosenttia oikein" % prosentit)
      break;

