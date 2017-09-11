word = 'CahahahHaaaha'
new_word = word[1:]
for thing in new_word:
    if thing == thing.upper():
        spot = new_word.index(thing)
        print(word[:spot + 1])
        print(word[spot + 1:])