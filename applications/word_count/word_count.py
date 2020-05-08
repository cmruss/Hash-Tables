def word_count(s):
    # Implement me.
    if len(s) < 1:
        return {}
    else:
        cache = {}
        s = " ".join(s.split()).lower().split(" ")
        for word in s:
            word = word.strip('":;,.-+=/\|[]}{()*^&')
            if cache.get(f"{word}"):
                cache[word] += 1
            elif len(word) >= 1:
                cache[word] = 1
        return cache

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))