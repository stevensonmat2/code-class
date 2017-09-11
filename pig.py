word = input('write word: ')
def piggy(word):


    if word[0] == ('a' or 'e' or 'i' or 'o' or 'u'):
        return(f'{word}yay'.capitalize())
    else:
        return(f'{word[1:]}{word[0]}ay'.capitalize())

word_list = word.split()
translated = []
for w in word_list:
    translated.append(piggy(w))
print(" ".join(translated))
