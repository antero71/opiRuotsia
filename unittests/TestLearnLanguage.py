import unittest

from languages import Languages
from learn_language import Learning


class TestLearnLanguage(unittest.TestCase):


    def setUp(self):
        self.learn=Learning("../sanasto.txt")
        self.all_words = self.learn.create_word_list()

    def test_find_word(self):
        self.assertEqual(self.learn.lines_in_file,102)

        word=self.learn.get_random_word(Languages.FINNISH)

        index=86
        points=0

        checked_answer=self.learn.check_answer("r", self.all_words, "svära,svär,svor,svurit", points, index)
        self.assertEqual(checked_answer[0],4)
        self.assertEqual(checked_answer[1], "Kaikki oikein!!!")

    def test_partly_incorrect_answer(self):
        points=0
        index=3
        checked_answer = self.learn.check_answer("r", self.all_words, "bjuda,bjuder", points, index)
        self.assertEqual(checked_answer[0], 2)
        self.assertEqual(checked_answer[1], "Osa oikein!")
        self.assertEqual(checked_answer[2],"Oikea vastaus on bjuda,bjuder,bjöd,bjudit")

