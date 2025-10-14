# Sequence Logos

![](output/sample_seq_logo_plot.png)

### Usage

Takes input sequences from text file: 

```
TFFRLFNRSFTQALGK
PWEKIFLYAFVVALQL
PWEKIFLFAFLMALLF
PWEKIFLFAFLMALLF
...
PWEKIFLFAFLMALLF
PWEKIFLFAFLMALLF
WWEEIFMYAFLMALLF
WWKEIFLFAFLMALLF
```

```
$ ./main.py -h

usage: main.py [-h] [--input INPUT] [--aminos] [--color COLOR]

options:
  -h, --help         show this help message and exit
  --input, -i INPUT  Input file path
  --aminos, -a       Specify amino acid characters for coloring plot.
  --color, -c COLOR  Color options: ['base_pairing', 'highlight_first',
                     'charge', 'hydrophobicity'] 'basepairs' only available if
                     -a false. Latter 2 options only available if -a true.
```

### Dependencies: 
- pandas
- matplotlib
- logomaker https://github.com/jbkinney/logomaker

Use conda environment from `environment.yml`:

```
conda env create -f environment.yml
conda activate seqlogo
```
