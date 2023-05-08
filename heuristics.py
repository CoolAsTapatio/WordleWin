def sorter(word):#formula = frequency, reciprocal letter frequency (gets less important each guess), unique letters
	letter_value = {'a':1 , 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':8, 'w':4, 'x':8, 'y':4, 'z':10}
	letters_in_word = []
	letter_score = 0
	for j in word:
		letter_score += letter_value[j]
		if letter_value[j] in letters_in_word:
			letter_score/2
		letters_in_word.append(letter_value[j])
		
#	print(letter_score)
	return letter_score