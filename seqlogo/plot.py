#!/usr/bin/env python3

import logomaker
import matplotlib.pyplot as plt
from .seq_logo import seq_prob_matrix

color_options = ['base_pairing', # for DNA and RNA only
                 'highlight_first', 
                 'charge', # for amino acids only
                 'hydrophobicity'] # for amino acids only

def make_plot_seq_prob(sequences, 
                       output_path, 
                       coloring = "", 
                       nuc_acid = True):

    # handle bad color options for selected chars
    if coloring not in color_options: coloring = ''
    if not nuc_acid and coloring in color_options[:1]: coloring = ''
    if nuc_acid and coloring in color_options[2:]: coloring = ''

    probs = seq_prob_matrix(sequences)
    fig, ax = plt.subplots(1, 1, figsize=[4,2.5])
    if coloring in ['', 'highlight_first']:
        logo = logomaker.Logo(probs)
    else: 
        logo = logomaker.Logo(probs, color_scheme = coloring)

    if coloring == 'highlight_first': 
        highlight = sequences[0]
        for i, char in enumerate(highlight):
            # p is 1-based position
            logo.style_single_glyph(c=char.upper(), p=i + 1, color = [1, 0, 0])

    plt.ylabel("Probability")

    logo.draw()
    plt.savefig(output_path)

if __name__ == "__main__":
    sequences = ["AAAAA", 
                 "CCCCC", 
                 "GGGGG", 
                 "TTTTT", 
                 "UUUUU"]
    make_plot_seq_prob(sequences, '../output/plot_testout.py')
