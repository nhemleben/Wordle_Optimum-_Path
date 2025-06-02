import unittest
import sys
sys.path.append('../src')
import src.Wordle_Engine as World_Engine
import src.Wordle_Player as World_Player

class Test_Engine_Methods(unittest.TestCase):



    def test_all_valid_guesses(self):
        Cur_Valid_Guesses = World_Player.All_Possible_Guesses
        matching_characters = ['a','a','h','e']
        matching_indexes = [0,1,2,3]
        non_matching_contained = []

        all_indexes = World_Player.all_valid_guesses(Cur_Valid_Guesses, matching_characters, matching_indexes, non_matching_contained):


        self.assertTrue(5 == len(all_indexes))




if __name__ == '__main__':
    unittest.main()