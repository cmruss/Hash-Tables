import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    # print(words)

# TODO: analyze which words can follow other words
def markov(s):
    cache = {}
    s = " ".join(s.split()).split(" ")
    prev_word = ""
    # loop through the new list
    for word in s:
        word = word.strip('()"}{')
        # print(word)
        # base case.. but not? seems to work when a word is reused consecutively
        if len(prev_word) < 1 or not cache.get(f"{word}"):
            cache[word] = []
        # if the previous word is in the cache
        if cache.get(f"{prev_word}"):
            # add this word to the previous' word's list of following words
            cache[prev_word].append(word)
        # if the word is not in the cache
        elif not cache.get(f"word") and len(prev_word) > 0:
            # enter current word into cache with empty list as value
            cache[word] = []
            # print(cache)
            # append the current word to the previous word's list
            cache[prev_word].append(word)
        # set this word to the previous word
        prev_word = word
    # print(cache)
    keys = list(cache.keys())
    random.shuffle(keys)
    sentence = []
    joined_sentence = " "
    word_count = 0
    new_word = ""
    #loop through the keys
    for word in keys: # until we find a starter word
        # print(word)
        if word_count is 0 and word[0].isupper():
            # print(word)
            # add it to the sentence
            sentence.append(f"{word}")
            # increment word_count
            word_count += 1
            new_word = random.choice(cache[word])
            break
    # loop until the next word is an ending word
    while new_word[-1] not in ["." ,"?" ,"!"]:
    # if the cache has words stored for that key
        if len(cache[new_word]) >= 1:
            # pick a random word from there                 
            new_word = random.choice(list(cache[new_word]))
            # add it to the sentence
            sentence.append(f"{new_word}")
            word_count += 1
        else:
            break

    print(joined_sentence.join(sentence))

# TODO: construct 5 random sentences

markov(words)
markov(words)
markov(words)
markov(words)
markov(words)