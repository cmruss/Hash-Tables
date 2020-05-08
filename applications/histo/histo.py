# Implement me.
def histo(s):
    if len(s) < 1:
        return {}
    else:
        cache = {}
        # remove unnessecary spaces, then split by lingering space
        s = " ".join(s.split()).lower().split(" ")
        for word in s:
            # loop through words, removing objectionable characters 
            word = word.strip('":;,.-+=/\|[]}{()*^&')
            # if the word's in the cache, increment count
            if cache.get(f"{word}"):
                cache[word] += 1
            # if not, add it as the first instance
            elif len(word) >= 1: # if it has a value
                cache[word] = 1
        # turning a dict to a list to sort it
        words = list(cache.items()) 
        # sorting it
        words.sort(key=(lambda e: (-e[-1], e[0])))
        for word, occ in words:
            # print the key and visualize the value 
            # here by multiplying the value by a printed pound
            word = word + " " * (17 - len(word)) + "#" * occ
            print(word)

if __name__ == "__main__":
    print(histo(""))
    print(histo("Hello"))
    print(histo('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(histo('This is a test of the emergency broadcast network. This is only a test.'))