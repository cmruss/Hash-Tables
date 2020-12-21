import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    # print(words)

# TODO: analyze which words can follow other words
def markov(s):
    # our dictionary
    cache = {}
    # makes the string a list, removing extra spaces
    s = " ".join(s.split()).split(" ")
    # initialize prev_word for loop
    prev_word = ""
    # loop through the new list
    for word in s:
        # remove characters
        word = word.strip('()"}{')
        # if the word's in the cache
        if cache.get(f"{word}"):
            # just add it to the prvious word's value
            cache[prev_word].append(word) 
        else: # if the word is not in the cache
            # enter current word into cache with empty list as value
            cache[word] = []
            # if the previous word has been set
            if len(prev_word) > 0:
                # append the current word to the previous word's list
                cache[prev_word].append(word)
        # set this word to the previous word
        prev_word = word
    # print(cache)
    # make the dict keys a list so we can randomly iterate
    keys = list(cache.keys())
    # sort the list randomly
    random.shuffle(keys)
    # intialize sentence as a list of words 
    sentence = []
    # initialize word count
    word_count = 0
    # initialize new_word for next word
    new_word = ""
    #loop through the keys
    for word in keys: # until we find a starter word
        if word_count is 0 and word[0].isupper():
            # add it to the sentence
            sentence.append(f"{word}")
            # increment word_count
            word_count += 1
            # make a word in the cache list the new word
            new_word = random.choice(cache[word])
            # exit loop
            break
    # loop until the next word has no values
    while cache[new_word] != []:
            # pick a random word from the value                
            new_word = random.choice(cache[new_word])
            # add it to the sentence
            sentence.append(f"{new_word}")
            word_count += 1
            # if the last character in the added word is one of these..
            if new_word[-1] in list(["." ,"?" ,"!"]):
                return (" ".join(sentence), word_count)

# TODO: construct 5 random sentences

print(markov(words))
print(markov(words))
print(markov(words))
print(markov(words))
print(markov(words))
print(markov(words))