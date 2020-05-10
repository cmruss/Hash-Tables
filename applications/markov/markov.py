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
        # if the word's in the cache
        if cache.get(f"{word}"):
            #add it to the prvious word's value
            cache[prev_word].append(word)
        # if the word is not in the cache and the previous word has been set
        elif not cache.get(f"{word}") and len(prev_word) > 0:
            # enter current word into cache with empty list as value
            cache[word] = []
            # append the current word to the previous word's list
            cache[prev_word].append(word)
        else:
            # base case baby
            cache[word] = []
        # set this word to the previous word
        prev_word = word
    # print(cache)
    keys = list(cache.keys())
    random.shuffle(keys)
    sentence = []
    word_count = 0
    new_word = ""
    #loop through the keys
    for word in keys: # until we find a starter word
        if word_count is 0 and word[0].isupper():
            # add it to the sentence
            sentence.append(f"{word}")
            # increment word_count
            word_count += 1
            new_word = random.choice(cache[word])
            break
    # loop until the next word has no values
    while cache[new_word] != []:
            # pick a random word from the value                
            new_word = random.choice(list(cache[new_word]))
            # add it to the sentence
            sentence.append(f"{new_word}")
            word_count += 1
            if new_word[-1] in list(["." ,"?" ,"!"]):
                print(" ".join(sentence))
                # print(cache['to'])
                break
    

# TODO: construct 5 random sentences

markov(words)
markov(words)
markov(words)
markov(words)
markov(words)