import unittest
import sys
sys.path.append('../src')
import src.Wordle_Player as World_Player

class Test_Player_Methods(unittest.TestCase):

    def test_all_valid_guesses_aahe(self):
        Cur_Valid_Guesses = World_Player.All_Possible_Guesses
        matching_characters = ['a','a','h','e']
        matching_indexes = [0,1,2,3]
        non_matching_contained = []

        valid_guesses = World_Player.all_valid_guesses(Cur_Valid_Guesses, matching_characters, matching_indexes, non_matching_contained)

        self.assertTrue(1 == len(valid_guesses))
        self.assertTrue(valid_guesses[0] == 'aahed')

    def test_all_valid_guesses_aa(self):
        Cur_Valid_Guesses = World_Player.All_Possible_Guesses
        matching_characters = ['a','a']
        matching_indexes = [0,1]
        non_matching_contained = []

        valid_guesses = World_Player.all_valid_guesses(Cur_Valid_Guesses, matching_characters, matching_indexes, non_matching_contained)

        self.assertTrue(4 == len(valid_guesses))
        self.assertTrue(valid_guesses[0] == 'aahed')

    def test_all_valid_guesses_a(self):
        Cur_Valid_Guesses = World_Player.All_Possible_Guesses
        matching_characters = ['a']
        matching_indexes = [0]
        non_matching_contained = []

        valid_guesses = World_Player.all_valid_guesses(Cur_Valid_Guesses, matching_characters, matching_indexes, non_matching_contained)

        self.assertTrue(596+141 == len(valid_guesses))
        self.assertTrue(valid_guesses[0] == 'aahed')

    def test_all_valid_answers_a(self):
        Cur_Valid_Guesses = World_Player.All_Possible_Answers
        matching_characters = ['a']
        matching_indexes = [0]
        non_matching_contained = []

        valid_guesses = World_Player.all_valid_guesses(Cur_Valid_Guesses, matching_characters, matching_indexes, non_matching_contained)

        self.assertTrue(141 == len(valid_guesses))
        self.assertTrue(valid_guesses[0] == 'aback')

if __name__ == '__main__':
    unittest.main()