import all_words as all_word_file
#NEW ERROR, IF THERE ARE IS A YELLOW LETTER AND A GREEN OF THE SAME LETTER, THE BOT MAY GIVE A WORD WITH ONLY ONE LETTER IN THE GREEN'S POSITION
#NEW Error, Word was hasty, guessed slate, wants, tasty, then it told me to guess tasty again
def main():
	print("WordleWin is meant to be used as a solver of games style like the New York Times Wordle. After your first guess, input the word and colors of each letter into the program (g-green, y-yellow, and w-white/gray). The program will return a word for you to guess. continue until you have solved the Wordle.\n")
	next_guess_input = all_word_file.all_words
	for o in range(0, 6):
#		print()

		next_guess_input = guesser(next_guess_input)
		if next_guess_input == "You won!":
			print("Congratulations! you solved the Wordle in " + str(o+1) + " guesses!")
			break
		print("WordleWin reccomends your next guess is: " + next_guess_input[0])
		print("Other words are" + str(next_guess_input))

def guesser(viable_words):
	guess = input("What was your next Wordle guess?\n")#//the guess variable is already created//
	color = input("What was the color coding of your Wordle?\n")
	if color == "ggggg":
		return "You won!"
	ht_of_green = {}
	ht_of_yellow = {}
	gray_letters = ""
	for i in range(0, 5):
		if color[i] == "g":
			if guess[i] not in ht_of_green:
				ht_of_green[guess[i]] = [i]
			else:
				ht_of_green[guess[i]].append(i)
		elif color[i] == "y":
			if guess[i] not in ht_of_yellow:
				ht_of_yellow[guess[i]] = [i]
			else:
				ht_of_yellow[guess[i]].append(i)	
		elif color[i] == "w":
			gray_letters += guess[i]
		else:
			raise exception("colors should only be g, w, y")#Shouldn't terminate
	all_viable_words = []
	for j in viable_words:
		is_viable = True
		for l in ht_of_yellow:
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
		for o in ht_of_green:
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
		for n in gray_letters:
			if n not in ht_of_green and n not in ht_of_yellow:
				if n in j:
					is_viable = False
					break
		if is_viable:
			all_viable_words.append(j)
	return all_viable_words
		 
if __name__ ==  "__main__":
	main()