import sys
import os
import math
from string import punctuation

words_used = []
positive_counter = 0
negative_counter = 0
total_words = 0
page_counter = 1

pos_words = open('positive.txt').read()
pos_words = pos_words.split("\n")

neg_words = open('negative.txt').read()
neg_words = neg_words.split("\n")

if len(sys.argv) < 2:
	print('Usage: python text_sentiment.py document.txt')
	sys.exit(1)

for filename in sys.argv[1:]:
	words_used = open(filename).read()
	words_used = words_used.lower()

	for p in list(punctuation):
		words_used = words_used.replace(p,'')

	for word in words_used.split():
		if word in pos_words:
			positive_counter = positive_counter+1
			total_words = total_words+1
		elif word in neg_words:
			negative_counter = negative_counter+1
			total_words = total_words+1
		else:
			total_words = total_words+1

	print('')
	print('File: %s' % (
		filename
	))
	print('%d positives, %d negatives, %d words' % (
		positive_counter, negative_counter, total_words
	))
	print('Ouderkirk Sentiment Score: %d' % (
		total_words / (positive_counter - negative_counter)
	))
