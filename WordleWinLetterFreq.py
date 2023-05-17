import AllWordsLists.all_words_letter_frequency as all_word_file #Stanford list of all 5 letter words, previously according to frequency by Words Api
#NEW ERROR, IF THERE ARE IS A YELLOW LETTER AND A GREEN OF THE SAME LETTER, THE BOT MAY GIVE A WORD WITH ONLY ONE LETTER IN THE GREEN'S POSITION
#NEW Error, Word was hasty, guessed slate, wants, tasty, then it told me to guess tasty again
def main(): #driver
	print("WordleWin is meant to be used as a solver of games style like the New York Times Wordle. After your first guess, input the word and colors of each letter into the program (g-green, y-yellow, and w-white/gray). The program will return a word for you to guess. continue until you have solved the Wordle.\n") #user instructions
	next_guess_input = all_word_file.all_words #simplifying the list to a variable
#	print(next_guess_input)
#	print("len next_guess_input" + str(len(next_guess_input)))
	for o in range(0, 6): #all code for each guess
		next_guess_input = guesser(next_guess_input, o) #thinning the list of viable words according to new color data
#		print("WordleWin recommends your next guess is: " + next_guess_input[0]) #giving user next guess
		print("Other words are" + str(next_guess_input)) #showing user all other remaing words

def guesser(viable_words, o): # function for each individual guess
	if o == 0:
		guess = input("What was your first Wordle guess?\n") #what the user's word was
	else:
		guess = input("What was your next Wordle guess?\n") #what the user's word was
	color = input("What was the color coding of your Wordle?\n") #what colors (white green yellow) the user had
	if color == "ggggg": #checking for win
		print("Congratulations! you solved the Wordle in " + str(o+1) + " guesses!")
		exit()
	ht_of_green = {} #holding the green letters and their location
	ht_of_yellow = {} #holding the yellow letters and their loaction
	gray_letters = "" # holding the gray letters
	for i in range(0, 5): #adding the colors to their respective arrays and dictionaries 
		if color[i] == "g": #adding to green
			if guess[i] not in ht_of_green:
				ht_of_green[guess[i]] = [i]
			else:
				ht_of_green[guess[i]].append(i)
		elif color[i] == "y": #adding to yellow
			if guess[i] not in ht_of_yellow:
				ht_of_yellow[guess[i]] = [i]
			else:
				ht_of_yellow[guess[i]].append(i)	
		elif color[i] == "w": #adding to gray
			gray_letters += guess[i]
		else: #error checking
			raise exception("colors should only be g, w, y")#Shouldn't terminate
	all_viable_words = [] #empty list off all new viable words
	for j in viable_words: #going through old viable words, eliminating based of off the colors (above)
		is_viable = True #acts like a while loop, if the word doesn't meet any criteria, it is eliminated
		for l in ht_of_yellow: #checking all of the yellow letters, if it is in the word, if the right number of it is in the word, if it is in the right location
			if l not in j:
				is_viable = False
				break
			if j.count(l) < len(ht_of_yellow[l]):
				is_viable = False
				break
			for m in ht_of_yellow[l]:
				if j[m] == l:
					is_viable = False
					break
		for o in ht_of_green: #checking all of the green letters, if it is in the word, if the right number of it is in the word, if it is in the right location
			if o not in j:
				is_viable = False
				break
			if j.count(o) < len(ht_of_green[o]):
				is_viable = False
				break
			for p in ht_of_green[o]:
				if j[p] != o:
					is_viable = False
					break
		for n in gray_letters: #If a gray letter is in the word, it is to be eliminated
			if n not in ht_of_green and n not in ht_of_yellow:
				if n in j:
					is_viable = False
					break
		if is_viable: #if the word passes all criteria, it is added to the new list
			all_viable_words.append(j)
	return all_viable_words #returnis all viable words
		 
if __name__ ==  "__main__":
	main()