def remove_more_than_two_duplicate_letters(word):
    answer = word[0:2]
    for i in range(2, len(word)):
        if word[i] != word[i-1] or word[i] != word[i-2]:
            answer += word[i]
    return answer

def get_correction_dicts():
	'''	Loads 3 dictionaries with the correct substitions
		for words. Most commonly mistakes while tweeting.
	'''
	words = {}
	# Dict1 structure: number wrong_typed_word | corrected_word

	with open('dict1.txt', 'rb') as word_file:
		for word in word_file:
			word = word.decode('utf-8').split()
			words[word[1]] = word[3]

	# Dict2 structure: wrong_word corrected_word
	with open('data/dict2.txt', 'rb') as word_file:
		for word in word_file:
			word = word.decode('utf-8').split()
			words[word[0]] = word[1]

	# Dict3 structure: wrong_word corrected_word
	with open('data/dict3.txt', 'rb') as word_file:
		for word in word_file:
			word = word.decode('utf-8').split()
			words[word[0]] = word[1]

	return words

def correct_spelling(word_list, word_dictionary):
	'''	Corrects the given sentence (list of words)
		Replaces it with the correct word if found in dictionary,
		Returns the same word otherwise.
	'''
	for i in range(len(word_list)):
		if word_list[i] in word_dictionary.keys():
			word_list[i] = word_dictionary[word_list[i]]

	return word_list


