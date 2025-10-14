#!/usr/bin/env python3

import unittest
import random
import string
import pandas as pd
from seqlogo import seq_logo

test_sequences = ["AAAAA", "CCCCC", "GGGGG", "TTTTT", "TTTTT", "CCGGC", "NNNNN"]

def generate_sequences(n_sequences: int = 100, 
                       length: int = 10, 
                       chars: str = 'ATGC'):
    '''
    Generate n sequences of some length using characters present in specified
    string.
    '''
    sequences = []
    for _ in range(n_sequences):
        sequences.append(''.join([random.choice(chars) for _ in range(length)]))
    return sequences

class TestFileRead(unittest.TestCase):

    def test_file_exists(self):
        real_file = 'tests/inputs/testinput1.txt'
        self.assertIsNotNone(seq_logo.read_sequence_file(real_file))

        with self.assertRaises(FileNotFoundError):
            fake_file = '/path/to/fake/file.txt'
            seq_logo.read_sequence_file(fake_file)

class TestLengthChecker(unittest.TestCase):

    def test_check_lengths(self):
        self.assertEqual(seq_logo.check_seq_lengths(["ACTG","GTCA","GTCA"]), 4)
        self.assertEqual(seq_logo.check_seq_lengths(["ACTGA","ACTGA"]), 5)

    def test_check_lengths_fails(self): 
        with self.assertRaises(ValueError):
            test_sequences2 = ["ACTG","ACTG","GTCA","GTCAA"]
            seq_logo.check_seq_lengths(test_sequences2)

class TestProbMatrix(unittest.TestCase):
    def test_ordering(self):
        arr = [[0.6, 0.2, 0.2], 
               [0.2, 0.4, 0.4], 
               [0.8, 0.2, 0.0]]
        ideal_mat = pd.DataFrame(arr, index=range(3), columns=['A', 'B', 'C'])

        mylist = ["AAA","ABB","ABA","BCA","CCA"]
        calced_mat = seq_logo.seq_prob_matrix(mylist)

        pd.testing.assert_frame_equal(ideal_mat, calced_mat)

    def test_sum(self, error=1e-10):
        '''
        Check that rows sum to approximately 1.
        '''
        r_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        sequences = generate_sequences(1000, 10, r_string)
        mat = seq_logo.seq_prob_matrix(sequences)
        assert all([sum(mat.iloc[r]) - 1 < error for r in mat.index])

if __name__ == "__main__":
    unittest.main()
