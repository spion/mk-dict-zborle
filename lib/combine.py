import sys
import os

freq_map = sys.argv[1]
words = sys.argv[2]


with open(os.path.join(os.getcwd(), freq_map), 'r') as f1, open(os.path.join(os.getcwd(), words), 'r') as f2:
    freqs = dict((line[0], line[1]) for line in (line.strip().split(' ') for line in f1.readlines()))
    out_freqs = ((line.strip(), freqs.get(line.strip()) or 0) for line in f2.readlines())
    for (word, freq) in out_freqs:
      print(word, freq)
