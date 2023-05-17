# Untitled.py
# Created by Kids on 5/15/23.
import AllWordsLists.all_words_word_frequency as all_words
import AllWordsLists.all_words_letter_frequency as all_words2
import sorting_formula as sorter
import heuristics as heuristics
if __name__ == "__main__":
	print("all_words = " + str(sorter.combined_sorter(all_words.all_words, all_words2.all_words)))
#	print("all_words = " + str(sorted(all_words2.all_words, key=lambda x: heuristics.sorter(x))))