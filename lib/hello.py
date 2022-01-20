from curses.ascii import islower
from typing import List
from nltk.tokenize import wordpunct_tokenize
from nltk.probability import FreqDist
import os

words: List[str] = []

fdist = FreqDist()

for filename in os.listdir(os.getcwd() + '/data'):
  with open(os.path.join(os.getcwd() + '/data', filename), 'r') as f:
    content = f.read()
    words = (word for word in wordpunct_tokenize(content) if (len(word) == 5 and word.islower()))
    fdist.update(words)
    # words = words + word_tokenize(content)

items = len(list(fdist))

out_lines = (f"{word} {count}" for (word, count) in fdist.most_common(50000))

for line in out_lines:
  print(line)

# fdist = FreqDist(words)
