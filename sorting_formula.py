def combined_sorter(list1, list2):
	ht_of_words = {}
	for i in range(0, len(list1)):
		ht_of_words[list1[i]] = i+(list2.index(list1[i])*2.5)
	return sorted(list1, key=lambda x: ht_of_words[x])
	