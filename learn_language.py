# -*- coding: utf-8 -*-
from random import randint
from readfile import readFile
from checker import Checker
from languages import Languages

from readfile import readFile


class Learning():
    def __init__(self,file_name):
        self.file_name=file_name
        self.word_list = self.create_word_list()

    def setFileName(self,name):
        self.file_name=name

    def create_word_list(self):
        outer_list = []
        lines = readFile(self.file_name)
        self.lines_in_file = len(lines)
        for x in range(0, self.lines_in_file):
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
        index = randint(0, self.lines_in_file-1)
        return [index,self.wordlist[index][language]]



    def check_answer(self, language, words=None, answer=None, points=None, index=None):
        """

        :param language:
        :param words: right answer
        :param answer: user answer
        :param points: the current user points
        :param index: index where the word found
        :return:
        """
        if words == None:
            words=self.word_list
        ret=[]
        if language== "r" or language==Languages.SWEDISH:

            p=Checker((words[index][Languages.SWEDISH]).split(",")).check(answer)
            if p > 0 and p < 4:
                ret.append("Osa oikein!")
                ret.append("Oikea vastaus on " + str(words[index][Languages.SWEDISH]))
            elif p == 4:
                ret.append("Kaikki oikein!!!")
            elif p == 0:
                ret.append("Ei yhtään oikein")
                ret.append("Oikea vastaus on " + str(words[index][Languages.SWEDISH]))
            points+=p;
            ret.insert(0,points)
        elif language== "s" or language==Languages.FINNISH:
            p = Checker((words[index][Languages.FINNISH]).split(",")).check(answer)
            if p > 0 and p < 4:
                ret.append("Osa oikein!")
                ret.append("Oikea vastaus on " + str(words[index][Languages.FINNISH]))
            elif p == 4:
                ret.append("Kaikki oikein!!!")
            elif p == 0:
                ret.append("Ei yhtään oikein")
                ret.append("Oikea vastaus on " + str(words[index][Languages.FINNISH]))
            points += p;
            ret.insert(0,points)
        return ret


def main():

    learn=Learning("sanasto.txt")

    words=learn.create_word_list()
    points=0
    count=0
    index_sverige=0
    index_finnish=1
    language=input("vastaa kielellä, ruotsi=r ja suomi=s ")
    checked_values = [0]
    while 1==1:
        count+=4
        index=randint(0,100)
        index_and_word=[]

        if language=="r":
            index_and_word=learn.get_random_word(Languages.FINNISH)
            print("suomi " + index_and_word[1])
        else:
            index_and_word=learn.get_random_word(Languages.SWEDISH)
            print("ruotsi " + index_and_word[1])
            #print("ruotsi "+learn.get_random_word(Languages.SWEDISH))
        answer=input("Anna sana toisella kielellä\n")
        checked_values=learn.check_answer(language, words,answer, checked_values[0],index_and_word[0])
        length=len(checked_values)

        if length==3:
            print(checked_values[1])
            print(checked_values[2])
        else:
            print(checked_values[1])
        print("Sinulla on nyt", checked_values[0], " pistettä.")
        #check_answer(language, answer, points)

        resume=input("Jatketaanko k/e ")
        if resume== "e":
            print("Kiitos ruotsin opiskelusta, tervetuloa uudelleen!")
            percent = checked_values[0] / count * 100
            print("sait " + str(checked_values[0]) + "/" + str(count) + " pistetta, eli %22.2f prosenttia oikein" % percent)
            break;

if __name__=='__main__':
    main()

