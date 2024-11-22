#КасимовТР, ГруздевИВ, Программная инженерия, Лабораторная работа №6

#Разработать тесты для командного проекта, разместить (если это не было сделано ранее) в репозитории на GitHub.
#Настроить Actions для автоматического тестирования проекта.
#Убедиться, что тесты проходят, линтер не находит ошибок в стиле.

import unittest
import aina

class TestMain(unittest.TestCase):

    def test_accuracy_not_none(self):
        acc = aina.Em_T_accuracy('random sentence')
        self.assertIsNotNone(acc)

    def test_accuracy_percent(self):
        acc = aina.Em_T_accuracy('random sentence')
        self.assertTrue(acc >= 0 and acc <= 100)

    def test_input_not_none(self):
        lbl = aina.Em_T_label('random sentence')
        self.assertIsNotNone(lbl)

    def test_good_bad_ugly(self):
        lbl = aina.Em_T_label('random sentence')
        self.assertTrue(lbl == 'neutral' or lbl == 'positive' or lbl == 'negative')

if __name__ == '__main__':
    unittest.main()