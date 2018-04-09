def remove_more_than_two_duplicate_letters(word):
    answer = word[0:2]
    for i in range(2, len(word)):
        if word[i] != word[i-1] or word[i] != word[i-2]:
            answer += word[i]
    return answer