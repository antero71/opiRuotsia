# -*- coding: utf-8 -*-
from random import randint
from readfile import readFile
from checker import Checker


from readfile import readFile

def create_word_list():
    outer_list = []
    lines = readFile("sanasto.txt")
    for x in range(0, len(lines)):
        outer_list.append(lines[x].strip().split(";"))
    return outer_list

def check_answer(language, words,answer, points,index,index_sverige,index_finnish):
    if language== "r":
        p=Checker((words[index][index_sverige]).split(",")).check(answer)
        if p > 0 and p < 4:
            print("Osa oikein!")
            print("Oikea vastaus on " + str(words[index][index_sverige]))
        elif p == 4:
            print("Kaikki oikein!!!")
        elif p == 0:
            print("Ei yhtään oikein")
            print("Oikea vastaus on " + str(words[index][index_sverige]))
        points+=p;
    elif language== "s":
        p = Checker((words[index][index_finnish]).split(",")).check(answer)
        if p > 0 and p < 4:
            print("Osa oikein!")
            print("Oikea vastaus on " + str(words[index][index_finnish]))
        elif p == 4:
            print("Kaikki oikein!!!")
        elif p == 0:
            print("Ei yhtään oikein")
            print("Oikea vastaus on " + str(words[index][index_finnish]))
        points += p;
    return points


def main():

    words=create_word_list()
    points=0
    count=0
    index_sverige=0
    index_finnish=1
    language=input("vastaa kielellä, ruotsi=r ja suomi=s ")
    while 1==1:
        count+=4
        index=randint(0,100)
        if language== "r":
            print("suomi " + str(words[index][index_finnish]))
        else:
            print("ruotsi " + str(words[index][index_sverige]))
        answer=input("Anna sana toisella kielellä\n")
        points=check_answer(language, words,answer, points,index,index_sverige,index_finnish)
        #check_answer(language, answer, points)

        resume=input("Jatketaanko k/e ")
        if resume== "e":
            print("Kiitos ruotsin opiskelusta, tervetuloa uudelleen!")
            percent = points / count * 100
            print("sait " + str(points) + "/" + str(count) + " pistetta, eli %22.2f prosenttia oikein" % percent)
            break;

if __name__=='__main__':
    main()

