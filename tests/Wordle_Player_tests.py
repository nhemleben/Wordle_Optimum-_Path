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


    def test_prob_of_character(self):
        Cur_Valid_Answers = ['aaaaa', 'aaaab', 'aaaab']
        val = World_Player.probability_of_character_in_pos(Cur_Valid_Answers, 'a', 0)
        self.assertTrue(1 == val)

    def test_prob_of_character_end(self):
        Cur_Valid_Answers = ['aaaaa', 'aaaab', 'aaaab']
        val = World_Player.probability_of_character_in_pos(Cur_Valid_Answers, 'a', 4)
        self.assertTrue((1/3) == val)

    def test_prob_of_character_table(self):
        Cur_Valid_Answers = ['aaaaa', 'aaaab', 'aaaab']
        probs = World_Player.probability_of_all_char_in_pos(Cur_Valid_Answers, 0)
        self.assertTrue(1 == probs[0])

    def test_prob_of_character_table_end(self):
        Cur_Valid_Answers = ['aaaaa', 'aaaab', 'aaaab']
        probs = World_Player.probability_of_all_char_in_pos(Cur_Valid_Answers, 4)
        self.assertTrue((1/3) == probs[0])
        self.assertTrue((2/3) == probs[1])

    def test_greedy_naive_guesser_aaaab(self):
        Cur_Valid_Answers = ['aaaaa', 'aaaab', 'aaaab']
        Cur_Valid_Guesses = ['aaaaa', 'aaaab', 'aaaab']

        naive = World_Player.greedy_naive_guesser(Cur_Valid_Answers, Cur_Valid_Guesses )

        self.assertTrue(naive == 'aaaab')

    def test_greedy_naive_guesser_baaaa_1(self):
        Cur_Valid_Answers = ['aaaaa', 'baaaa', 'baaaa']
        Cur_Valid_Guesses = ['aaaaa', 'baaaa', 'baaaa']

        naive = World_Player.greedy_naive_guesser(Cur_Valid_Answers, Cur_Valid_Guesses )

        self.assertTrue(naive == 'baaaa')

    def test_greedy_naive_guesser_baaaa_2(self):
        Cur_Valid_Answers = ['aaaaa', 'baaaa', 'bbaaa']
        Cur_Valid_Guesses = ['aaaaa', 'baaaa', 'bbaaa']

        naive = World_Player.greedy_naive_guesser(Cur_Valid_Answers, Cur_Valid_Guesses )

        self.assertTrue(naive == 'baaaa')

    def test_greedy_naive_guesser_answers_and_guesses_differ(self):
        Cur_Valid_Answers = ['aaaaa', 'baaac', 'bbaac']
        Cur_Valid_Guesses = ['aaaaa', 'baaac', 'bbaac', 'baaaa', 'bbaaa']

        naive = World_Player.greedy_naive_guesser(Cur_Valid_Answers, Cur_Valid_Guesses )

        self.assertTrue(naive == 'baaac')

    def test_greedy_naive_guesser_optimal_not_guessable(self):
        Cur_Valid_Answers = ['abaac', 'baaac', 'bbaaa']
        Cur_Valid_Guesses = ['abaac', 'baaac', 'bbaaa']

        naive = World_Player.greedy_naive_guesser(Cur_Valid_Answers, Cur_Valid_Guesses )

        #first guess should be bbaac then it should find
        self.assertTrue(naive == 'abaac')


    def test_greedy_naive_guesser_optimal_not_guessable_end_modify(self):
        Cur_Valid_Answers = ['bbbac', 'bbabc', 'bbaaa']
        Cur_Valid_Guesses = ['bbbac', 'bbabc', 'bbaaa']

        naive = World_Player.greedy_naive_guesser(Cur_Valid_Answers, Cur_Valid_Guesses )

        #first guess should be bbaac then it should find
        self.assertTrue(naive == 'bbbac')

if __name__ == '__main__':
    unittest.main()