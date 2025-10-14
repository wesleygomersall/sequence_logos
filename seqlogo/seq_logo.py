#!/usr/bin/env python3 

import os
import argparse
import logomaker
import pandas as pd
import matplotlib.pyplot as plt

def read_sequence_file(path: str):
    sequence_list = pd.read_csv(path, header = None)[0].to_list()
    return sequence_list

def check_seq_lengths(sequence_list):
    ''' Assert all sequences have same length and return that length '''
    seqlen = 0
    for i, s in enumerate(sequence_list):
        if i == 0: seqlen = len(s)
        elif seqlen != len(s):
            raise ValueError(f"len(seq{i + 1} = {len(s)} differs from first sequence ({seqlen}).")
    return seqlen

def seq_prob_matrix(sequences: list[str]):
    '''
    Calculate the probability matrix for characters in sequences list. For use
    with logomaker, function returns "matrix specifying character heights and
    positions. Rows correspond to positions while columns correspond to
    characters. Column names must be single characters and row indices must be
    integers." 
    '''
    n_positions = check_seq_lengths(sequences)
    characters = set()
    for sequence in sequences:
        characters.update(list(sequence))
    
    column_names = sorted(list(characters))
    row_indices = range(n_positions)
    char_heights = pd.DataFrame(0.0, index= row_indices, columns= column_names)
    for position in range(n_positions):
        for sequence in sequences:
            character = sequence[position]
            char_heights.loc[position, character] += 1 / len(sequences)

    return char_heights

def make_plot_seq_prob(sequences, output_path):
    probs = seq_prob_matrix(sequences)
    fig, ax = plt.subplots(1, 1, figsize=[4,2])
    logo = logomaker.Logo(probs)
    logo.draw()
    plt.savefig(output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--input", "-i", type=str, help="Input file path")
    parser.add_argument("--output", "-o", type=str, help="Output file path")
    args = parser.parse_args()

    sequence_list = read_sequence_file(args.input)
    make_plot_seq_prob(sequence_list, args.output)
