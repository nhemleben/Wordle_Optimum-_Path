import unittest
import sys
sys.path.append('../src')
import src.Wordle_Engine as Wordle_Engine

class Test_Engine_Methods(unittest.TestCase):


    def test_matching_character_indexes_all(self):
        all_indexes = Wordle_Engine.matching_character_indexes('aaaaa','aaaaa')
        self.assertTrue(5 == len(all_indexes))

    def test_matching_character_indexes_no(self):
        no_indexes = Wordle_Engine.matching_character_indexes('aaaaa','bbbbb')
        self.assertTrue(0 == len(no_indexes))

    def test_matching_character_indexes_some_1(self):
        some_indexes = Wordle_Engine.matching_character_indexes('aaaaa','abbbb')
        self.assertTrue(0 == some_indexes[0])
        self.assertTrue(1 == len(some_indexes))

    def test_matching_character_indexes_some_2(self):
        some_indexes = Wordle_Engine.matching_character_indexes('aaaaa','bbbab')
        self.assertTrue(3 == some_indexes[0])
        self.assertTrue(1 == len(some_indexes))

    def test_matching_character_indexes_some_3(self):
        some_indexes = Wordle_Engine.matching_character_indexes('aaaaa','abbab')
        self.assertTrue(0 == some_indexes[0])
        self.assertTrue(3 == some_indexes[1])
        self.assertTrue(2 == len(some_indexes))



    def test_non_matching_contained_in_answer_indexes_no(self):
        no_indexes = Wordle_Engine.non_matching_contained_in_answer_indexes('aaaaa','aaaaa')
        self.assertTrue(0 == len(no_indexes))

    def test_non_matching_contained_in_answer_indexes_some_1(self):
        some_indexes = Wordle_Engine.non_matching_contained_in_answer_indexes('aaaab','baaaa')
        self.assertTrue(0 == some_indexes[0])
        self.assertTrue(1 == len(some_indexes))

    def test_non_matching_contained_in_answer_indexes_some_2(self):
        some_indexes = Wordle_Engine.non_matching_contained_in_answer_indexes('aaaab','babaa')
        self.assertTrue(0 == some_indexes[0])
        self.assertTrue(2 == some_indexes[1])
        self.assertTrue(2 == len(some_indexes))

    def test_non_matching_contained_in_answer_indexes_all(self):
        some_indexes = Wordle_Engine.non_matching_contained_in_answer_indexes('abcde','edabc')
        self.assertTrue(0 == some_indexes[0])
        self.assertTrue(1 == some_indexes[1])
        self.assertTrue(5 == len(some_indexes))


    def test_non_matched_non_duped_1(self):
        some_indexes = Wordle_Engine.non_matched_non_duped('abcde','eeabc')
        self.assertTrue(0 == len(some_indexes))

    def test_non_matched_non_duped_2(self):
        some_indexes = Wordle_Engine.non_matched_non_duped('abcdz','eeabc')
        self.assertTrue(2 == len(some_indexes))

if __name__ == '__main__':
    unittest.main()