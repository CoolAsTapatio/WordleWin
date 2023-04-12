# Untitled.py
# Created by Kids on 2/27/23.
# Git personal access token: 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
import requests
import json

def main():
	print("WordleWin is meant to be used as a solver of games style like the New York Times Wordle. After your first guess, input the word and colors of each letter into the program (g-green, y-yellow, and w-white/gray). The program will return a word for you to guess. continue until you have solved the Wordle.\n")
	guess = input("What was your first Wordle guess?\n")#//the guess variable is already created//
	color = input("What was the color coding of your Wordle?\n")
	ht_of_yellow = {}
	gray_letters = ""
	query_param = ""# //what goes into the query for the letters//
	for i in range(0, 5):
		if color[i] == "g":
			query_param += guess[i]
		elif color[i] == "y":
			if guess[i] not in ht_of_yellow:
				ht_of_yellow[guess[i]] = [i]
				query_param += "[a-z]"
			else:
				ht_of_yellow[guess[i]].append(i)	
				query_param += "[a-z]"
		elif color[i] == "w":
			gray_letters += guess[i]
			query_param += "[a-z]"
		else:
			raise exception("colors should only be g, w, y")
	all_words_in_param = query(query_param)
#	print(query_param)
#	print(query(query_param))
	all_viable_words = []
	for j in all_words_in_param:
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
		for n in gray_letters:
			if n not in ht_of_yellow:
				if n in j:
					is_viable = False
					break
		if is_viable:
			all_viable_words.append(j)
	#################
	################
	###############
	best_guess,sorted_viable_words = sort_viable_words(all_viable_words)
	print(sort_viable_words)
	print("WordleWin reccomends your next guess is:" + best_guess)
	next_guess_input = all_viable_words
	for o in range(0, 5):
		next_guess_input = guesser(next_guess_input)
		print("WordleWin reccomends your next guess is:" + next_guess_input[0])
		if next_guess_input == "You won!":
			break
			


#def sort_viable_words(viable_words):
#	words_with_frequency = {}
#	frequencies = []
#	for i in viable_words:
#		frequency = frequence_getter(i)
#		words_with_frequency[i] = frequency
#		frequencies.append(frequency)
#	frequencies.sort(reverse=True)
#	sorted_words = []
#	for j in frequencies:
#		for k in words_with_frequency:
#			if words_with_frequency[k] == j: 
#				sorted_words.append(k)
#	return sorted_words[0], sorted_words


def sort_viable_words(viable_words):
	viable_words.sort(key=lambda x:frequence_getter(x), reverse=True)
	print("viable words:" + str(viable_words))
	return viable_words[0], viable_words
	
	
def frequence_getter(word):
	try:
		headers={"X-RapidAPI-Key": "12c2e794e4msh65bd636dedd764ep1a7ef5jsn710b1816978d", "Accept": "application/json", "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"}
		r = requests.request("GET", "https://wordsapiv1.p.rapidapi.com/words/" + word, headers=headers)
		#print(word)
		return json.loads(r.text)["frequency"]
	except:
		return 0

def guesser(viable_words):
	guess = input("What was your next Wordle guess?\n")#//the guess variable is already created//
	color = input("What was the color coding of your Wordle?\n")
	if color == "ggggg":
		return "You won!"
	ht_of_green = {}
	ht_of_yellow = {}
#	ht_of_white = {}
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
#			if guess[i] not in ht_of_white:
#				ht_of_white[guess[i]] = [i]
#			else:
#				ht_of_white[guess[i]].append(i)

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
#			if j.count(n) < len(ht_of_white[n]):
#				is_viable = False
#				break
#			for q in ht_of_white[n]:
#				if j[q] != n:
#					is_viable = False
#					break
		if is_viable:
			all_viable_words.append(j)
	return all_viable_words

def query(query_param):
	headers={"X-RapidAPI-Key": "12c2e794e4msh65bd636dedd764ep1a7ef5jsn710b1816978d", "Accept": "application/json", "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"}
	r = requests.request("GET", "https://wordsapiv1.p.rapidapi.com/words/?letters=5&limit=100000&letterPattern=^" + query_param + "$", headers=headers)
	return json.loads(r.text)['results']['data']

		 
if __name__ ==  "__main__":
	main()
			