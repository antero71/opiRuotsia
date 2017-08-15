# -*- coding: utf-8 -*-
from random import randint
from readfile import readFile
from checker import Checker
from languages import Languages

from readfile import readFile


class Learning():
    def __init__(self):
        self.word_list = self.create_word_list()

    def create_word_list(self):
        outer_list = []
        lines = readFile("sanasto.txt")
        for x in range(0, len(lines)):
            outer_list.append(lines[x].strip().split(";"))
        return outer_list

    @property
    def wordlist(self):
        return self.word_list

    def get_random_word(self,language):
        """

        :param self:
        :param language:
        :return: randomly selected index and correct word in the selected language
        """
        index = randint(0, 100)
        return [index,self.wordlist[index][language]]



def check_answer(language, words,answer, points,index):
    if language== "r":
        p=Checker((words[index][Languages.FINNISH]).split(",")).check(answer)
        if p > 0 and p < 4:
            print("Osa oikein!")
            print("Oikea vastaus on " + str(words[index][Languages.SWEDISH]))
        elif p == 4:
            print("Kaikki oikein!!!")
        elif p == 0:
            print("Ei yhtään oikein")
            print("Oikea vastaus on " + str(words[index][Languages.SWEDISH]))
        points+=p;
    elif language== "s":
        p = Checker((words[index][Languages.FINNISH]).split(",")).check(answer)
        if p > 0 and p < 4:
            print("Osa oikein!")
            print("Oikea vastaus on " + str(words[index][Languages.FINNISH]))
        elif p == 4:
            print("Kaikki oikein!!!")
        elif p == 0:
            print("Ei yhtään oikein")
            print("Oikea vastaus on " + str(words[index][Languages.FINNISH]))
        points += p;
    return points


def main():

    learn=Learning()

    words=learn.create_word_list()
    points=0
    count=0
    index_sverige=0
    index_finnish=1
    language=input("vastaa kielellä, ruotsi=r ja suomi=s ")
    while 1==1:
        count+=4
        index=randint(0,100)
        index_and_word=[]
        if language== "r":
            index_and_word=learn.get_random_word(Languages.FINNISH)
            print("suomi " + index_and_word[1])
        else:
            index_and_word=learn.get_random_word(Languages.SWEDISH)
            print("ruotsi " + index_and_word[1])
            #print("ruotsi "+learn.get_random_word(Languages.SWEDISH))
        answer=input("Anna sana toisella kielellä\n")
        points=check_answer(language, words,answer, points,index_and_word[0])
        #check_answer(language, answer, points)

        resume=input("Jatketaanko k/e ")
        if resume== "e":
            print("Kiitos ruotsin opiskelusta, tervetuloa uudelleen!")
            percent = points / count * 100
            print("sait " + str(points) + "/" + str(count) + " pistetta, eli %22.2f prosenttia oikein" % percent)
            break;

if __name__=='__main__':
    main()

