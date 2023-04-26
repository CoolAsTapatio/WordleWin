def sorter(frequency, word):#formula = frequency, reciprocal letter frequency (gets less important each guess), unique letters
	letter_value = {'a':1 , 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':8, 'w':4, 'x':8, 'y':4, 'z':10}
	letter_score = 0
	for i in word:
		letter_score += letter_value[i]
	return (100*frequency/letter_score)/2