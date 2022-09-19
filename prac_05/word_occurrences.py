"""CP1404_practical"""

count_word = {}
text = input("Text:")
words = text.split()
for word in words:
    times = count_word.get(word,0)
    count_word[word] = times + 1

words = list(count_word.keys())
words.sort()

max_length = max((len(word)for word in words))
for word in words:
    print("{:{}} = {}".format(word,max_length,count_word[word]))
