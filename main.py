#!/usr/bin/env python3

import os
import argparse 
from datetime import datetime
from seqlogo.seq_logo import read_sequence_file, make_plot_seq_prob

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--input", "-i", type=str, help="Input file path")
    args = parser.parse_args()

    date_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    outputdir = os.path.dirname(__file__) + '/output/' 
    input_base_name = os.path.splitext(os.path.basename(args.input))[0] 
    output_path = outputdir + date_time + '_' + input_base_name + '_sequencelogo.pdf'
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)

    sequence_list = read_sequence_file(args.input)
    make_plot_seq_prob(sequence_list, output_path)
